Q := @
IGNORE_ERROR := -
SHELL := /bin/bash
.SHELLFLAGS := -e -o pipefail -c
COLOR := y
SPACE :=
SPACE +=
COMMA := ,

PYTHON := python3
POETRY := $(HOME)/.local/bin/poetry
MD := $(shell which mdp || which less)
PYTHON_PACKAGES := fileset tests features
PY_SRC := $(shell find fileset -type f -name '*.py')

.PHONY: .FORCE

ROOT.dir := $(abspath $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))/..)
MAKETOOLS.dir := $(ROOT.dir)/maketools
BUILD.dir := $(ROOT.dir)/build
BIN.dir := $(ROOT.dir)/bin
SCRIPT.dir := $(ROOT.dir)/scripts
TOOLS.dir :=$(ROOT.dir)/.tools
DIRECTORIES += $(BUILD.dir) $(TOOLS.dir)

MAKETOOLS.files := $(shell find "$(MAKETOOLS.dir)" -type f -name '*.mk' -not -path '*init.mk' | sort)
include $(MAKETOOLS.files)

# Create directories
# after inclusion of other mk-files, so that newly added directories are included
$(DIRECTORIES):
	$(Q)mkdir -p '$@'

# Explicit rules for certain files to prevent implicit rule invokation.
Makefile: ;
%.mk: ;
