"""Visualise average units by category and promotion status."""

import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data/processed/pg_analytics.db"
OUTPUT_PATH = ROOT / "reports/figures/fmcg_promotion_comparison.png"

query = """
SELECT
    category,
    promotion_flag,
    AVG(units_sold) AS avg_units
FROM fmcg_retail
WHERE quality_flag = 0
GROUP BY category, promotion_flag
ORDER BY category, promotion_flag
"""

with sqlite3.connect(DB_PATH) as conn:
    df = pd.read_sql_query(query, conn)

pivot = df.pivot(
    index="category",
    columns="promotion_flag",
    values="avg_units",
).rename(columns={0: "No promotion", 1: "Promotion"})

pivot = pivot.sort_values("Promotion", ascending=True)

positions = np.arange(len(pivot))
bar_height = 0.36

fig, ax = plt.subplots(figsize=(10, 6))

ax.barh(
    positions - bar_height / 2,
    pivot["No promotion"],
    bar_height,
    label="No promotion",
)
ax.barh(
    positions + bar_height / 2,
    pivot["Promotion"],
    bar_height,
    label="Promotion",
)

ax.set_yticks(positions)
ax.set_yticklabels(pivot.index)
ax.set_xlabel("Average units sold per record")
ax.set_title("Average Units by Category and Promotion Status")
ax.legend()
ax.grid(axis="x", alpha=0.25)

fig.text(
    0.01,
    0.01,
    "Synthetic dataset. Descriptive comparison, not causal evidence.",
    fontsize=9,
)
fig.tight_layout(rect=(0, 0.04, 1, 1))

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT_PATH, dpi=150, bbox_inches="tight")
plt.close(fig)

print(pivot.round(2).to_string())
print(f"\nChart saved to: {OUTPUT_PATH}")
