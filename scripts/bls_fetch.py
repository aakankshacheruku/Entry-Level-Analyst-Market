"""
Pull JOLTS (Job Openings and Labor Turnover Survey) data from the BLS API
and save Job Openings and Hires series to a parquet file.

Series:
- JTS00000000JOL : Job Openings, Total Nonfarm
- JTS00000000HIL : Hires, Total Nonfarm
"""

import os
import time
import json
import pathlib
from datetime import datetime
import requests
import pandas as pd

BLS_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
SERIES = {
    "job_openings": ["JTS00000000JOL"],
    "hires": ["JTS00000000HIL"],
}

def fetch_series(series_ids, start_year="2015", end_year=None, api_key=None, pause=1.0):
    # Ensure API gets both startyear and endyear
    if end_year is None:
        end_year = str(datetime.utcnow().year)
    start_year = str(start_year)
    end_year = str(end_year)

    payload = {"seriesid": series_ids, "startyear": start_year, "endyear": end_year}
    if api_key:
        payload["registrationkey"] = api_key

    r = requests.post(BLS_URL, json=payload, timeout=30)
    r.raise_for_status()
    j = r.json()

    if j.get("status") != "REQUEST_SUCCEEDED":
        raise RuntimeError(f"BLS API failed. Payload={payload} Response={j}")

    rows = []
    for s in j.get("Results", {}).get("series", []):
        sid = s.get("seriesID", "UNKNOWN")
        for item in s.get("data", []):
            # monthly records have period like 'M01'...'M12'
            period = item.get("period", "")
            if not period.startswith("M"):
                continue
            try:
                rows.append({
                    "series_id": sid,
                    "year": int(item["year"]),
                    "month": int(period[1:]),
                    "period_name": item.get("periodName"),
                    "value": float(item["value"]),
                })
            except Exception as e:
                raise RuntimeError(f"Bad item for {sid}: {item}") from e

    # polite pause (BLS rate limits)
    time.sleep(pause)

    df = pd.DataFrame(rows)
    if df.empty:
        # give a precise, actionable error
        raise RuntimeError(
            "No monthly rows returned from BLS. "
            f"Check series_ids={series_ids}, start={start_year}, end={end_year}. "
            f"Raw response summary: status={j.get('status')}, message={j.get('message')}"
        )

    df["date"] = pd.to_datetime(df[["year", "month"]].assign(day=1)) + pd.offsets.MonthEnd(0)
    return df

def main():
    api_key = os.getenv("BLS_API_KEY")
    start = os.getenv("BLS_START", "2015")
    end = os.getenv("BLS_END")  # may be None; handled in fetch_series
    outdir = pathlib.Path("data_raw")
    outdir.mkdir(parents=True, exist_ok=True)

    frames = []
    for name, ids in SERIES.items():
        df = fetch_series(ids, start, end, api_key)
        df["metric"] = name
        frames.append(df)

    out = pd.concat(frames, ignore_index=True)
    stamp = datetime.utcnow().strftime("%Y-%m-%d")
    out_path = outdir / f"bls_jolts_{stamp}.parquet"
    out.to_parquet(out_path, index=False)
    print(f"Wrote {out_path} with {len(out)} rows across metrics={list(SERIES.keys())}.")

if __name__ == "__main__":
    main()
