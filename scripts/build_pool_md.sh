#!/usr/bin/env bash
# Regenerate the two pool markdown files from the PDFs in references/.
#
# The markdown is derived data: never hand-edit it, edit this pipeline instead.
# Both PDFs must be present; see PROJECT-STATUS.md §5a if they are not.
set -euo pipefail
cd "$(dirname "$0")/.."

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

for pool in Extra General; do
  pdf="references/HamExam.org ${pool} Question Pool.pdf"
  if [ ! -f "$pdf" ]; then
    echo "MISSING: $pdf — see PROJECT-STATUS.md §5a" >&2
    exit 1
  fi
  key=$(echo "$pool" | tr 'A-Z' 'a-z')
  pdftotext -layout "$pdf" "$tmp/$key.txt"
  python3 scripts/parse_pool.py "$tmp/$key.txt" "$tmp/$key.json"
  python3 scripts/emit_md.py "$key" "$tmp/$key.json" \
    "references/${key}-pool-circuits.md"
done

echo "Wrote references/extra-pool-circuits.md and references/general-pool-circuits.md"
