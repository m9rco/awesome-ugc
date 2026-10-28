"""Regenerate the catalog tables and stats block inside README.md from data/catalog.json.

Usage:
    python scripts/build_readme.py            # rewrite README.md in place
    python scripts/build_readme.py --check    # exit 1 if README.md is out of sync (CI)

The generated regions are delimited by HTML comments so hand-written prose around
them is never touched.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "catalog.json"
README = ROOT / "README.md"

CATALOG_BEGIN = "<!-- CATALOG:BEGIN -->"
CATALOG_END = "<!-- CATALOG:END -->"
STATS_BEGIN = "<!-- STATS:BEGIN -->"
STATS_END = "<!-- STATS:END -->"
EMPTY_STAGE = "—"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def replace_region(text: str, begin: str, end: str, body: str) -> str:
    start = text.find(begin)
    stop = text.find(end)
    if start == -1 or stop == -1 or stop < start:
        raise SystemExit(f"README.md is missing the {begin} / {end} markers")
    return f"{text[:start]}{begin}\n{body.rstrip()}\n{text[stop:]}"


def render_catalog(data: dict[str, Any]) -> str:
    entries = data.get("entries") or []
    categories = {item["id"]: item["name"] for item in data["categories"]}
    stages = {item["id"]: item["name"] for item in data["stages"]}
    cat_order = {item["id"]: index for index, item in enumerate(data["categories"])}

    blocks: list[str] = []
    for platform in data["platforms"]:
        rows = [item for item in entries if item.get("platform") == platform["id"]]
        header = f"### {platform['name']}\n\n{platform['desc']}"
        if platform.get("doc"):
            header += f"\n\n> 深度笔记：[{platform['doc']}]({platform['doc']})"
        if not rows:
            blocks.append(f"{header}\n\n_待收录。_\n")
            continue

        ordered = sorted(
            rows,
            key=lambda item: (cat_order.get(item["category"], 99), item["name"].lower()),
        )
        lines = ["| 名称 | 类别 | 工序 | 说明 |", "| --- | --- | --- | --- |"]
        for item in ordered:
            stage = stages.get(item.get("stage") or "", EMPTY_STAGE)
            summary = item["summary"].replace("|", "\\|")
            label = categories.get(item["category"], item["category"])
            lines.append(f"| [{item['name']}]({item['url']}) | {label} | {stage} | {summary} |")
        blocks.append(f"{header}\n\n" + "\n".join(lines) + "\n")
    return "\n".join(blocks)


def render_stats(data: dict[str, Any]) -> str:
    entries = data.get("entries") or []
    platforms = {item["id"]: item["name"] for item in data["platforms"]}
    categories = {item["id"]: item["name"] for item in data["categories"]}

    def tally(key: str, labels: dict[str, str]) -> str:
        counts: dict[str, int] = {}
        for item in entries:
            value = item.get(key)
            if value:
                counts[value] = counts.get(value, 0) + 1
        ordered = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
        parts = [f"{labels.get(k, k)} {v}" for k, v in ordered]
        return " · ".join(parts) if parts else "—"

    verified = sum(1 for item in entries if item.get("http_status") == 200)
    catalog_line = (
        f"- 数据文件：`data/catalog.json`"
        f"（schema v{data['schema_version']}，更新于 {data['updated_at']}）"
    )
    return "\n".join(
        [
            f"- 条目总数：**{len(entries)}**（收录时实测 HTTP 200：{verified}）",
            f"- 按平台：{tally('platform', platforms)}",
            f"- 按类别：{tally('category', categories)}",
            catalog_line,
            f"- 报告生成时间：{date.today().isoformat()}",
        ]
    )


def build(check: bool) -> int:
    data = load(CATALOG)
    text = README.read_text(encoding="utf-8")
    updated = replace_region(text, CATALOG_BEGIN, CATALOG_END, render_catalog(data))
    updated = replace_region(updated, STATS_BEGIN, STATS_END, render_stats(data))

    if check:
        if updated != text:
            print("README.md is out of sync with data/catalog.json", file=sys.stderr)
            print("run: python scripts/build_readme.py", file=sys.stderr)
            return 1
        print("README.md is in sync with data/catalog.json")
        return 0

    README.write_text(updated, encoding="utf-8")
    print(f"README.md regenerated from {len(data.get('entries') or [])} entries")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    return build(parser.parse_args().check)


if __name__ == "__main__":
    raise SystemExit(main())
