# Regenerate all data-plot figures (Bode, root locus, pole-zero, transient,
# filter families). Circuit schematics are circuitikz in the LaTeX source and
# are NOT built here.
#
# Usage:
#   make          # regenerate every figure
#   make clean    # remove generated PDFs
#
# Requires: python3 with numpy, scipy, matplotlib.

# Prefer the first Python that has the declared figure dependencies.  Override
# with `make PY=/path/to/python` on a nonstandard installation.
PY ?= $(shell for p in python3 /opt/anaconda3/bin/python3; do \
	$$p -c 'import numpy, scipy, matplotlib' >/dev/null 2>&1 && { echo $$p; break; }; \
done)
MPLCONFIGDIR := /tmp/radio-extra-book-mpl
export MPLCONFIGDIR
SRC := $(wildcard src/*.py)
SCRIPTS := $(filter-out src/_style.py, $(SRC))
PDFS := $(patsubst src/%.py,%.pdf,$(SCRIPTS))
MANIFEST := manifest.json

.PHONY: all clean manifest audit
all: $(PDFS) manifest

%.pdf: src/%.py src/_style.py
	cd src && $(PY) $(notdir $<)

manifest: $(PDFS) ../scripts/generate_figure_manifest.py
	$(PY) ../scripts/generate_figure_manifest.py

audit: all ../scripts/audit_figures.py
	$(PY) ../scripts/audit_figures.py

clean:
	rm -f $(PDFS) $(MANIFEST)
	rm -rf provenance audit
