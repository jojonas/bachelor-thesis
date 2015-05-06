all: document.pdf

includes = $(shell sed -e 's/\\include{\(.*\)}/\1.tex/g;tx;d;:x' $(1))

document.dvi: document.tex $(call includes,document.tex)

%.dvi: %.tex
	@echo Latexing $< ...
	@latex -quiet $<
	
%.ps: %.dvi
	@echo Converting $< to postscript ...
	@dvips -q* -Ppdf $<
	
%.pdf: %.ps
	@echo Converting $< to PDF ...
	@ps2pdf $<
	
clean:
	@echo Removing intermediate files ...
	@rm -rf *.dvi *.ps *.log *.aux
	