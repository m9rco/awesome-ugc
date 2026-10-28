# Awesome UGC

**A curated map of the UGC creator ecosystem: platforms, art pipelines, and the AI that actually saves hours.**

[![CI](https://github.com/m9rco/awesome-ugc/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/m9rco/awesome-ugc/actions/workflows/ci.yml)
[![Weekly link check](https://github.com/m9rco/awesome-ugc/actions/workflows/links-weekly.yml/badge.svg?branch=main)](https://github.com/m9rco/awesome-ugc/actions/workflows/links-weekly.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

[简体中文](README.md) · English

The full catalog is maintained in [`README.md`](README.md) and generated from [`data/catalog.json`](data/catalog.json). This page is the English entry point: what the repo is for, how entries are vetted, and where to start.

## What this is

1. **Where UGC ships** — Roblox / Luobulesi, Eggy Party, Dream Star, Aola Star, Mini World, Minecraft: distribution channels, editors, and creator programs.
2. **How the good creators make their art** — concept → three-view sheet → model/paint → texture → store art. See [`docs/ART-PIPELINE.md`](docs/ART-PIPELINE.md).
3. **Which steps AI can actually take over** — tools pinned to a pipeline stage (concept, image, 3D, texture, upscale, background removal, video, audio, batch layout, publishing) instead of a "top AI tools" list. See [`docs/AI-WORKFLOW.md`](docs/AI-WORKFLOW.md).

## How entries are vetted

Every entry carries a measured HTTP status, the page title observed at check time, a one-line purpose, and a license note. No entry is included from memory, and dead links get caught by a weekly probe that opens an issue automatically.

**Included**: official sites and docs, maintained open-source projects, real tutorials and communities, asset libraries with an explicit license page (CC0 / CC-BY / commercial).

**Excluded**: piracy, cracks, cheats, private servers, account or virtual-item trading, pure marketing pages, and unreachable links.

**For AI tools**, three questions decide admission: can the output be used commercially, is it reproducible, and can failures be rolled back in bulk? If one answer is no, the tool stays out of the main pipeline.

## Start here

- [`data/catalog.json`](data/catalog.json) — the single source of truth (schema v1).
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — admission bar and the four commands to run before a PR.
- [`docs/RESEARCH.md`](docs/RESEARCH.md) — research tracks, verification commands, and naming disambiguation records.
- [`docs/ROADMAP.md`](docs/ROADMAP.md) — what is next, and what this repo will not do.

## Repository layout

```text
awesome-ugc/
├── README.md               # 简体中文 (primary, generated tables)
├── README.en.md            # English overview (this file)
├── data/catalog.json       # single source of truth (schema v1)
├── docs/                   # art pipeline, AI workflow, research, roadmap, per-platform notes
├── scripts/                # build_readme.py, check_links.py
└── tests/test_catalog.py   # structure + README sync
```

## License

Code and docs: [MIT](LICENSE). Third-party resources keep their own licenses; this repo only points at them.
