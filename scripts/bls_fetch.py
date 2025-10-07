import os, time, pathlib
from datetime import datetime
import requests, pandas as pd

BLS_URL = "https://api.bls.gov/publicAPI/v2/timeseries/data/"
SERIES = {
    "job_openings": ["JTS000000000000000JOL"],  # JT + S + total nonfarm + US + all areas + all sizes + JO + L
    "hires":        ["JTS000000000000000HIL"],  # JT + S + total nonfarm + US + all areas + all sizes + HI + L
}

def fetch_series(series_ids, start_year="2015", end_year=None, api_key=None, pause=1.0):
    if end_year is None:
        end_year = str(datetime.utcnow().year)
    payload = {"seriesid": series_ids, "startyear": str(start_year), "endyear": str(end_year)}
    if api_key:
        payload["registrationkey"] = api_key
    r = requests.post(BLS_URL, json=payload, timeout=30); r.raise_for_status()
    j = r.json()
    if j.get("status") != "REQUEST_SUCCEEDED":
        raise RuntimeError(f"BLS API failed. Payload={payload} Response={j}")
    rows = []
    for s in j.get("Results", {}).get("series", []):
        sid = s.get("seriesID", "UNKNOWN")
        for item in s.get("data", []):
            p = item.get("period","")
            if not p.startswith("M"): continue
            rows.append({
                "series_id": sid,
                "year": int(item["year"]),
                "month": int(p[1:]),
                "period_name": item.get("periodName"),
                "value": float(item["value"]),
            })
    time.sleep(pause)
    df = pd.DataFrame(rows)
    if df.empty:
        raise RuntimeError(f"No monthly rows returned. series_ids={series_ids}, start={start_year}, end={end_year}, message={j.get('message')}")
    df["date"] = pd.to_datetime(df[["year","month"]].assign(day=1)) + pd.offsets.MonthEnd(0)
    return df

def main():
    api_key = os.getenv("BLS_API_KEY")
    start = os.getenv("BLS_START", "2015")
    end = os.getenv("BLS_END")  # may be None
    outdir = pathlib.Path("data_raw"); outdir.mkdir(parents=True, exist_ok=True)
    frames = []
    for name, ids in SERIES.items():
        df = fetch_series(ids, start, end, api_key); df["metric"] = name; frames.append(df)
    out = pd.concat(frames, ignore_index=True)
    out_path = outdir / f"bls_jolts_{datetime.utcnow().strftime('%Y-%m-%d')}.parquet"
    out.to_parquet(out_path, index=False)
    print(f"Wrote {out_path} with {len(out)} rows.")
if __name__ == "__main__":
    main()
