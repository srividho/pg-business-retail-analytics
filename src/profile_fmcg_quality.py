"""Profile data quality issues in the synthetic FMCG dataset."""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data/raw/fmcg/FMCG_2022_2024.csv"

df = pd.read_csv(DATA_PATH)

# Parse dates and identify invalid date values
df["date"] = pd.to_datetime(df["date"], errors="coerce")

print("\n--- Date coverage ---")
print("Earliest date:", df["date"].min())
print("Latest date:", df["date"].max())
print("Invalid dates:", df["date"].isna().sum())

# Count suspicious values without modifying the original data
checks = {
    "Negative prices": df["price_unit"] < 0,
    "Negative stock": df["stock_available"] < 0,
    "Negative delivered quantity": df["delivered_qty"] < 0,
    "Negative units sold": df["units_sold"] < 0,
    "Negative delivery days": df["delivery_days"] < 0,
    "Invalid promotion flags": ~df["promotion_flag"].isin([0, 1]),
}

print("\n--- Suspicious-value counts ---")
for name, mask in checks.items():
    print(f"{name}: {int(mask.sum()):,}")

print("\n--- Numeric ranges ---")
numeric_cols = [
    "price_unit",
    "stock_available",
    "delivered_qty",
    "units_sold",
    "delivery_days",
]
print(df[numeric_cols].describe().round(2).to_string())

print("\n--- Negative-value examples ---")
for col in ["stock_available", "delivered_qty", "units_sold"]:
    examples = df.loc[df[col] < 0, [
        "date", "sku", "channel", "region", col
    ]].head(5)

    print(f"\n{col}:")
    if examples.empty:
        print("No negative values.")
    else:
        print(examples.to_string(index=False))

print("\n--- Categorical values ---")
for col in ["brand", "category", "channel", "region", "pack_type"]:
    print(f"{col}: {df[col].nunique()} unique values")
    print(df[col].value_counts().head(10).to_string())

print("\n--- Repeated date/product combinations ---")
key = ["date", "sku", "channel", "region", "pack_type"]
print("Rows sharing this combination:", int(df.duplicated(key).sum()))

print("\nProfiling complete. No source records were changed.")
