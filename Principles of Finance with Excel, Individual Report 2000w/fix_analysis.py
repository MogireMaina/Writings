import pandas as pd
import numpy as np
from openpyxl import load_workbook
import warnings
warnings.filterwarnings('ignore')

# Load the data file
data_file = "Data Q2 & Q3.xlsx"
analysis_file = "Q2_Analysis.xlsx"

print("=" * 80)
print("EXAMINING DATA FILE")
print("=" * 80)

# Read the data file to see its structure
xl_data = pd.ExcelFile(data_file)
print(f"\nSheets in {data_file}:")
for sheet in xl_data.sheet_names:
    print(f"  - {sheet}")

# Read each sheet
for sheet in xl_data.sheet_names:
    print(f"\n--- Sheet: {sheet} ---")
    df = pd.read_excel(data_file, sheet_name=sheet, nrows=10)
    print(f"Shape: {df.shape}")
    print(f"Columns: {df.columns.tolist()}")
    print(df.head())

print("\n" + "=" * 80)
print("EXAMINING ANALYSIS FILE")
print("=" * 80)

# Read the analysis file
xl_analysis = pd.ExcelFile(analysis_file)
print(f"\nSheets in {analysis_file}:")
for sheet in xl_analysis.sheet_names:
    print(f"  - {sheet}")

# Read each sheet
for sheet in xl_analysis.sheet_names:
    print(f"\n--- Sheet: {sheet} ---")
    df = pd.read_excel(analysis_file, sheet_name=sheet, nrows=20)
    print(f"Shape: {df.shape}")
    print(df.head(20))
