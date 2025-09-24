# CPS published headline series -> clean CSV for Tableau
from pathlib import Path
import pandas as pd
from .bls_fetch import fetch_bls_series

SERIES = {
    "UnempRate_Total": "LNS14000000",
    "LFPR_Total":      "LNS11300000",
    "EmpPop_Total":    "LNS12300000",
    "UnempRate_20_24": "LNS14000036",
    "UnempRate_25_34": "LNS14000089",
}

def build(start_year=2015, end_year=2025):
    df = fetch_bls_series(SERIES.values(), start_year, end_year)
    df["metric"] = df.series_id.map({v:k for k,v in SERIES.items()})
    pivot = df.pivot(index="date", columns="metric", values="value").reset_index()
    return pivot

if __name__ == "__main__":
    out = build()
    Path("data_clean").mkdir(parents=True, exist_ok=True)
    out.to_csv("data_clean/cps_published.csv", index=False)
    print("Wrote data_clean/cps_published.csv")
