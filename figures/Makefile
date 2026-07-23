# Regenerate all data-plot figures (Bode, root locus, pole-zero, transient,
# filter families). Circuit schematics are circuitikz in the LaTeX source and
# are NOT built here.
#
# Usage:
#   make          # regenerate every figure
#   make clean    # remove generated PDFs
#
# Requires: python3 with numpy, scipy, matplotlib.

PY := python3
SRC := $(wildcard src/*.py)
SCRIPTS := $(filter-out src/_style.py, $(SRC))
PDFS := $(patsubst src/%.py,%.pdf,$(SCRIPTS))

.PHONY: all clean
all: $(PDFS)

%.pdf: src/%.py src/_style.py
	cd src && $(PY) $(notdir $<)

clean:
	rm -f $(PDFS)
