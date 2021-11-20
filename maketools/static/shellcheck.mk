SHELLCHECK.bin := ${BIN.dir}/shellcheck.sh
SHELLCHECK.args := -x --source-path=SCRIPTDIR
SHELLCHECK.cmd := $(SHELLCHECK.bin) $(SHELLCHECK.args)


.PHONY static: static-shellcheck
static-shellcheck:
	$(Q)cd "$(ROOT.dir)" \
		&& find "$(ROOT.dir)" \
			-type f \
			-name '*.sh'| xargs --no-run-if-empty -L1 $(SHELLCHECK.cmd)
