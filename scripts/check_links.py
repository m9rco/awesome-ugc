"""Check that every catalog URL is still reachable.

Usage:
    python scripts/check_links.py                 # report only
    python scripts/check_links.py --strict        # non-zero exit on any hard failure
    python scripts/check_links.py --timeout 20 --workers 12 --json reports/links.json

A "hard failure" is a network error (no status at all) or an HTTP status >= 400.
Redirects in the 3xx family are reported but are not failures: many vendor docs
answer 301/302 for legacy paths.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "catalog.json"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 awesome-ugc-linkcheck"
)


def probe(url: str, timeout: float) -> tuple[int | None, str]:
    """Return (status, detail). status is None when the request never completed."""
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return int(response.status), response.geturl()
    except urllib.error.HTTPError as exc:
        return int(exc.code or 0), f"HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001 - the raw reason belongs in the report
        return None, f"{type(exc).__name__}: {exc}"


def load_entries(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(data.get("entries") or [])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=CATALOG)
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--json", type=Path, default=None, help="write a JSON report here")
    parser.add_argument("--strict", action="store_true", help="exit 1 on any hard failure")
    args = parser.parse_args()

    entries = load_entries(args.catalog)
    if not entries:
        print("catalog has no entries yet", file=sys.stderr)
        return 0

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(lambda item: probe(item["url"], args.timeout), entries))

    rows: list[dict[str, Any]] = []
    dead: list[str] = []
    for entry, (status, detail) in zip(entries, results, strict=True):
        rows.append(
            {
                "id": entry.get("id"),
                "url": entry["url"],
                "status": status,
                "detail": detail,
            }
        )
        hard_failure = status is None or status >= 400
        if hard_failure:
            dead.append(entry["url"])
        marker = "DEAD" if hard_failure else ("warn" if status >= 300 else "ok  ")
        print(f"{marker} {str(status):>4}  {entry.get('id', ''):<34} {entry['url']}")

    print(
        f"\nchecked {len(entries)} entries: "
        f"{len(entries) - len(dead)} reachable, {len(dead)} hard failures"
    )
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        payload = {"catalog": str(args.catalog), "results": rows}
        args.json.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"report written to {args.json}")

    return 1 if (args.strict and dead) else 0


if __name__ == "__main__":
    raise SystemExit(main())
