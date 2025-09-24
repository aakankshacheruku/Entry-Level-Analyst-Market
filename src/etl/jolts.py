# JOLTS headline series -> clean CSV for Tableau
from pathlib import Path
import pandas as pd
from .bls_fetch import fetch_bls_series

SERIES = {
    "JOLTS_Openings": "JTSJOL",
    "JOLTS_Hires": "JTSHIR",
    "JOLTS_QuitsRate": "JTSQUR",
    "JOLTS_LayoffsRate": "JTSLDR",
}

def build(start_year=2015, end_year=2025):
    df = fetch_bls_series(SERIES.values(), start_year, end_year)
    df["metric"] = df.series_id.map({v:k for k,v in SERIES.items()})
    pivot = df.pivot(index="date", columns="metric", values="value").reset_index()
    return pivot

if __name__ == "__main__":
    out = build()
    Path("data_clean").mkdir(parents=True, exist_ok=True)
    out.to_csv("data_clean/jolts_US.csv", index=False)
    print("Wrote data_clean/jolts_US.csv")
