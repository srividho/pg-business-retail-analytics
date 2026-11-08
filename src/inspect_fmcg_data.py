"""Inspect the downloaded FMCG dataset without modifying it."""

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data/raw/fmcg/FMCG_2022_2024.csv"

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATA_PATH}\n"
        "Download the CSV from the documented source first."
    )

df = pd.read_csv(DATA_PATH)

print("\n--- Dataset dimensions ---")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")

print("\n--- Column names ---")
print(df.columns.tolist())

print("\n--- First five rows ---")
print(df.head().to_string(index=False))

print("\n--- Data types ---")
print(df.dtypes.to_string())

print("\n--- Missing values ---")
print(df.isna().sum().to_string())

print("\n--- Duplicate rows ---")
print(df.duplicated().sum())

print("\n--- Numeric summary ---")
print(df.describe().round(2).to_string())
