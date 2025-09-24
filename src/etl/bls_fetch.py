# Fetch helper for BLS series (published timeseries)
import os, requests, pandas as pd

BLS_API = "https://api.bls.gov/publicAPI/v2/timeseries/data/"

def fetch_bls_series(series_ids, start_year=2015, end_year=2025, api_key=None):
    payload = {"seriesid": list(series_ids), "startyear": str(start_year), "endyear": str(end_year)}
    if api_key is None:
        api_key = os.getenv("BLS_API_KEY")
    if api_key:
        payload["registrationkey"] = api_key
    r = requests.post(BLS_API, json=payload, timeout=60)
    r.raise_for_status()
    js = r.json()
    if js.get("status") != "REQUEST_SUCCEEDED":
        raise RuntimeError(f"BLS API error: {js}")
    rows = []
    for s in js["Results"]["series"]:
        sid = s["seriesID"]
        for obs in s["data"]:
            if not obs["period"].startswith("M"):  # monthly only
                continue
            rows.append({
                "series_id": sid,
                "year": int(obs["year"]),
                "period": obs["period"],
                "value": float(obs["value"]),
            })
    df = pd.DataFrame(rows)
    df["month"] = df["period"].str[1:].astype(int)
    df["date"] = pd.to_datetime(df["year"].astype(str) + "-" + df["month"].astype(str) + "-01")
    return df[["date","series_id","value"]].sort_values("date")
