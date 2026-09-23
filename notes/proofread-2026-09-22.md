# Proofreading pass — 2026-09-22

Full-manuscript proofread of all 26 chapters, front matter and appendices, for
spelling, American English, and page/figure formatting. Run after the Round 7
revisions and the literature audit were pulled.

**Result: 231 pages, all checks passing.** Five classes of defect found and fixed;
one trade-off identified and deliberately *not* taken (see Open question OQ-5).

---

## Method

Spelling could not be checked against the `.tex` sources directly — LaTeX markup,
math, labels and TikZ bodies generate thousands of false positives. A stripper
(`prose.py`, reproduced at the end) removes comments, inline and display math,
non-prose environments (`tikzpicture`, `circuitikz`, tables, `verbatim`), and the
*arguments* of commands whose contents are not prose (`\label`, `\cref`, `\cite`,
`\includegraphics`, `\texttt`, `\SI`, …), then flattens the rest.

That reduced aspell's output from **434 distinct "misspellings" to a list containing
no actual misspelled words** — everything remaining was technical jargon (`passband`,
`phasor`, `megohms`, `transconductance`), proper nouns (`Butterworth`, `Yagi-Uda`,
`Litz`, `Friis`), or acronyms. Two independent scans backed this up: a
duplicated-word scan and a real-word-confusion scan (`principal`/`principle`,
`affect`/`effect`, `loose`/`lose`, `then`/`than`, …), both of which came back clean
on inspection.

**Caution for future passes:** aspell alone is nearly useless here. Three of my own
first-pass "findings" were artifacts of insufficient stripping or over-eager
regexes, and I only caught them by checking the source. Specifically: `pdftotext`
wraps "Figure" and "4.3" onto separate lines, so adjacency-based reference matching
under-reports; and excluding `Figure N.M:` to skip captions also excludes genuine
in-text references that happen to precede a colon.

---

## Fixed

### 1. American English — 28 replacements across 11 files

A pattern scan for `-ise`/`-isation`/`-yse` endings came back **clean**. Fixed-list
matching found the rest:

| Was | Now | Count |
|---|---|---|
| analogue | analog | 2 |
| neighbouring | neighboring | 1 |
| manoeuvre | maneuver | 2 |
| grey | gray | 1 |
| towards | toward | 1 |
| backwards | backward | 7 |
| afterwards | afterward | 3 |
| cancelled / cancelling | canceled / canceling | 9 |
| colour / coloured (preamble comments) | color / colored | 2 |

**`cancellation` was deliberately left alone** — it is the correct American spelling
in both dialects; only the `-ed`/`-ing` forms differ. The book had been mixed 1 US
to 9 UK on those.

### 2. A truncated sentence — Ch 9

The PEP worked example read:

> Same answer, as it must be. Note that the
> The average RF output over a voice transmission is…

"Note that the" is a fragment left behind by an earlier revision. Removed; the
following sentence was already complete. A scan for the same defect class (a line
ending in a dangling connective followed by a capitalized new sentence) found **no
other instances**.

### 3. An undisclosed symbol collision — Ch 1

The study guide discloses which letters do double duty. It listed two meanings for
β; Round 7's Ch 22 added a third. All three are live:

- feedback fraction — 43 uses in Ch 5
- transmission-line phase constant — 48 uses in Ch 16
- **FM modulation index — Ch 22** (was undisclosed)

The note now lists all three.

### 4. Hyphenation

Prose-only comparison of technical compounds found exactly one inconsistency:
`bandpass` in Ch 13 against `band-pass` everywhere else (9 uses). Fixed.
"single sideband" in Ch 17 is a *predicate noun* and correctly unhyphenated — left
alone. `lowpass`, `highpass`, `feedpoint`, `halfpower`, `selfresonance` all appeared
to be mixed but turned out to be **label names**, not prose.

### 5. Float placement — the largest formatting win

