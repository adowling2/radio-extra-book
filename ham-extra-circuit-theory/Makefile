.PHONY: book cheat-sheet all clean

LATEXMK=latexmk
LATEXFLAGS=-pdf -interaction=nonstopmode -halt-on-error

book:
	$(LATEXMK) $(LATEXFLAGS) main.tex
	mkdir -p output
	cp main.pdf output/Circuit_Theory_for_the_Amateur_Extra_Exam.pdf

cheat-sheet:
	$(LATEXMK) $(LATEXFLAGS) cheat_sheet.tex
	mkdir -p output
	cp cheat_sheet.pdf output/Circuit_Theory_Cheat_Sheet.pdf

all: book cheat-sheet

clean:
	$(LATEXMK) -C main.tex cheat_sheet.tex
	rm -f *.bbl *.blg *.run.xml *.bcf
