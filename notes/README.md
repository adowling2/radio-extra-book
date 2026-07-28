# Working notes from the Round 4 audits

These are the **full-reasoning working notes** behind the two summary documents in the
repository root. They were produced in a session scratchpad, which does not survive, so
they are preserved here — `PROJECT-STATUS.md` and `ARRL-GAP-PROPOSAL.md` both cite
them.

| File | What it is |
|---|---|
| `audit-general-pool.md` | Complete concept inventory of the **General (Element 3)** pool: 423 questions, 35 groups, the 236 that are circuit/electronics questions, distilled to a 157-concept checklist with question IDs. This is what the book was checked against. |
| `audit-arrl-ch4.md` | ARRL Extra manual Ch 4 (radio mathematics, principles of circuits) — 9 proposals |
| `audit-arrl-ch6.md` | ARRL Ch 6 (amplifiers, signal processing, DSP, filters, power supplies) — 12 proposals |
| `audit-arrl-ch7.md` | ARRL Ch 7 (test equipment, receiver performance, interference) — 12 proposals |
| `audit-arrl-ch9.md` | ARRL Ch 9 (antennas, transmission lines) — 12 proposals |

**Start from the LEDGER at the end of `ARRL-GAP-PROPOSAL.md`, not from these files.**
The ledger reconciles every proposal against the book as built and ranks what is left;
these notes are the detail you drop into once you have picked an item.

## Two caveats these notes carry

1. **The ARRL manual audited is the 12th edition, keyed to the 2020–2024 pool**, while
   the book targets 2024–2028. Any exam-relevance claim in these files sourced from the
   manual is suspect until checked against the real pool. One claim (power factor) was
   materially wrong and one citation (E7H14/E7H15) pointed at questions that do not
   exist. Every other cited ID was verified.
2. **The PLL proposal in `audit-arrl-ch6.md` contains an error.** It states that a
   type-1 loop has zero steady-state phase error for a frequency step. It does not — a
   frequency step leaves a constant error `Δω/K`. `sec:pll` in the book states it
   correctly.

## Copyright

These are **concept inventories and analysis**, not reproductions. They paraphrase what
each source asserts in order to argue about what the book should derive. They contain no
verbatim question text, no answer choices, no figures, and no extended prose — only
occasional five-to-nine-word fragments identifying a claim being discussed. The source
PDFs themselves live in `references/`, which is **gitignored** and must not be
committed.
