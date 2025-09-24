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
        raise RuntimeError(f"BLS API error: {js.get('message')} :: {js}")

    rows = []
    for s in js.get("Results", {}).get("series", []):
        sid = s.get("seriesID")
        for obs in s.get("data", []):
            p = obs.get("period", "")
            if not p.startswith("M"):   # monthly only
                continue
            rows.append({
                "series_id": sid,
                "year": int(obs["year"]),
                "period": p,
                "value": float(obs["value"]),
            })

    if not rows:
        raise RuntimeError(f"No monthly observations returned for {series_ids}. "
                           f"Check series IDs, date range, or add BLS_API_KEY.")

    df = pd.DataFrame(rows)
    if "period" not in df.columns:
        raise RuntimeError(f"Unexpected payload shape: missing 'period' key. Sample: {js}")

    df["month"] = df["period"].str[1:].astype(int)
    df["date"] = pd.to_datetime(df["year"].astype(str) + "-" + df["month"].astype(str) + "-01")
    return df[["date","series_id","value"]].sort_values("date")
