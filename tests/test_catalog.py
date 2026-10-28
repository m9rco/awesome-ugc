"""Structural tests for data/catalog.json and its generated README regions."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "data" / "catalog.json"
README = ROOT / "README.md"

REQUIRED_FIELDS = {
    "id",
    "name",
    "url",
    "lang",
    "category",
    "platform",
    "summary",
    "http_status",
    "added",
}
PRIVATE_HOST = re.compile(r"localhost|127\.0\.0\.1|192\.168\.|\b10\.\d+\.\d+\.\d+|\.local\b")
MIN_ENTRIES = 60


@pytest.fixture(scope="module")
def catalog() -> dict:
    return json.loads(CATALOG.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def entries(catalog: dict) -> list[dict]:
    return list(catalog["entries"])


def test_catalog_shape(catalog: dict) -> None:
    assert catalog["schema_version"] == 1
    assert catalog["updated_at"]
    assert catalog["intro"]
    for key in ("platforms", "categories", "stages"):
        assert catalog[key], f"{key} must not be empty"


def test_entry_fields(entries: list[dict]) -> None:
    for item in entries:
        missing = REQUIRED_FIELDS - item.keys()
        assert not missing, f"{item.get('id')} missing {sorted(missing)}"
        assert item["url"].startswith("https://"), f"{item['id']} must use https"
        assert isinstance(item["http_status"], int)
        assert 200 <= item["http_status"] < 400, f"{item['id']} status {item['http_status']}"
        assert item["lang"] in {"zh", "en"}, f"{item['id']} lang {item['lang']}"
        assert 2 <= len(item["name"]) <= 80, f"{item['id']} name length"
        assert 4 <= len(item["summary"]) <= 100, f"{item['id']} summary length"


def test_vocabularies(catalog: dict, entries: list[dict]) -> None:
    platforms = {item["id"] for item in catalog["platforms"]}
    categories = {item["id"] for item in catalog["categories"]}
    stages = {item["id"] for item in catalog["stages"]}
    for item in entries:
        assert item["platform"] in platforms, f"{item['id']} unknown platform"
        assert item["category"] in categories, f"{item['id']} unknown category"
        assert item.get("stage") in stages | {None}, f"{item['id']} unknown stage"


def test_unique_ids_and_urls(entries: list[dict]) -> None:
    ids = [item["id"] for item in entries]
    urls = [item["url"].rstrip("/") for item in entries]
    assert len(ids) == len(set(ids)), "duplicate entry ids"
    assert len(urls) == len(set(urls)), "duplicate entry urls"


def test_no_private_hosts(entries: list[dict]) -> None:
    for item in entries:
        assert not PRIVATE_HOST.search(item["url"]), f"{item['id']} points at a private host"


def test_catalog_size(entries: list[dict]) -> None:
    assert len(entries) >= MIN_ENTRIES, f"expected >= {MIN_ENTRIES} entries, found {len(entries)}"


def test_readme_is_in_sync() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_readme.py"), "--check"],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_readme_lists_every_entry(entries: list[dict]) -> None:
    text = README.read_text(encoding="utf-8")
    missing = [item["id"] for item in entries if item["url"] not in text]
    assert not missing, f"entries missing from README: {missing[:5]}"


def test_platform_docs_exist(catalog: dict) -> None:
    for platform in catalog["platforms"]:
        doc = platform.get("doc")
        assert doc, f"{platform['id']} has no doc path"
        assert (ROOT / doc).is_file(), f"missing {doc}"