The book had **no float parameters set at all**, so LaTeX's defaults were in force.
Those defaults are tuned for text-heavy documents: a float page need only be half
full, and any page carrying a float must still be 20 % text. In a figure-dense book
that strands single half-page plots alone on a page with white bands above and
below. **Printed pages 28 and 29 were each one figure and nothing else.**

```latex
\renewcommand{\topfraction}{0.85}        % was 0.7
\renewcommand{\bottomfraction}{0.60}     % was 0.3
\renewcommand{\textfraction}{0.10}       % was 0.2
\renewcommand{\floatpagefraction}{0.80}  % was 0.5
\setcounter{topnumber}{3}\setcounter{bottomnumber}{2}\setcounter{totalnumber}{4}
```

| Metric | Before | After |
|---|---|---|
| Pages | 234 | **231** |
| Float-dominated pages | 8 | **7** |
| Worst case | one figure alone, white bands | two figures, page full |

Figure placement was then measured against the prose that discusses each figure:
**55 of 58 figures sit within one page of a mention.** The three at two pages
(2.1, 4.4, 16.6) are acceptable.

---

## Tested and deliberately reverted

Two further fixes for the remaining stranded figures were tried and backed out.
Both are recorded so nobody re-litigates them from scratch.

1. **Relaxing placement to `[!htb]`** on the five end-of-chapter worked-example
   figures: **no effect.** LaTeX floats only ever move *forward*, and these figures
   are declared *after* the text that would have held them, so no placement
   specifier can rescue them.
2. **Moving a figure earlier in the source** (tested on `fig:rlcpar-worked`, Ch 14):
   **this works** — the stranded page disappeared and the count went 7 → 6. But it
   puts a figure captioned with the worked example's component values *ahead of the
   section that introduces those values*. That is precisely the ordering defect this
   project fixed in Ch 13 in an earlier round, so the fix costs more than it buys.

---

## Open question

### OQ-5 — five end-of-chapter figure pages

**Status: open, low priority, needs Alex's call.**

Five worked-example figures close their chapters and land on pages of their own,
using roughly a third of the page: figures **9.4, 11.5, 12.3, 14.2, 16.7**. All
five are the last float in their chapter, so the chapter's `\clearpage` flushes them
out with no following text to share the page.

The three options, with their costs:

- **(a) Accept.** A figure on its own page at a chapter end is ordinary book
  typography. Costs nothing. *This is the current state and my recommendation.*
- **(b) Move each figure earlier in its chapter.** Recovers about five pages of
  whitespace, but breaks the convention that a worked example's numbers are
  introduced before any figure that depends on them — see "Tested and reverted"
  above.
- **(c) Shrink the five figures** so a figure plus the closing `exambox` fits one
  page. Costs legibility on plots that are already at a sensible size, and would
  make these five inconsistent with the other 53.

Nothing else in the manuscript depends on this decision.

---

## The prose stripper

Kept because any future spelling pass needs it. It lives in the session scratchpad,
not the repo, since it is a throwaway analysis tool:

```python
import re, sys
t = open(sys.argv[1]).read()
t = re.sub(r'(?<!\\)%.*', '', t)                                   # comments
t = re.sub(r'\\\[.*?\\\]', ' ', t, flags=re.S)                     # display math
t = re.sub(r'\\\(.*?\\\)', ' ', t, flags=re.S)                     # inline math
for env in ('tikzpicture','circuitikz','equation','align','longtable',
            'tabularx','tabular','verbatim','lstlisting','pgfplots','axis'):
    t = re.sub(r'\\begin\{%s\*?\}.*?\\end\{%s\*?\}' % (env, env), ' ', t, flags=re.S)
for cmd in ('label','cref','Cref','ref','cite','includegraphics','input','texttt',
            'url','href','si','SI','num','usepackage','color','node','draw'):
    t = re.sub(r'\\%s\*?(\[[^\]]*\])?\{[^{}]*\}' % cmd, ' ', t)
t = re.sub(r'\\[A-Za-z@]+\*?', ' ', t)
sys.stdout.write(t.replace('{',' ').replace('}',' '))
```
