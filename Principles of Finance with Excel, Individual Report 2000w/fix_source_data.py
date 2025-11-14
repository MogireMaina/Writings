"""
Step 1: Fix the source data by handling missing AAPL values
"""
import pandas as pd
import numpy as np

print("=" * 100)
print("STEP 1: FIXING SOURCE DATA - Handling Missing AAPL Values")
print("=" * 100)

# Load source data
df = pd.read_excel("Data Q2 & Q3.xlsx", sheet_name='Q2 (weekly)')

print(f"\nOriginal data shape: {df.shape}")
print(f"Missing AAPL values: {df['AAPL'].isnull().sum()}")

# Show where the missing values are
print("\nRows with missing AAPL values:")
missing_aapl = df[df['AAPL'].isnull()]
print(missing_aapl[['Date', 'S&P_500 index', 'AAPL']])

# Option 1: Forward fill (use previous week's value)
print("\n" + "─" * 100)
print("OPTION 1: Forward Fill (recommended for time series)")
print("─" * 100)
df_filled = df.copy()
df_filled['AAPL'] = df_filled['AAPL'].fillna(method='ffill')
print(f"Missing values after forward fill: {df_filled['AAPL'].isnull().sum()}")

# Option 2: Linear interpolation (smooth missing values)
print("\n" + "─" * 100)
print("OPTION 2: Linear Interpolation")
print("─" * 100)
df_interpolated = df.copy()
df_interpolated['AAPL'] = df_interpolated['AAPL'].interpolate(method='linear')
print(f"Missing values after interpolation: {df_interpolated['AAPL'].isnull().sum()}")

# Option 3: Drop rows with missing AAPL (reduces dataset size)
print("\n" + "─" * 100)
print("OPTION 3: Drop Missing Rows (not recommended - loses data)")
print("─" * 100)
df_dropped = df.dropna(subset=['AAPL'])
print(f"Rows remaining: {len(df_dropped)} (lost {len(df) - len(df_dropped)} rows)")

# RECOMMENDATION: Use forward fill
print("\n" + "=" * 100)
print("RECOMMENDATION: Using Forward Fill Method")
print("=" * 100)
df_clean = df.copy()
df_clean['AAPL'] = df_clean['AAPL'].fillna(method='ffill')

# If there are still any NaN at the beginning, use backward fill
if df_clean['AAPL'].isnull().sum() > 0:
    df_clean['AAPL'] = df_clean['AAPL'].fillna(method='bfill')

print(f"✓ Final missing values: {df_clean['AAPL'].isnull().sum()}")
print(f"✓ Dataset shape: {df_clean.shape}")

# Save the cleaned data
output_file = "Data Q2 & Q3_CLEAN.xlsx"
with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df_clean.to_excel(writer, sheet_name='Q2 (weekly)', index=False)

print(f"\n✓ Clean data saved to: {output_file}")
print("\nNext steps:")
print("  1. Review the cleaned data")
print("  2. Run the create_excel_with_formulas.py script with the clean data")
print("  3. Or manually replace missing values in Excel using =IF(ISBLANK())")
