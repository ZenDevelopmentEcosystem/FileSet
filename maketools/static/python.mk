FLAKE8_ERROR := (echo "Run 'make format' to automatically solve most formatting problems" && exit 1)

PYDOCSTYLE_ARGS := --ignore=D1,D202,D203,D204,D212 --match '.*\.py' --match-dir='^((?!generated|syntaxerror).)*$$$$' --explain

YAPF_CHECK_ARGS := --parallel --diff --recursive
YAPF_ERROR := (echo "Run 'make format' to automatically solve formatting problems" && exit 1)

ISORT_CHECK_ARGS := --multi-line 2 --check-only --line-width 100
ISORT_ERROR := (echo "Run 'make format' to automatically sort includes" && exit 1)

static: static-python

.PHONY static-python: static-flake8
static-flake8: $(POETRY)
	$(Q)$(POETRY) run flake8 $(PYTHON_PACKAGES) || $(FLAKE8_ERROR)

.PHONY static-python: static-pydocstyle
static-pydocstyle: $(POETRY)
	$(Q)$(POETRY) run pydocstyle $(PYTHON_PACKAGES) $(PYDOCSTYLE_ARGS)

.PHONY static-python: static-yapf
static-yapf: $(POETRY)
	$(Q)$(POETRY) run yapf $(YAPF_CHECK_ARGS) $(PYTHON_PACKAGES) || $(YAPF_ERROR)

.PHONY static-python: static-isort
static-isort: $(POETRY)
	$(Q)$(POETRY) run isort $(ISORT_CHECK_ARGS) $(PYTHON_PACKAGES) || $(ISORT_ERROR)
