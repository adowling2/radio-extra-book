.PHONY: book cheat-sheet all figures audit-diff clean

LATEXMK=latexmk
LATEXFLAGS=-pdf -interaction=nonstopmode -halt-on-error

# Regenerate the Python-generated data plots (Bode, root locus, pole-zero,
# transient, filter families). Committed PDFs mean the LaTeX build does not
# require Python; run this only after editing a figure script.
figures:
	$(MAKE) -C figures

book:
	$(LATEXMK) $(LATEXFLAGS) main.tex
	mkdir -p output
	cp main.pdf output/Circuit_Theory_for_the_Amateur_Extra_Exam.pdf

cheat-sheet:
	$(LATEXMK) $(LATEXFLAGS) cheat_sheet.tex
	mkdir -p output
	cp cheat_sheet.pdf output/Circuit_Theory_Cheat_Sheet.pdf

all: book cheat-sheet

# Rebuild the review copy for the 2026 literature audit.  The two immutable
# revisions keep later documentation edits out of the manuscript diff.
audit-diff:
	./scripts/build_latexdiff.sh 4f4100a 660dda4 \
		output/pdf/literature-audit-latexdiff.pdf

clean:
	$(LATEXMK) -C main.tex cheat_sheet.tex
	rm -f *.bbl *.blg *.run.xml *.bcf
