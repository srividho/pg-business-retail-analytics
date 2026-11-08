"""Load the analysed synthetic FMCG data into SQLite."""

import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data/processed/fmcg_analyzed.csv"
DB_PATH = ROOT / "data/processed/pg_analytics.db"

df = pd.read_csv(CSV_PATH)
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

with sqlite3.connect(DB_PATH) as conn:
    df.to_sql(
        "fmcg_retail",
        conn,
        if_exists="replace",
        index=False,
    )

    count = pd.read_sql_query(
        "SELECT COUNT(*) AS row_count FROM fmcg_retail",
        conn,
    ).iloc[0]["row_count"]

print(f"Loaded {count:,} records into fmcg_retail.")
print(f"Database: {DB_PATH}")
