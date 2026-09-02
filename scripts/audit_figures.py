#!/usr/bin/env python3
"""Check source, provenance, and grayscale previews for textbook data figures."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIGURES, SOURCES, AUDIT = ROOT / "figures", ROOT / "figures" / "src", ROOT / "figures" / "audit"
records = json.loads((FIGURES / "manifest.json").read_text(encoding="utf-8"))["figures"]
names = {Path(record["figure"]).stem for record in records}
pdfs = {path.stem for path in FIGURES.glob("*.pdf")}
scripts = {path.stem for path in SOURCES.glob("*.py") if path.name != "_style.py"}
if names != pdfs or pdfs != scripts:
    raise SystemExit("figure PDFs, source scripts, and manifest entries must agree")
if not shutil.which("pdftoppm"):
    raise SystemExit("pdftoppm is required for grayscale previews")
AUDIT.mkdir(exist_ok=True)
for name in sorted(names):
    subprocess.run([
        "pdftoppm", "-f", "1", "-l", "1", "-singlefile", "-gray", "-png",
        str(FIGURES / f"{name}.pdf"), str(AUDIT / f"{name}_grayscale"),
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(f"figure provenance and grayscale previews OK ({len(names)} figures)")
