"""Load P&G financial highlights into a local SQLite database."""

import sqlite3
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = PROJECT_ROOT / "data/raw/pg/pg_financial_highlights.csv"
DB_PATH = PROJECT_ROOT / "data/processed/pg_analytics.db"

df = pd.read_csv(CSV_PATH)

with sqlite3.connect(DB_PATH) as conn:
    df.to_sql("pg_financials", conn, if_exists="replace", index=False)

    result = pd.read_sql_query(
        "SELECT * FROM pg_financials ORDER BY fiscal_year",
        conn,
    )

print("Data loaded into SQLite successfully.")
print(result.to_string(index=False))
print(f"\nDatabase saved to: {DB_PATH}")
