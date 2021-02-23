# The name of the main .tex file to build.
MANUSCRIPT = manuscript
# Folder where output will be placed
OUTDIR = _output
# Name of the output file
PDF = $(OUTDIR)/$(MANUSCRIPT).pdf

LATEX_COMPILER = latexmk
LATEX_FLAGS = -pdf -outdir=$(OUTDIR)
PDFVIEWER = xdg-open


all: preprint

preprint: $(PDF)

clean:
	rm -rf $(OUTDIR)

word-count:
	texcount -merge $(MANUSCRIPT).tex

show: preprint
	@( $(PDFVIEWER) $(PDF) 2> /dev/null; )

$(PDF): $(MANUSCRIPT).tex $(TEX_FILES) $(RESULTS)
	$(LATEX_COMPILER) $(LATEX_FLAGS) $<
