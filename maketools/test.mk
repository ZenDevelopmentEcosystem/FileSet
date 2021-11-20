REPORTS.dir := $(BUILD.dir)/reports
DIRECTORIES += $(REPORTS.dir)

.PHONY check: test systest

test:
	$(Q)poetry run pytest tests/

systest: $(PYZ) $(WHEEL) $(SDIST) | $(REPORTS.dir)
	$(Q)poetry run pytest features --cucumber-json=$(REPORTS.dir)/cucumber.json --junit-xml=$(REPORTS.dir)/system-test-junit.xml --gherkin-terminal-reporter -vv -s
