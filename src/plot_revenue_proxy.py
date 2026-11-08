
"""Plot revenue proxy by FMCG category and channel."""

import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data/processed/pg_analytics.db"
OUTPUT_PATH = ROOT / "reports/figures/revenue_proxy_by_category_channel.png"

query = """
SELECT
    category,
    channel,
    SUM(price_unit * units_sold) AS revenue_proxy
FROM fmcg_retail
WHERE quality_flag = 0
GROUP BY category, channel
"""

with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql_query(query, conn)

pivot = df.pivot(
    index="category",
    columns="channel",
    values="revenue_proxy",
)

pivot = pivot.sort_values("Retail", ascending=True)

ax = pivot.plot(kind="barh", figsize=(10, 6), width=0.75)

ax.set_title("Revenue Proxy by Category and Sales Channel")
ax.set_xlabel("Revenue proxy (dataset units)")
ax.set_ylabel("Product category")
ax.legend(title="Sales channel")
ax.grid(axis="x", alpha=0.25)

plt.figtext(
    0.01,
    0.01,
    "Synthetic dataset. Revenue proxy = price_unit × units_sold.",
    fontsize=9,
)
plt.tight_layout(rect=(0, 0.04, 1, 1))

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUTPUT_PATH, dpi=150, bbox_inches="tight")
plt.close()

print(pivot.round(2).to_string())
print(f"\nChart saved to: {OUTPUT_PATH}")

