
VERSION := $(shell poetry version -s)
WHEEL := $(BUILD.dir)/fileset-$(VERSION)-py3-none-any.whl
SDIST := $(BUILD.dir)/fileset-$(VERSION).tar.gz
PYZ := $(BUILD.dir)/fileset.pyz

.PHONY: package

package: $(PYZ) $(WHEEL) $(SDIST) | $(BUILD.dir)

$(PYZ): $(PY_SRC)
	$(Q)$(POETRY) run shiv -e fileset.__main__:entrypoint -o $(abspath $(@)) .

$(WHEEL): $(PY_SRC)
	$(Q)$(POETRY) build -f wheel && mv dist/$(notdir $(@)) $(BUILD.dir)

$(SDIST): $(PY_SRC)
	$(Q)$(POETRY) build -f sdist && mv dist/$(notdir $(@)) $(BUILD.dir)
