import pandas as pd
import numpy as np
from openpyxl import load_workbook
import warnings
warnings.filterwarnings('ignore')

analysis_file = "Q2_Analysis.xlsx"

print("=" * 80)
print("VERIFICATION OF Q2_Analysis.xlsx")
print("=" * 80)

# Load workbook
wb = load_workbook(analysis_file)

def check_for_errors(ws, sheet_name):
    """Check for #N/A, #NAME?, #VALUE!, etc. errors"""
    errors_found = []
    for row_idx, row in enumerate(ws.iter_rows(min_row=1, max_row=100, values_only=True), start=1):
        for col_idx, cell_value in enumerate(row, start=1):
            if cell_value is not None:
                cell_str = str(cell_value)
                if '#N/A' in cell_str or '#NAME?' in cell_str or '#VALUE!' in cell_str or '#REF!' in cell_str or '#DIV/0!' in cell_str:
                    errors_found.append(f"  Row {row_idx}, Col {col_idx}: {cell_value}")
    return errors_found

# Check Calculations sheet
print("\n--- CALCULATIONS SHEET ---")
ws_calc = wb['Calculations']
errors = check_for_errors(ws_calc, 'Calculations')
if errors:
    print("❌ ERRORS FOUND:")
    for error in errors:
        print(error)
else:
    print("✓ No errors found")

# Display key values
print("\nKey Calculations:")
for row in ws_calc.iter_rows(min_row=1, max_row=100, values_only=True):
    if row[0] and any(keyword in str(row[0]) for keyword in ['Mean', 'Variance', 'Standard', 'Skewness', 'Kurtosis', 'Covariance', 'Correlation', 'Slope', 'Intercept', 'R-Square', 'Weeks moving']):
        print(f"  {row[0]}: {row[1] if len(row) > 1 else ''}, {row[2] if len(row) > 2 else ''}")

# Check Histograms sheet
print("\n--- HISTOGRAMS SHEET ---")
ws_hist = wb['Histograms']
errors = check_for_errors(ws_hist, 'Histograms')
if errors:
    print("❌ ERRORS FOUND:")
    for error in errors:
        print(error)
else:
    print("✓ No errors found")

# Check for missing frequencies (None or 0 where there should be values)
print("\nHistogram Frequencies Summary:")
freq_count_sp500 = 0
freq_count_aapl = 0
for row_idx, row in enumerate(ws_hist.iter_rows(min_row=1, max_row=100, values_only=True), start=1):
    if row[0] and 'S&P 500 RETURNS HISTOGRAM' in str(row[0]):
        # Count frequencies starting 2 rows below
        for i in range(2, 33):  # 31 bins
            freq = ws_hist.cell(row_idx + i, 2).value
            if freq is not None and freq != '':
                freq_count_sp500 += 1
        print(f"  S&P 500: {freq_count_sp500} frequencies populated")
        break

for row_idx, row in enumerate(ws_hist.iter_rows(min_row=1, max_row=100, values_only=True), start=1):
    if row[0] and 'AAPL RETURNS HISTOGRAM' in str(row[0]):
        # Count frequencies starting 2 rows below
        for i in range(2, 43):  # 41 bins
            freq = ws_hist.cell(row_idx + i, 2).value
            if freq is not None and freq != '':
                freq_count_aapl += 1
        print(f"  AAPL: {freq_count_aapl} frequencies populated")
        break

# Check Summary Results sheet
print("\n--- SUMMARY RESULTS SHEET ---")
ws_summary = wb['Summary Results']
errors = check_for_errors(ws_summary, 'Summary Results')
if errors:
    print("❌ ERRORS FOUND:")
    for error in errors:
        print(error)
else:
    print("✓ No errors found")

print("\nSummary Values:")
for row in ws_summary.iter_rows(min_row=1, max_row=50, values_only=True):
    if row[0] and any(keyword in str(row[0]) for keyword in ['Stock', 'Index', 'Frequency', 'Period', 'Observations', 'Mean', 'Variance', 'Standard', 'Skewness', 'Kurtosis', 'Covariance', 'Correlation', 'Beta', 'Alpha', 'R-Square', 'Weeks']):
        print(f"  {row[0]}: {row[1] if len(row) > 1 else ''}, {row[2] if len(row) > 2 else ''}")

# Check Data & Returns sheet
print("\n--- DATA & RETURNS SHEET ---")
ws_data = wb['Data & Returns']
errors = check_for_errors(ws_data, 'Data & Returns')
if errors:
    print("❌ ERRORS FOUND:")
    for error in errors[:10]:  # Show first 10 errors
        print(error)
    if len(errors) > 10:
        print(f"  ... and {len(errors) - 10} more errors")
else:
    print("✓ No errors found")

# Count how many returns were calculated
sp500_return_count = 0
aapl_return_count = 0
for row in ws_data.iter_rows(min_row=2, max_row=315, values_only=True):
    if row[3] is not None and row[3] != '':  # S&P 500 Log Return column
        sp500_return_count += 1
    if row[4] is not None and row[4] != '':  # AAPL Log Return column
        aapl_return_count += 1

print(f"\nLog Returns Calculated:")
print(f"  S&P 500: {sp500_return_count} returns")
print(f"  AAPL: {aapl_return_count} returns")

print("\n" + "=" * 80)
print("VERIFICATION COMPLETE")
print("=" * 80)
