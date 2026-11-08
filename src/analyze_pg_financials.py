"""Explore rounded P&G financial highlights for FY2022–FY2026."""

from pathlib import Path

import pandas as pd
from matplotlib.ticker import MaxNLocator

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "pg" / "pg_financial_highlights.csv"

df = pd.read_csv(DATA_PATH)

# Basic data-quality checks
assert df["fiscal_year"].is_unique, "Duplicate fiscal years found"
assert df.notna().all().all(), "Missing values found"
assert (df["net_sales_usd_bn"] > 0).all(), "Invalid net sales values"
assert (df["operating_income_usd_bn"] > 0).all(), "Invalid operating income values"

# Calculate analytical KPIs
df["net_sales_growth_pct"] = df["net_sales_usd_bn"].pct_change() * 100
df["operating_margin_pct"] = (
    df["operating_income_usd_bn"] / df["net_sales_usd_bn"] * 100
)

print("\nP&G Financial Highlights — FY2022–FY2026")
print(df.round(2).to_string(index=False))

sales_change = (
    df["net_sales_usd_bn"].iloc[-1] / df["net_sales_usd_bn"].iloc[0] - 1
) * 100

print(f"\nNet sales change from FY2022 to FY2026: {sales_change:.2f}%")
print("Note: Input financial figures are rounded headline values.")

import matplotlib.pyplot as plt

# Create a two-panel financial performance chart
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Net sales trend
axes[0].plot(
    df["fiscal_year"],
    df["net_sales_usd_bn"],
    marker="o",
)
axes[0].set_title("P&G Net Sales (FY2022–FY2026)")
axes[0].set_xlabel("Fiscal Year")
axes[0].set_ylabel("USD billions")
axes[0].grid(True, alpha=0.3)
axes[0].xaxis.set_major_locator(MaxNLocator(integer=True))

# Operating margin trend
axes[1].plot(
    df["fiscal_year"],
    df["operating_margin_pct"],
    marker="o",
)
axes[1].set_title("P&G Operating Margin")
axes[1].set_xlabel("Fiscal Year")
axes[1].set_ylabel("Operating margin (%)")
axes[1].grid(True, alpha=0.3)
axes[1].xaxis.set_major_locator(MaxNLocator(integer=True))

fig.suptitle("P&G Financial Performance — Public Data Case Study")
fig.tight_layout()

output_path = PROJECT_ROOT / "reports" / "figures" / "pg_financial_trends.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
plt.show()

print(f"\nChart saved to: {output_path}")
