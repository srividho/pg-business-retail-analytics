"""Analyse the synthetic FMCG dataset and compare flagged records."""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data/raw/fmcg/FMCG_2022_2024.csv"
OUTPUT_PATH = ROOT / "data/processed/fmcg_analyzed.csv"
FIGURES_DIR = ROOT / "reports/figures"

df = pd.read_csv(DATA_PATH)
df["date"] = pd.to_datetime(df["date"], errors="raise")

# Preserve every source record and flag suspicious quantities.
df["quality_flag"] = (
    (df["stock_available"] < 0)
    | (df["delivered_qty"] < 0)
    | (df["units_sold"] < 0)
)

# This is a revenue proxy, not verified accounting revenue.
df["revenue_proxy"] = df["price_unit"] * df["units_sold"]

# Derive monthly periods for trend analysis.
df["month"] = df["date"].dt.to_period("M").astype(str)

# Save an analysed copy; the raw CSV remains unchanged.
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_PATH, index=False)

# Compare results with and without flagged records.
valid = df.loc[~df["quality_flag"]].copy()

print("\n--- Dataset overview ---")
print(f"Rows: {len(df):,}")
print(f"Flagged rows: {int(df['quality_flag'].sum()):,}")
print(f"Date range: {df['date'].min().date()} to {df['date'].max().date()}")

print("\n--- Sensitivity to flagged records ---")
comparison = pd.DataFrame({
    "All records": [
        df["units_sold"].sum(),
        df["revenue_proxy"].sum(),
    ],
    "Excluding flagged records": [
        valid["units_sold"].sum(),
        valid["revenue_proxy"].sum(),
    ],
}, index=["Total units sold", "Revenue proxy"])

print(comparison.round(2).to_string())

print("\n--- Revenue proxy by category ---")
category_kpis = (
    valid.groupby("category")
    .agg(
        units_sold=("units_sold", "sum"),
        revenue_proxy=("revenue_proxy", "sum"),
        average_unit_price=("price_unit", "mean"),
    )
    .sort_values("revenue_proxy", ascending=False)
)

print(category_kpis.round(2).to_string())

print("\n--- Sales by channel ---")
channel_kpis = (
    valid.groupby("channel")
    .agg(
        units_sold=("units_sold", "sum"),
        revenue_proxy=("revenue_proxy", "sum"),
    )
    .sort_values("revenue_proxy", ascending=False)
)

print(channel_kpis.round(2).to_string())

print("\n--- Monthly revenue proxy ---")
monthly = (
    valid.groupby("month")["revenue_proxy"]
    .sum()
    .sort_index()
)

print(monthly.head(6).round(2).to_string())

# Plot monthly revenue proxy.
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

monthly_dates = pd.to_datetime(monthly.index)

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(monthly_dates, monthly.values, marker=".", markersize=4)
ax.set_title("Synthetic FMCG Monthly Revenue Proxy")
ax.set_xlabel("Month")
ax.set_ylabel("Revenue proxy (dataset currency units)")
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
ax.grid(True, alpha=0.3)
fig.autofmt_xdate()
fig.tight_layout()

FIGURES_DIR.mkdir(parents=True, exist_ok=True)
chart_path = FIGURES_DIR / "fmcg_monthly_revenue_proxy.png"
fig.savefig(chart_path, dpi=150, bbox_inches="tight")
plt.close(fig)

print(f"\nAnalysed data saved to: {OUTPUT_PATH}")
print(f"Chart saved to: {chart_path}")
print("Note: Dataset is synthetic; revenue is an unverified proxy.")
