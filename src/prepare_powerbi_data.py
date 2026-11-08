"""Prepare a Power BI-friendly FMCG dataset."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/raw/fmcg/FMCG_2022_2024.csv"
OUTPUT = ROOT / "data/processed/fmcg_powerbi.csv"

df = pd.read_csv(SOURCE, parse_dates=["date"])

# Flag the three known rows with negative stock or quantity values.
df["quality_flag"] = (
    (df["stock_available"] < 0)
    | (df["delivered_qty"] < 0)
    | (df["units_sold"] < 0)
)

# Descriptive revenue proxy only; not verified financial revenue.
df["revenue_proxy"] = df["price_unit"] * df["units_sold"]
df["promotion_status"] = df["promotion_flag"].map(
    {0: "No promotion", 1: "Promotion"}
)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT, index=False)

print(f"Rows exported: {len(df):,}")
print(f"Flagged rows: {df['quality_flag'].sum()}")
print(f"Output: {OUTPUT}")
print("Revenue proxy is not actual P&G revenue.")
