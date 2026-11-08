"""Validate the P&G financial dataset and SQLite table."""

import sqlite3
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data/raw/pg/pg_financial_highlights.csv"
DB_PATH = ROOT / "data/processed/pg_analytics.db"

df = pd.read_csv(CSV_PATH)

# 1. Check required columns
required = {
    "fiscal_year",
    "net_sales_usd_bn",
    "operating_income_usd_bn",
}
assert required.issubset(df.columns), "Required columns are missing"

# 2. Check completeness and duplicates
assert not df[list(required)].isna().any().any(), "Missing values found"
assert df["fiscal_year"].is_unique, "Duplicate fiscal years found"

# 3. Check fiscal-year coverage
assert df["fiscal_year"].tolist() == [2022, 2023, 2024, 2025, 2026], (
    "Unexpected fiscal-year coverage"
)

# 4. Check numeric validity
assert (df["net_sales_usd_bn"] > 0).all(), "Invalid net sales"
assert (df["operating_income_usd_bn"] > 0).all(), (
    "Invalid operating income"
)
assert (
    df["operating_income_usd_bn"] <= df["net_sales_usd_bn"]
).all(), "Operating income exceeds net sales"

# 5. Compare CSV and SQLite records
with sqlite3.connect(DB_PATH) as conn:
    db_df = pd.read_sql_query(
        "SELECT fiscal_year, net_sales_usd_bn, operating_income_usd_bn "
        "FROM pg_financials ORDER BY fiscal_year",
        conn,
    )

expected = df.sort_values("fiscal_year").reset_index(drop=True)
actual = db_df.reset_index(drop=True)

pd.testing.assert_frame_equal(expected, actual, check_dtype=False)

print("PASS: Required columns are present")
print("PASS: No missing values or duplicate fiscal years")
print("PASS: Fiscal years and numeric values are valid")
print("PASS: CSV and SQLite records match")
print("\nAll data-quality checks passed.")
