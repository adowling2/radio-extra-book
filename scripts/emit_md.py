"""Emit the circuits/calculation subset of a parsed pool as markdown."""
import json
import re
import sys
import collections

# Whole subelements are kept or dropped; over-inclusion is deliberate, because a
# question that is missing from this file is a coverage gap we would never notice.
IN_SCOPE = {
    'extra': ['E4', 'E5', 'E6', 'E7', 'E8', 'E9'],
    'general': ['G4', 'G5', 'G6', 'G7', 'G8', 'G9'],
}

NUM = re.compile(r'\d')
# "Figure E7- 2" — the source PDF wraps the line mid-identifier, which breaks grep.
FIGWRAP = re.compile(r'\b([EG]\d)-\s+(\d)\b')
FIGREF = re.compile(r'[Ff]igure\s+([EG]\d-\d)')


def fix(text):
    return FIGWRAP.sub(r'\1-\2', text)


def is_calc(q):
    """A calculation question: every distractor carries a number."""
    return all(NUM.search(t) for _, t in q['answers'])


def figure_of(q):
    """The figure identifier this question cannot be answered without, if any."""
    blob = fix(q['stem'] + ' ' + ' '.join(t for _, t in q['answers']))
    m = FIGREF.search(blob)
    return m.group(1) if m else None


def titlecase_group(name):
    """Group headings arrive SHOUTING and hyphen-wrapped; leave the words, tidy spacing."""
    return re.sub(r'\s+', ' ', name).strip().rstrip(';').strip()


def emit(name, qs, meta, out):
    keep = [q for q in qs if q['subelement'] in IN_SCOPE[name]]
    dropped = [q for q in qs if q['subelement'] not in IN_SCOPE[name]]
    sub_names = {q['subelement']: q['subelement_name'] for q in qs}
    counts = collections.Counter(q['subelement'] for q in qs)

    w = out.write
    w(f"# {meta['title']}\n\n")
    w(f"{meta['blurb']}\n\n")

    w('## Provenance\n\n')
    for k, v in meta['provenance']:
        w(f'- **{k}:** {v}\n')
    w('\n')
    w('Regenerate with `./scripts/build_pool_md.sh`. The extraction rules live in\n'
      '`scripts/parse_pool.py`, the scope and formatting rules in `scripts/emit_md.py`.\n'
      '**This file is derived data — do not hand-edit it; change the pipeline.**\n\n')

    w('## Scope\n\n')
    w(f'**{len(keep)} of {len(qs)}** questions are reproduced here: every question in\n'
      'the circuits, electronics, and calculation subelements. Whole subelements are\n'
      'kept or dropped — no question inside a kept subelement is filtered out, because a\n'
      'question missing from this file is a coverage gap we would never notice.\n\n')
    w('| Subelement | Questions | In this file |\n|---|---|---|\n')
    for s in sorted(counts):
        mark = '✅ all' if s in IN_SCOPE[name] else '—'
        w(f'| {s} — {sub_names[s]} | {counts[s]} | {mark} |\n')
    w(f'\nExcluded: {len(dropped)} questions on rules, operating procedure, propagation,\n'
      'and safety — the topics the book omits by design (see the preface).\n\n')

    calc = [q for q in keep if is_calc(q)]
    w(f'Of the {len(keep)} kept, **{len(calc)}** are calculation questions (every answer\n'
      'choice is numeric) and are tagged `[calc]` below.\n\n')

    figq = [(q['id'], figure_of(q)) for q in keep if figure_of(q)]
    if figq:
        figs = sorted({f for _, f in figq})
        w('## Questions that need a figure\n\n')
        w(f'**{len(figq)}** of the kept questions cannot be answered from text alone —\n'
          f'they refer to {len(figs)} schematic or plot ({", ".join(figs)}), which exist\n'
          'only in the source PDF. Treat these as unanswerable from this file:\n\n')
        for f in figs:
            ids = ', '.join(f'`{i}`' for i, ff in figq if ff == f)
            w(f'- **{f}** — {ids}\n')
        w('\n')

    w('## Questions absent from this export\n\n')
    w(meta['absent_intro'] + '\n\n')
    w('| ID | Status |\n|---|---|\n')
    for qid, status in meta['absent']:
        w(f'| `{qid}` | {status} |\n')
    w('\n---\n\n')

    cur_sub = cur_group = None
    for q in keep:
        if q['subelement'] != cur_sub:
            cur_sub = q['subelement']
            w(f"## Subelement {cur_sub} — {q['subelement_name']}\n\n")
            cur_group = None
        if q['group'] != cur_group:
            cur_group = q['group']
            w(f"### Group {cur_group} — {titlecase_group(q['group_name'])}\n\n")
        tag = ' `[calc]`' if is_calc(q) else ''
        w(f"#### {q['id']} — answer **{q['correct']}**{tag}\n\n")
        w(fix(q['stem']) + '\n\n')
        for letter, text in q['answers']:
            body = f'{letter}. {fix(text)}'
            w(f'- **{body}**\n' if letter == q['correct'] else f'- {body}\n')
        w('\n')
    return len(keep), len(qs), len(calc)


