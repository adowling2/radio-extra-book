"""Parse a HamExam.org 'view pool' PDF text dump into structured questions."""
import re
import sys
import json

QID = re.compile(r'^([EG]\d[A-Z]\d\d)\s*\(([A-D])\)\s*$')
ANS = re.compile(r'^([A-D])\.\s+(.*)$')
SUBEL = re.compile(r'^Subelement\s+([EG]\d)\s*-\s*(.*)$')
GROUP = re.compile(r'^GROUP\s+([EG]\d[A-Z])\s*-\s*-?\s*(.*)$')

JUNK = (
    'HamExam.org:', 'https://hamexam.org', 'Only show correct answers',
    'Show question numbers', 'Highlight correct answers', 'View Question Pool',
    'Element 3: General', 'Element 4: Extra',
)


def clean(path):
    """Yield (indent, text) for every meaningful line, page furniture removed."""
    out = []
    for raw in open(path):
        line = raw.rstrip('\n')
        text = line.strip()
        if not text:
            continue
        if any(j in text for j in JUNK):
            continue
        if re.match(r'^Page \d+ of \d+$', text):
            continue
        out.append((len(line) - len(line.lstrip()), text))
    return out


def parse(path):
    lines = clean(path)
    questions = []
    subel = subel_name = group = group_name = None
    pending_group = None          # group title still accumulating wrapped lines
    q = None
    state = None                  # 'stem' | 'answers'

    def flush():
        if q is not None:
            q['stem'] = ' '.join(q['stem']).strip()
            q['answers'] = [(l, ' '.join(t).strip()) for l, t in q['answers']]
            questions.append(q)

    for indent, text in lines:
        m = SUBEL.match(text)
        if m:
            flush()
            q, state = None, None
            subel, subel_name = m.group(1), m.group(2).strip()
            pending_group = None
            continue

        m = GROUP.match(text)
        if m:
            flush()
            q, state = None, None
            group, group_name = m.group(1), m.group(2).strip()
            pending_group = True
            continue

        m = QID.match(text)
        if m:
            flush()
            pending_group = None
            q = {'id': m.group(1), 'correct': m.group(2), 'subelement': subel,
                 'subelement_name': subel_name, 'group': group,
                 'group_name': group_name, 'stem': [], 'answers': []}
            state = 'stem'
            continue

        if pending_group:
            # Group headings wrap across lines; keep appending until the first Qxxx.
            group_name = (group_name + ' ' + text).strip()
            continue

        if q is None:
            continue

        m = ANS.match(text)
        if m:
            state = 'answers'
            q['answers'].append((m.group(1), [m.group(2)]))
            continue

        if state == 'stem':
            q['stem'].append(text)
        elif state == 'answers' and q['answers']:
            q['answers'][-1][1].append(text)   # wrapped answer text

    flush()
    return questions


if __name__ == '__main__':
    qs = parse(sys.argv[1])
    print(f'{len(qs)} questions', file=sys.stderr)
    bad = [x for x in qs if len(x['answers']) != 4 or not x['stem']]
    if bad:
        print(f'MALFORMED: {[x["id"] for x in bad]}', file=sys.stderr)
    ids = [x['id'] for x in qs]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        print(f'DUPLICATES: {sorted(dupes)}', file=sys.stderr)
    json.dump(qs, open(sys.argv[2], 'w'), indent=1)
