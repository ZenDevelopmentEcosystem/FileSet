TRIVY_CACHE_DIR := $(PWD)/.trivycache
TRIVY_VERSION := "0.20.1"
TRIVY_COMMAND := MSYS_NO_PATHCONV=1 docker run --rm --user $$(id -u):$$(id -g) -e TRIVY_CACHE_DIR=/cache -v $(TRIVY_CACHE_DIR):/cache -v $(PWD):/project:ro aquasec/trivy:$(TRIVY_VERSION)
DIRECTORIES += $(TRIVY_CACHE_DIR)

.PHONY check: scan

scan: $(POETRY) | $(TRIVY_CACHE_DIR)
	$(Q)$(TRIVY_COMMAND) fs --ignorefile /project/.trivyignore --skip-dirs="/project/Web.Frontend/node_modules" /project
