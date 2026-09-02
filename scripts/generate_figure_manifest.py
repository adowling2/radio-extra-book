#!/usr/bin/env python3
"""Generate the tracked provenance manifest for textbook data figures."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "figures"
PROVENANCE = FIGURES / "provenance"
records = [json.loads(path.read_text(encoding="utf-8"))
           for path in sorted(PROVENANCE.glob("*.json"))]
if len(records) != len(list(FIGURES.glob("*.pdf"))):
    raise SystemExit("provenance sidecars do not cover every generated PDF")
(FIGURES / "manifest.json").write_text(
    json.dumps({"figures": records}, indent=2) + "\n", encoding="utf-8"
)
