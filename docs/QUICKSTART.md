# Quickstart

## Prerequisites
- Python 3.10+ available as `python3`
- macOS/Linux (Windows WSL is fine)

## One-time setup
make bootstrap     # creates .venv and installs requirements

## Run the pipeline (Day 3)
make fetch         # real run; writes to data_raw/*.parquet
make validate      # checks latest parquet is readable & non-empty

### Optional: dry-run fetch
make fetch DRY_RUN=1

### Optional: schema check (warn-only today)
EXPECTED_COLS="series_id,date,value" make validate
