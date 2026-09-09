#!/usr/bin/env bash
# Build a flattened, highlighted PDF comparing two committed manuscript revisions.
set -euo pipefail

repo_root=$(cd "$(dirname "$0")/.." && pwd)
base_ref=${1:-HEAD^}
target_ref=${2:-HEAD}
output_arg=${3:-output/pdf/latex-review-diff.pdf}

for command_name in git latexpand latexdiff latexmk; do
  if ! command -v "$command_name" >/dev/null 2>&1; then
    printf 'Missing required command: %s\n' "$command_name" >&2
    exit 2
  fi
done

git -C "$repo_root" cat-file -e "${base_ref}^{commit}"
git -C "$repo_root" cat-file -e "${target_ref}^{commit}"

mkdir -p "$repo_root/tmp/pdfs" "$repo_root/output/pdf"
work_dir=$(mktemp -d "$repo_root/tmp/pdfs/latexdiff.XXXXXX")
trap 'rm -rf "$work_dir"' EXIT

mkdir -p "$work_dir/old" "$work_dir/new"
git -C "$repo_root" archive "$base_ref" | tar -x -C "$work_dir/old"
git -C "$repo_root" archive "$target_ref" | tar -x -C "$work_dir/new"

(
  cd "$work_dir/old"
  latexpand --empty-comments main.tex > "$work_dir/old-flat.tex"
)
(
  cd "$work_dir/new"
  latexpand --empty-comments main.tex > "$work_dir/new-flat.tex"
)

latexdiff --visible-label \
  --label="Baseline ${base_ref}" --label="Audited ${target_ref}" \
  --add-to-config "PICTUREENV=circuitikz" \
  "$work_dir/old-flat.tex" "$work_dir/new-flat.tex" \
  > "$work_dir/new/literature-audit-latexdiff.tex"

(
  cd "$work_dir/new"
  if ! latexmk -pdf -interaction=nonstopmode -halt-on-error \
    literature-audit-latexdiff.tex > "$work_dir/latexmk.log" 2>&1; then
    tail -n 100 "$work_dir/latexmk.log" >&2
    exit 1
  fi
)

if [[ "$output_arg" = /* ]]; then
  output_path=$output_arg
else
  output_path="$repo_root/$output_arg"
fi
mkdir -p "$(dirname "$output_path")"
cp "$work_dir/new/literature-audit-latexdiff.pdf" "$output_path"
printf 'Wrote %s\n' "$output_path"
