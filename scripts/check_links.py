"""Check that every catalog URL is still reachable.

Usage:
    python scripts/check_links.py                 # report only（直连）
    python scripts/check_links.py --strict        # 有死链就非零退出
    python scripts/check_links.py --proxy http://127.0.0.1:7897
    python scripts/check_links.py --timeout 20 --workers 12 --json reports/links.json

判读规则：
  * `ok`   —— 2xx，命令行可复核；
  * `wall` —— 401/403/429，多半是反爬（Cloudflare/风控），不代表站点下线，需人工或浏览器复核；
  * `DEAD` —— 网络错误或 4xx/5xx（除上面三类），这才是要处理的死链。

`--proxy` 只在直连失败时启用，所以 CI 上不需要配它；本机在受限网络里跑时才用。
"""

from __future__ import annotations

import argparse
import json
import os
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


BLOCKED_STATUS = {401, 403, 429}


def _opener(proxy: str | None) -> urllib.request.OpenerDirector:
    """显式关闭环境变量代理，保证本地跑与 CI 跑行为一致。"""
    mapping = {"http": proxy, "https": proxy} if proxy else {}
    return urllib.request.build_opener(urllib.request.ProxyHandler(mapping))


def probe(url: str, timeout: float, proxy: str | None = None) -> tuple[int | None, str, str]:
    """Return (status, detail, via). status is None when the request never completed.

    先直连；直连失败且给了 --proxy 时再走代理重试（本机常在受限网络里，CI 不需要代理）。
    """
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        },
    )
    try:
        with _opener(None).open(request, timeout=timeout) as response:
            return int(response.status), response.geturl(), "direct"
    except urllib.error.HTTPError as exc:
        status, detail = int(exc.code or 0), f"HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001 - the raw reason belongs in the report
        status, detail = None, f"{type(exc).__name__}: {exc}"

    if proxy and (status is None or (status >= 400 and status not in BLOCKED_STATUS)):
        try:
            with _opener(proxy).open(request, timeout=timeout) as response:
                return int(response.status), response.geturl(), "proxy"
        except urllib.error.HTTPError as exc:
            return int(exc.code or 0), f"HTTP {exc.code}", "proxy"
        except Exception as exc:  # noqa: BLE001
            return None, f"{type(exc).__name__}: {exc}", "proxy"
    return status, detail, "direct"


def load_entries(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(data.get("entries") or [])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=CATALOG)
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--json", type=Path, default=None, help="write a JSON report here")
    parser.add_argument("--strict", action="store_true", help="exit 1 when any URL is dead")
    parser.add_argument(
        "--proxy",
        default=os.environ.get("UGC_LINKCHECK_PROXY", ""),
        help="直连失败时的回退代理，例如 http://127.0.0.1:7897",
    )
    args = parser.parse_args()

    entries = load_entries(args.catalog)
    if not entries:
        print("catalog has no entries yet", file=sys.stderr)
        return 0

    proxy = args.proxy or None
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(
            pool.map(lambda item: probe(item["url"], args.timeout, proxy), entries)
        )

    rows: list[dict[str, Any]] = []
    dead: list[str] = []
    blocked: list[str] = []
    for entry, (status, detail, via) in zip(entries, results, strict=True):
        rows.append(
            {"id": entry.get("id"), "url": entry["url"], "status": status,
             "detail": detail, "via": via}
        )
        if status is None or (status >= 400 and status not in BLOCKED_STATUS):
            dead.append(entry["url"])
            marker = "DEAD"
        elif status in BLOCKED_STATUS:
            blocked.append(entry["url"])
            marker = "wall"
        elif status >= 300:
            marker = "warn"
        else:
            marker = "ok  "
        print(f"{marker} {str(status):>4}  {entry.get('id', ''):<34} {entry['url']}")

    walls = ""
    if blocked:
        names = "、".join(url.split("//")[-1].split("/")[0] for url in blocked[:5])
        walls = f"，{len(blocked)} 条反爬拦截（{names}）"
    print(
        f"\nchecked {len(entries)} entries: "
        f"{len(entries) - len(dead) - len(blocked)} ok, "
        f"{len(blocked)} bot-walled, {len(dead)} dead{walls}"
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
