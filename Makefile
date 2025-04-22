# Rules for compiling the PDF from the LaTeX sources and displaying the output

# Variables
###############################################################################
### Git tags for different revisions
SUBMITTED = submitted-gji
### Documents to build
PDF = paper/preprint.pdf paper/manuscript.pdf paper/cover-letter.pdf
### File Types (for dependencies)
TEX = $(filter-out $(PDF:.pdf=.tex), $(wildcard paper/*.tex))
TEXVARS = $(wildcard paper/variables/*.tex)
BIB = $(wildcard paper/*.bib)
FIG = $(wildcard paper/figures/*)
# For word counting, how many words does the journal consider for each figure
WORDS_PER_FIGURE = 300


# Main targets
###############################################################################
preprint: paper/preprint.pdf

manuscript: paper/manuscript.pdf

# Use this to make a version with marked changes after the first reviews
diff-submitted: paper/manuscript-diff-$(SUBMITTED).pdf

letter: paper/cover-letter.pdf

all: $(PDF)

clean:
	rm -rf $(PDF) paper/manuscript-diff-*.tex paper/_diff

format:
	black code/

# The lock file specifies all packages installed at their exact versions. This
# can be used to completely replicate the environment on another computer. See
# REPRODUCING.md
lock: conda-lock.yml

wordcount:
	@echo -n "Paper: "
	@echo $$((`detex paper/content.tex | wc --words` + `detex paper/abstract.tex | wc --words` + $(WORDS_PER_FIGURE) * `ls paper/figures/*.png | wc --lines`))
	@echo -n "Abstract: "
	@echo $$((`detex paper/abstract.tex | wc --words`))


# Rules for building PDFs
###############################################################################
%.pdf: %.tex $(TEX) $(BIB) $(FIG)
	tectonic -X compile $<

paper/manuscript-diff-$(SUBMITTED).tex: paper/manuscript.tex $(TEX) $(BIB) $(FIG)
	cd paper \
		&& latexdiff-vc --git --flatten --force --dir=_diff --rev $(SUBMITTED) `basename $<` \
		&& cd .. \
		&& mv paper/_diff/*.tex $@

paper/misc/cover-letter.pdf: paper/misc/cover-letter.tex paper/information.tex
	tectonic -X compile $<

paper/variables.tex: $(TEXVARS)
	cat $^ > $@

# Rules for generating results and other files
###############################################################################
conda-lock.yml: environment.yml
	conda-lock -f $<
