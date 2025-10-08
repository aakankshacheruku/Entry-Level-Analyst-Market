.PHONY: venv deps fetch validate clean
# Detect which fetch script exists (src/etl/ preferred; fallback to scripts/)
FETCH_SCRIPT := $(shell if [ -f src/etl/bls_fetch.py ]; then echo src/etl/bls_fetch.py; elif [ -f scripts/bls_fetch.py ]; then echo scripts/bls_fetch.py; else echo ""; fi)
ve nv:
	/opt/homebrew/bin/python3 -m venv .venv && . .venv/bin/activate && python -m pip install -U pip
deps:
	. .venv/bin/activate && pip install -U pip && pip install pandas requests pyarrow duckdb
fetch:
	@if [ -z "$(FETCH_SCRIPT)" ]; then echo "No fetch script found (expected src/etl/bls_fetch.py or scripts/bls_fetch.py)"; exit 2; fi
	. .venv/bin/activate && python $(FETCH_SCRIPT) --dry-run
validate:
	. .venv/bin/activate && python scripts/validate_output.py
clean:
	rm -rf .venv __pycache__ */__pycache__