EXTRA_META = {
    'title': 'Extra (Element 4) Question Pool — Circuits and Calculations',
    'blurb': (
        'The circuit-theory and calculation questions of the Amateur Extra pool, in one\n'
        'greppable file, so coverage claims in this book can be checked without opening\n'
        'the source PDF. Answer letters are as published; the correct choice is **bold**.'
    ),
    'provenance': [
        ('Source', '`references/HamExam.org Extra Question Pool.pdf`, printed from '
                   'hamexam.org on 2026-07-28'),
        ('Cycle', 'Element 4, **2024–2028** — valid for exams through **2028-06-30** '
                  '(per the pool table on hamexam.org)'),
        ('Questions in the export', '599 in 50 groups'),
        ('Extracted', '2026-07-28, by `pdftotext -layout` plus `scripts/parse_pool.py`'),
    ],
    'absent_intro': (
        'The export has 599 questions. NCVEC has withdrawn questions mid-cycle, so the\n'
        'numbering has gaps. Every gap found by scanning each group for interior missing\n'
        'numbers is listed here, whether or not we can explain it. **A missing ID is not\n'
        'evidence the question never existed** — cite nothing from this table as a pool\n'
        'question.'
    ),
    'absent': [
        ('E2A13', 'Removed by NCVEC; HamExam removed it 2024-12-06. Last in its group, '
                  'so it leaves no interior gap.'),
        ('E4D05', 'Removed by NCVEC; HamExam removed it 2026-02-23. See the '
                  '[NCVEC pool release page](https://ncvec.org/index.php/2024-2028-extra-class-question-pool-release).'),
        ('E6D07', 'Removed by NCVEC 2025-10-15 — it "contained more than one correct '
                  'answer."'),
        ('E9E10', '**Unexplained.** Absent from the export but not in HamExam\'s change '
                  'log. Verify against NCVEC before assuming anything about it.'),
    ],
}

GENERAL_META = {
    'title': 'General (Element 3) Question Pool — Circuits and Calculations',
    'blurb': (
        'The circuit-theory and calculation questions of the General pool. This book\n'
        'never mentions the General exam, but it was written to be the circuits\n'
        'foundation a General licensee needs, so this file is the checklist for that\n'
        'claim. The correct choice is **bold**.'
    ),
    'provenance': [
        ('Source', '`references/HamExam.org General Question Pool.pdf`, printed from '
                   'hamexam.org on 2026-07-28'),
        ('Cycle', 'Element 3, **2023–2027** — valid for exams through **2027-06-30** '
                  '(per the pool table on hamexam.org; the PDF itself carries no cycle '
                  'dates, which previously caused us to doubt them)'),
        ('Questions in the export', '423 in 35 groups'),
        ('Extracted', '2026-07-28, by `pdftotext -layout` plus `scripts/parse_pool.py`'),
    ],
    'absent_intro': (
        'The export has 423 questions, with gaps where NCVEC withdrew questions\n'
        'mid-cycle. Every interior gap is listed, explained or not. Four are accounted\n'
        'for by HamExam\'s change log; four are not, and **must not be treated as\n'
        'settled** — an earlier round of work wrongly assumed the same absences were an\n'
        'extraction fault. They are not: the IDs appear nowhere in the PDF text.'
    ),
    'absent': [
        ('G1A04', 'Removed by NCVEC; HamExam removed it 2026-03-18. (Rules — outside '
                  'this file\'s scope anyway.)'),
        ('G1C08', '**Unexplained.**'),
        ('G1C09', 'Removed by NCVEC; HamExam removed it 2026-03-18.'),
        ('G1C10', '**Unexplained.**'),
        ('G1E09', 'Removed by NCVEC as of 2024-03-06.'),
        ('G6B09', '**Unexplained** — and in scope for this file. Verify against NCVEC.'),
        ('G8C01', 'Removed by NCVEC; HamExam removed it 2024-12-06.'),
        ('G9C06', '**Unexplained** — and in scope for this file. Verify against NCVEC.'),
    ],
}

if __name__ == '__main__':
    which = sys.argv[1]
    meta = EXTRA_META if which == 'extra' else GENERAL_META
    qs = json.load(open(sys.argv[2]))
    with open(sys.argv[3], 'w') as out:
        kept, total, calc = emit(which, qs, meta, out)
    print(f'{which}: {kept}/{total} kept, {calc} calculation questions')
