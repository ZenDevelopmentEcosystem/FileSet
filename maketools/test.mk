REPORTS.dir := $(BUILD.dir)/reports
DIRECTORIES += $(REPORTS.dir)

UNITTEST.testargs := --junit-xml=$(REPORTS.dir)/test-report-junit.xml
UNITTEST.covargs := --cov-report html:$(REPORTS.dir)/cov-html --cov-report xml:$(REPORTS.dir)/coverage-report.xml --cov=fileset --cov-report term-missing
UNITTEST.dir := tests

.PHONY check: test systest

test: export UNIT_TEST_MODE := True
test:
	$(Q)poetry run pytest $(UNITTEST.dir) $(UNITTEST.testargs) $(UNITTEST.covargs)

systest: $(PYZ) $(WHEEL) $(SDIST) | $(REPORTS.dir)
	$(Q)poetry run pytest features \
		--fileset-path "$(realpath $(PYZ))" \
		--wheel-package-path "$(realpath $(WHEEL))" \
		--sdist-package-path "$(realpath $(SDIST))" \
		--cucumber-json=$(REPORTS.dir)/cucumber.json \
		--junit-xml=$(REPORTS.dir)/system-test-report-junit.xml \
		--gherkin-terminal-reporter \
		-vv -s
