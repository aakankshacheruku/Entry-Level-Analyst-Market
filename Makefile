# ---------- Project Settings ----------
PYTHON ?= python3
VENV   ?= .venv
PIP    := $(VENV)/bin/pip
PY     := $(VENV)/bin/python

# Toggle dry-run fetch via: make fetch DRY_RUN=1
DRY_RUN ?= 0

# Data dirs (also created by config)
DATA_RAW := data_raw
DATA_CLEAN := data_clean
DATA_MART := data_mart

# ---------- Helpers ----------
.DEFAULT_GOAL := help

help: ## Show this help
	@grep -E '^[a-zA-Z0-9_\-]+:.*?## ' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "• %-18s %s\n", $$1, $$2}'

venv: ## Create virtualenv
	$(PYTHON) -m venv $(VENV) && \
	$(PY) -m pip install -U pip

deps: venv ## Install pinned dependencies (base required; extras best-effort)
	$(PIP) install -r requirements-base.txt
	-$(PIP) install --only-binary=:all: -r requirements-extras.txt || \
	  echo "[deps] Skipping extras (pyarrow/duckdb) due to wheel issues; pipeline can still run."

bootstrap: ## One-shot setup: venv + deps
	$(MAKE) venv && $(MAKE) deps

fetch: ## Run ETL fetch (real by default; set DRY_RUN=1 to smoke-test)
	@if [ -f scripts/bls_fetch.py ]; then \
		SCRIPT="scripts/bls_fetch.py"; \
	elif [ -f src/etl/bls_fetch.py ]; then \
		SCRIPT="src/etl/bls_fetch.py"; \
	else \
		echo "[fetch] ERROR: Could not find bls_fetch.py under scripts/ or src/etl/"; exit 1; \
	fi; \
	if [ "$(DRY_RUN)" = "1" ]; then \
		echo "[fetch] DRY RUN using $$SCRIPT"; \
		$(PY) $$SCRIPT --dry-run; \
	else \
		echo "[fetch] REAL RUN using $$SCRIPT"; \
		$(PY) $$SCRIPT; \
	fi

validate: ## Validate latest raw artifact (non-empty; optional schema check)
	$(PY) scripts/validate_output.py

clean: ## Remove build caches and data artifacts
	rm -rf $(VENV) .pytest_cache .mypy_cache __pycache__ **/__pycache__ \
	       $(DATA_CLEAN) $(DATA_MART)
	@echo "[clean] Keeping $(DATA_RAW) by default. Use 'make nuke' to delete all data."

nuke: clean ## Aggressive clean, including raw data
	rm -rf $(DATA_RAW)
	@echo "[nuke] Removed $(DATA_RAW) as well."
