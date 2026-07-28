#!/usr/bin/env bash
# Health check for "Circuit Theory for the Amateur Extra Exam".
#
# Every check below must report zero. Run it after any edit and before committing:
#
#     ./scripts/check.sh
#
# Exits non-zero if any check fails, so it is safe to chain or use in a hook.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 2

fail=0
note() { printf '%-42s %s\n' "$1" "$2"; }
check() { # name, count, expectation
  if [ "$2" -eq 0 ]; then note "$1" "OK (0)"; else note "$1" "FAIL ($2)"; fail=1; fi
}

echo "=== Building (quiet; see main.log on failure) ==="
if ! make book >/dev/null 2>&1; then
  echo "BUILD FAILED — run 'make book' and read the error." ; exit 2
fi

# --- LaTeX-level health -----------------------------------------------------
check "undefined references"      "$(grep -ci 'undefined' main.log)"
check "overfull boxes > 20pt"     "$(grep -cE 'Overfull.*\(([2-9][0-9]|[0-9]{3,})\.' main.log)"
check "multiply-defined labels"   "$(grep -ci 'multiply defined' main.log)"

# --- cross-reference hygiene ------------------------------------------------
# Labels are stable across renumbering, so numbers must never be hard-coded and
# every label must be reachable.
python3 - <<'PY'
import re, glob, sys
files = glob.glob('chapters/*.tex') + glob.glob('frontmatter/*.tex') + glob.glob('appendices/*.tex')
text = "\n".join(open(f).read() for f in files)
labels = set(re.findall(r'\\label\{([^}]+)\}', text))
refs = set()
for m in re.findall(r'\\[cC]?ref\{([^}]+)\}', text):
    refs.update(p.strip() for p in m.split(','))
orphan, dangling = sorted(labels - refs), sorted(refs - labels)
print(f"{'orphan labels (never \\cref-ed)':<42} {'OK (0)' if not orphan else 'FAIL: ' + ', '.join(orphan)}")
print(f"{'dangling refs (no such label)':<42} {'OK (0)' if not dangling else 'FAIL: ' + ', '.join(dangling)}")
sys.exit(1 if (orphan or dangling) else 0)
PY
[ $? -ne 0 ] && fail=1

check "hard-coded cross-references" \
  "$(grep -nE '(Chapter|Section|Figure|Table|Appendix) *~?[0-9]' \
      chapters/*.tex frontmatter/*.tex appendices/*.tex 2>/dev/null \
      | grep -v '\\label' | wc -l | tr -d ' ')"

# --- glossary must stay alphabetical ---------------------------------------
python3 - <<'PY'
import re, sys
items = re.findall(r'\\item\[([^]]+)\]', open('appendices/glossary.tex').read())
def key(s): return re.sub(r'\\\(.*?\\\)|\\[A-Za-z]+', '', s).lower().strip()
bad = [(b, a) for a, b in zip(items, items[1:]) if key(b) < key(a)]
print(f"{'glossary out of order':<42} "
      + ("OK (0)" if not bad else "FAIL: " + "; ".join(f'{b} after {a}' for b, a in bad)))
print(f"{'glossary entries':<42} {len(items)}")
sys.exit(1 if bad else 0)
PY
[ $? -ne 0 ] && fail=1

# --- every generated figure is included, and vice versa --------------------
python3 - <<'PY'
import re, glob, os, sys
inc = set()
for f in glob.glob('chapters/*.tex'):
    inc |= set(re.findall(r'\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}', open(f).read()))
have = {os.path.splitext(os.path.basename(p))[0] for p in glob.glob('figures/*.pdf')}
missing, unused = sorted(inc - have), sorted(have - inc)
print(f"{'figures included but missing':<42} {'OK (0)' if not missing else 'FAIL: ' + ', '.join(missing)}")
print(f"{'figures present but never included':<42} {'OK (0)' if not unused else 'WARN: ' + ', '.join(unused)}")
sys.exit(1 if missing else 0)
PY
[ $? -ne 0 ] && fail=1

# --- informational ---------------------------------------------------------
echo "=== Summary ==="
note "pages" "$(pdfinfo main.pdf 2>/dev/null | awk '/Pages/{print $2}')"
note "chapters" "$(ls chapters/*.tex | wc -l | tr -d ' ')"
note "figures" "$(ls figures/*.pdf | wc -l | tr -d ' ')"
note "section labels" "$(grep -rhoE '\\label\{sec:[^}]+\}' chapters/ | sort -u | wc -l | tr -d ' ')"

if [ "$fail" -eq 0 ]; then
  echo "ALL CHECKS PASSED"
else
  echo "SOME CHECKS FAILED (see FAIL lines above)"
fi
exit "$fail"
