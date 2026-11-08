"""Compare promotion-associated differences across categories and channels."""

import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data/processed/pg_analytics.db"
OUTPUT_PATH = ROOT / "reports/figures/promotion_difference_by_channel.png"

query = """
SELECT
    category,
    channel,
    promotion_flag,
    AVG(units_sold) AS avg_units
FROM fmcg_retail
WHERE quality_flag = 0
GROUP BY category, channel, promotion_flag
"""

with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql_query(query, conn)

pivot = df.pivot(
    index=["category", "channel"],
    columns="promotion_flag",
    values="avg_units",
)

pivot["difference_pct"] = (pivot[1] - pivot[0]) / pivot[0] * 100
plot_data = pivot["difference_pct"].sort_values()
plot_data.index = [f"{category} — {channel}" for category, channel in plot_data.index]

fig, ax = plt.subplots(figsize=(10, 7))
plot_data.plot(kind="barh", ax=ax)

ax.set_title("Observed Difference in Average Units by Promotion Status")
ax.set_xlabel("Difference in average units (%)")
ax.set_ylabel("Category and channel")
ax.axvline(0, linewidth=1)
ax.grid(axis="x", alpha=0.25)

fig.text(
    0.01, 0.01,
    "Synthetic dataset. Descriptive comparison, not causal evidence.",
    fontsize=9,
)
fig.tight_layout(rect=(0, 0.04, 1, 1))

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT_PATH, dpi=150, bbox_inches="tight")
plt.close(fig)

print(plot_data.round(2).to_string())
print(f"\nChart saved to: {OUTPUT_PATH}")
