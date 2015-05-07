.DEFAULT: all
.PHONY: clean

all: document.pdf

includes = $(shell sed -e 's/\\include{\(.*\)}/\1.tex/g;tx;d;:x' $(1))
inputs = $(shell sed -e 's/\\input{\(.*\)}/\1.tex/g;tx;d;:x' $(1))
bibliographies = $(shell sed -e 's/\\bibliography{\(.*\)}/\1.bib/g;tx;d;:x' $(1))

document.pdf: document.tex lieb.sty $(call includes,document.tex) $(call inputs,document.tex) $(call bibliographies,document.tex)

%.pdf: %.tex
	@echo Running PDF-Latex on "$*"...
	@pdflatex -quiet $*
	@bibtex -quiet $*
	@pdflatex -quiet $*
	@pdflatex -quiet $*

%.dvi: %.tex
	@echo Running Latex on "$*"...
	@latex -quiet $*
	@bibtex -quiet $*
	@latex -quiet $*
	@latex -quiet $*

%.ps: %.dvi
	@echo Converting "$*" to postscript...
	@dvips -q* -Ppdf -o $@ $*

#%.pdf: %.ps
#	@echo Converting "$<" to PDF...
#	@ps2pdf $< $@

clean:
	@echo Removing intermediate files...
	@rm -f *.ps *.dvi *.log *.aux *.blg *.bbl *.out

