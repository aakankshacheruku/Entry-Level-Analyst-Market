from pathlib import Path
import os

# Centralized data locations (created on import)
ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data_raw"
DATA_CLEAN = ROOT / "data_clean"
DATA_MART = ROOT / "data_mart"

for p in (DATA_RAW, DATA_CLEAN, DATA_MART):
    p.mkdir(parents=True, exist_ok=True)

APP_ENV = os.getenv("APP_ENV", "dev")
