"""
Lightweight QA for latest raw export.
 - Ensures at least one parquet exists in data_raw/
 - Reads the newest file and checks basic schema assumptions
 - Exits non-zero on failure (useful for CI and pre-commit)
"""
import sys, glob, pandas as pd

def fail(msg: str, code: int = 1) -> None:
    print(f"[validate_output] FAIL: {msg}", file=sys.stderr)
    sys.exit(code)

fps = sorted(glob.glob("data_raw/*.parquet"))
if not fps:
    fail("No parquet files found under data_raw/")

fp = fps[-1]
try:
    df = pd.read_parquet(fp)
except Exception as e:
    fail(f"Could not read parquet {fp}: {e}")

if df.empty:
    fail(f"Dataframe is empty: {fp}")

# Minimal expected columns; adjust to your actual schema
expected = {"series_id", "date", "value"}
missing = expected - set(df.columns)
if missing:
    fail(f"Missing expected columns: {sorted(missing)} in {fp}")

print(f"[validate_output] OK: {fp} rows={len(df)} cols={len(df.columns)}")
sys.exit(0)
