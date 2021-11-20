REPORTS.dir := $(BUILD.dir)/reports
DIRECTORIES += $(REPORTS.dir)

.PHONY check: test systest

test:
	$(Q)poetry run pytest tests/ --junit-xml=$(REPORTS.dir)/test-report-junit.xml

systest: $(PYZ) $(WHEEL) $(SDIST) | $(REPORTS.dir)
	$(Q)poetry run pytest features \
		--fileset-path "$(realpath $(PYZ))" \
		--cucumber-json=$(REPORTS.dir)/cucumber.json \
		--junit-xml=$(REPORTS.dir)/system-test-report-junit.xml \
		--gherkin-terminal-reporter \
		-vv -s
