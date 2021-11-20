YAPF_FORMAT_ARGS = --parallel --in-place --recursive
ISORT_FORMAT_ARGS = -j8 --multi-line 2 --line-width 100

format: format-python

.PHONY format-python: format-yapf
format-yapf: $(POETRY)
	$(Q)$(POETRY) run yapf $(YAPF_FORMAT_ARGS) $(PYTHON_PACKAGES)

.PHONY format-python: format-isort
format-isort: $(POETRY)
	$(Q)$(POETRY) run isort $(ISORT_FORMAT_ARGS) $(PYTHON_PACKAGES)
