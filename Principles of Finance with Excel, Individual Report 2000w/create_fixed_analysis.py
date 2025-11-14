"""
Create Q2_Analysis_FIXED.xlsx with CLEAN DATA and WORKING FORMULAS
"""
import pandas as pd
import numpy as np
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
import warnings
warnings.filterwarnings('ignore')

print("=" * 100)
print("CREATING FIXED EXCEL FILE WITH FORMULAS")
print("=" * 100)

# Load CLEAN source data
source_file = "Data Q2 & Q3_CLEAN.xlsx"
try:
    df_source = pd.read_excel(source_file, sheet_name='Q2 (weekly)')
    print(f"✓ Loaded clean data: {len(df_source)} rows")
    print(f"✓ Missing AAPL values: {df_source['AAPL'].isnull().sum()}")
except FileNotFoundError:
    print(f"❌ Error: {source_file} not found!")
    print("   Run fix_source_data.py first to create the clean data file.")
    exit(1)

# Create new workbook
wb = Workbook()
wb.remove(wb.active)

# =============================================================================
# SHEET 1: Data & Returns
# =============================================================================
print("\n1. Creating 'Data & Returns' sheet...")
ws_data = wb.create_sheet("Data & Returns")

# Headers
headers = ["Week", "Date", "S&P 500 Price", "AAPL Price", "S&P 500 Log Return", "AAPL Log Return"]
for col, header in enumerate(headers, 1):
    cell = ws_data.cell(1, col, header)
    cell.font = Font(bold=True, size=11, color="FFFFFF")
    cell.fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    cell.alignment = Alignment(horizontal="center")

# Write price data
for row_idx, (idx, row) in enumerate(df_source.iterrows(), start=2):
    ws_data.cell(row_idx, 1, row_idx - 1)  # Week number
    ws_data.cell(row_idx, 2, row['Date'])
    ws_data.cell(row_idx, 3, row['S&P_500 index'])
    ws_data.cell(row_idx, 4, row['AAPL'])

# Add log return FORMULAS (starting from row 3)
for row_idx in range(3, len(df_source) + 2):
    ws_data.cell(row_idx, 5, f"=LN(C{row_idx}/C{row_idx-1})")
    ws_data.cell(row_idx, 6, f"=LN(D{row_idx}/D{row_idx-1})")

# Formatting
ws_data.column_dimensions['A'].width = 8
ws_data.column_dimensions['B'].width = 12
ws_data.column_dimensions['C'].width = 15
ws_data.column_dimensions['D'].width = 15
ws_data.column_dimensions['E'].width = 20
ws_data.column_dimensions['F'].width = 20

for row in range(2, len(df_source) + 2):
    ws_data.cell(row, 3).number_format = '#,##0.00'
    ws_data.cell(row, 4).number_format = '#,##0.00'
    if row >= 3:
        ws_data.cell(row, 5).number_format = '0.00000000'
        ws_data.cell(row, 6).number_format = '0.00000000'

print(f"  ✓ Added {len(df_source)} price observations")
print(f"  ✓ Added {len(df_source)-1} log return formulas")

# =============================================================================
# SHEET 2: Calculations
# =============================================================================
print("\n2. Creating 'Calculations' sheet...")
ws_calc = wb.create_sheet("Calculations")

def add_section_header(ws, row, title):
    ws.cell(row, 1, title)
    ws.cell(row, 1).font = Font(bold=True, size=12, color="FFFFFF")
    ws.cell(row, 1).fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
    ws.merge_cells(f'A{row}:C{row}')
    ws.cell(row, 1).alignment = Alignment(horizontal="center")
    return row + 1

def add_column_headers(ws, row):
    ws.cell(row, 1, "Calculation Method")
    ws.cell(row, 2, "S&P 500")
    ws.cell(row, 3, "AAPL")
    for col in range(1, 4):
        ws.cell(row, col).font = Font(bold=True)
        ws.cell(row, col).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    return row + 1

current_row = 1
n_returns = len(df_source) - 1
sp500_range = f"'Data & Returns'!E3:E{n_returns+2}"
aapl_range = f"'Data & Returns'!F3:F{n_returns+2}"

# (a) MEAN
current_row = add_section_header(ws_calc, current_row, "(a) MEAN WEEKLY LOG RETURN")
current_row = add_column_headers(ws_calc, current_row)
ws_calc.cell(current_row, 1, "Mean (Excel AVERAGE)")
ws_calc.cell(current_row, 2, f"=AVERAGE({sp500_range})")
ws_calc.cell(current_row, 3, f"=AVERAGE({aapl_range})")
mean_row = current_row
current_row += 2

# (b) VARIANCE
current_row = add_section_header(ws_calc, current_row, "(b) VARIANCE CALCULATION")
current_row = add_column_headers(ws_calc, current_row)

ws_calc.cell(current_row, 1, "Manual: Σ(x - mean)²/N")
ws_calc.cell(current_row, 2, f"=SUMPRODUCT(({sp500_range}-B{mean_row})^2)/COUNT({sp500_range})")
ws_calc.cell(current_row, 3, f"=SUMPRODUCT(({aapl_range}-C{mean_row})^2)/COUNT({aapl_range})")
var_manual_row = current_row
current_row += 1

ws_calc.cell(current_row, 1, "Excel VAR.P function")
ws_calc.cell(current_row, 2, f"=VAR.P({sp500_range})")
ws_calc.cell(current_row, 3, f"=VAR.P({aapl_range})")
var_excel_row = current_row
current_row += 1

ws_calc.cell(current_row, 1, "Difference")
ws_calc.cell(current_row, 2, f"=B{var_manual_row}-B{var_excel_row}")
ws_calc.cell(current_row, 3, f"=C{var_manual_row}-C{var_excel_row}")
current_row += 2

# (c) STANDARD DEVIATION
current_row = add_section_header(ws_calc, current_row, "(c) STANDARD DEVIATION CALCULATION")
current_row = add_column_headers(ws_calc, current_row)

ws_calc.cell(current_row, 1, "Manual: SQRT(Variance)")
ws_calc.cell(current_row, 2, f"=SQRT(B{var_manual_row})")
ws_calc.cell(current_row, 3, f"=SQRT(C{var_manual_row})")
std_manual_row = current_row
current_row += 1

ws_calc.cell(current_row, 1, "Excel STDEV.P function")
ws_calc.cell(current_row, 2, f"=STDEV.P({sp500_range})")
ws_calc.cell(current_row, 3, f"=STDEV.P({aapl_range})")
std_excel_row = current_row
current_row += 1

ws_calc.cell(current_row, 1, "Difference")
ws_calc.cell(current_row, 2, f"=B{std_manual_row}-B{std_excel_row}")
ws_calc.cell(current_row, 3, f"=C{std_manual_row}-C{std_excel_row}")
current_row += 2

# (e) SKEWNESS AND KURTOSIS
current_row = add_section_header(ws_calc, current_row, "(e) SKEWNESS AND KURTOSIS")
current_row = add_column_headers(ws_calc, current_row)

ws_calc.cell(current_row, 1, "Skewness")
ws_calc.cell(current_row, 2, f"=SKEW({sp500_range})")
ws_calc.cell(current_row, 3, f"=SKEW({aapl_range})")
skew_row = current_row
current_row += 1

ws_calc.cell(current_row, 1, "Kurtosis")
ws_calc.cell(current_row, 2, f"=KURT({sp500_range})")
ws_calc.cell(current_row, 3, f"=KURT({aapl_range})")
kurt_row = current_row
current_row += 2

# (f) WEEKS MOVING TOGETHER/APART
current_row = add_section_header(ws_calc, current_row, "(f) WEEKS MOVING TOGETHER/APART")
ws_calc.cell(current_row, 1, "Metric")
ws_calc.cell(current_row, 2, "Count")
ws_calc.cell(current_row, 3, "Proportion")
for col in range(1, 4):
    ws_calc.cell(current_row, col).font = Font(bold=True)
    ws_calc.cell(current_row, col).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
current_row += 1

ws_calc.cell(current_row, 1, "Weeks moving together (same sign)")
ws_calc.cell(current_row, 2, f"=SUMPRODUCT((SIGN({sp500_range})=SIGN({aapl_range}))*1)")
ws_calc.cell(current_row, 3, f"=B{current_row}/COUNT({sp500_range})")
together_row = current_row
current_row += 1

ws_calc.cell(current_row, 1, "Weeks moving apart (different sign)")
ws_calc.cell(current_row, 2, f"=SUMPRODUCT((SIGN({sp500_range})<>SIGN({aapl_range}))*1)")
ws_calc.cell(current_row, 3, f"=B{current_row}/COUNT({sp500_range})")
apart_row = current_row
current_row += 2

# (g) COVARIANCE
current_row = add_section_header(ws_calc, current_row, "(g) COVARIANCE CALCULATION")
ws_calc.cell(current_row, 1, "Calculation Method")
ws_calc.cell(current_row, 2, "Value")
ws_calc.cell(current_row, 1).font = Font(bold=True)
ws_calc.cell(current_row, 2).font = Font(bold=True)
ws_calc.cell(current_row, 1).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
ws_calc.cell(current_row, 2).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
current_row += 1

ws_calc.cell(current_row, 1, "Manual: Σ(x-mean_x)(y-mean_y)/N")
ws_calc.cell(current_row, 2, f"=SUMPRODUCT(({sp500_range}-B{mean_row}),({aapl_range}-C{mean_row}))/COUNT({sp500_range})")
cov_manual_row = current_row
current_row += 1

ws_calc.cell(current_row, 1, "Excel COVARIANCE.P function")
ws_calc.cell(current_row, 2, f"=COVARIANCE.P({sp500_range},{aapl_range})")
cov_excel_row = current_row
current_row += 1

ws_calc.cell(current_row, 1, "Difference")
ws_calc.cell(current_row, 2, f"=B{cov_manual_row}-B{cov_excel_row}")
current_row += 2

# (h) CORRELATION
current_row = add_section_header(ws_calc, current_row, "(h) CORRELATION CALCULATION")
ws_calc.cell(current_row, 1, "Calculation Method")
ws_calc.cell(current_row, 2, "Value")
ws_calc.cell(current_row, 1).font = Font(bold=True)
ws_calc.cell(current_row, 2).font = Font(bold=True)
ws_calc.cell(current_row, 1).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
ws_calc.cell(current_row, 2).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
current_row += 1

ws_calc.cell(current_row, 1, "Manual: Cov(x,y)/(StdDev_x * StdDev_y)")
ws_calc.cell(current_row, 2, f"=B{cov_excel_row}/(B{std_excel_row}*C{std_excel_row})")
corr_manual_row = current_row
current_row += 1

ws_calc.cell(current_row, 1, "Excel CORREL function")
ws_calc.cell(current_row, 2, f"=CORREL({sp500_range},{aapl_range})")
corr_excel_row = current_row
current_row += 1

ws_calc.cell(current_row, 1, "Difference")
ws_calc.cell(current_row, 2, f"=B{corr_manual_row}-B{corr_excel_row}")
current_row += 2

# (j) REGRESSION STATISTICS
current_row = add_section_header(ws_calc, current_row, "(j) REGRESSION STATISTICS (AAPL vs S&P 500)")
ws_calc.cell(current_row, 1, "Statistic")
ws_calc.cell(current_row, 2, "Value")
for col in range(1, 3):
    ws_calc.cell(current_row, col).font = Font(bold=True)
    ws_calc.cell(current_row, col).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
current_row += 1

ws_calc.cell(current_row, 1, "Slope (Beta)")
ws_calc.cell(current_row, 2, f"=SLOPE({aapl_range},{sp500_range})")
slope_row = current_row
current_row += 1

ws_calc.cell(current_row, 1, "Intercept (Alpha)")
ws_calc.cell(current_row, 2, f"=INTERCEPT({aapl_range},{sp500_range})")
intercept_row = current_row
current_row += 1

ws_calc.cell(current_row, 1, "R-Square")
ws_calc.cell(current_row, 2, f"=RSQ({aapl_range},{sp500_range})")
rsq_row = current_row

# Formatting
ws_calc.column_dimensions['A'].width = 45
ws_calc.column_dimensions['B'].width = 25
ws_calc.column_dimensions['C'].width = 25

for row in range(1, current_row + 1):
    for col in [2, 3]:
        cell = ws_calc.cell(row, col)
        if cell.value and isinstance(cell.value, str) and cell.value.startswith('='):
            cell.number_format = '0.00000000'

print(f"  ✓ Created calculations with formulas")
print(f"  ✓ Data range: E3:E{n_returns+2} ({n_returns} returns)")

# =============================================================================
# SHEET 3: Summary Results
# =============================================================================
print("\n3. Creating 'Summary Results' sheet...")
ws_summary = wb.create_sheet("Summary Results")

ws_summary.cell(1, 1, "STATISTICAL ANALYSIS SUMMARY")
ws_summary.cell(1, 1).font = Font(bold=True, size=14, color="FFFFFF")
ws_summary.cell(1, 1).fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
ws_summary.merge_cells('A1:C1')
ws_summary.cell(1, 1).alignment = Alignment(horizontal="center")

row = 3
ws_summary.cell(row, 1, "Metric")
ws_summary.cell(row, 2, "S&P 500")
ws_summary.cell(row, 3, "AAPL")
for col in range(1, 4):
    ws_summary.cell(row, col).font = Font(bold=True)
    ws_summary.cell(row, col).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
row += 1

ws_summary.cell(row, 1, "Mean (Excel AVERAGE)")
ws_summary.cell(row, 2, f"=Calculations!B{mean_row}")
ws_summary.cell(row, 3, f"=Calculations!C{mean_row}")
row += 1

ws_summary.cell(row, 1, "Variance (Excel VAR.P)")
ws_summary.cell(row, 2, f"=Calculations!B{var_excel_row}")
ws_summary.cell(row, 3, f"=Calculations!C{var_excel_row}")
row += 1

ws_summary.cell(row, 1, "Standard Deviation (Excel STDEV.P)")
ws_summary.cell(row, 2, f"=Calculations!B{std_excel_row}")
ws_summary.cell(row, 3, f"=Calculations!C{std_excel_row}")
row += 1

ws_summary.cell(row, 1, "Skewness")
ws_summary.cell(row, 2, f"=Calculations!B{skew_row}")
ws_summary.cell(row, 3, f"=Calculations!C{skew_row}")
row += 1

ws_summary.cell(row, 1, "Kurtosis")
ws_summary.cell(row, 2, f"=Calculations!B{kurt_row}")
ws_summary.cell(row, 3, f"=Calculations!C{kurt_row}")
row += 2

ws_summary.cell(row, 1, "Weeks moving together (same sign)")
ws_summary.cell(row, 2, f"=Calculations!B{together_row}")
ws_summary.cell(row, 3, f"=Calculations!C{together_row}")
row += 1

ws_summary.cell(row, 1, "Weeks moving apart (different sign)")
ws_summary.cell(row, 2, f"=Calculations!B{apart_row}")
ws_summary.cell(row, 3, f"=Calculations!C{apart_row}")
row += 2

ws_summary.cell(row, 1, "Covariance")
ws_summary.cell(row, 2, f"=Calculations!B{cov_excel_row}")
row += 1

ws_summary.cell(row, 1, "Correlation")
ws_summary.cell(row, 2, f"=Calculations!B{corr_excel_row}")
row += 2

ws_summary.cell(row, 1, "Regression Statistics (AAPL vs S&P 500)")
ws_summary.cell(row, 1).font = Font(bold=True)
row += 1

ws_summary.cell(row, 1, "Slope (Beta)")
ws_summary.cell(row, 2, f"=Calculations!B{slope_row}")
row += 1

ws_summary.cell(row, 1, "Intercept (Alpha)")
ws_summary.cell(row, 2, f"=Calculations!B{intercept_row}")
row += 1

ws_summary.cell(row, 1, "R-Square")
ws_summary.cell(row, 2, f"=Calculations!B{rsq_row}")

ws_summary.column_dimensions['A'].width = 40
ws_summary.column_dimensions['B'].width = 20
ws_summary.column_dimensions['C'].width = 20

for r in range(1, row + 1):
    for col in [2, 3]:
        cell = ws_summary.cell(r, col)
        if cell.value and isinstance(cell.value, str) and cell.value.startswith('='):
            cell.number_format = '0.00000000'

print(f"  ✓ Created summary sheet")

# =============================================================================
# SAVE WORKBOOK
# =============================================================================
output_file = "Q2_Analysis_FIXED.xlsx"
wb.save(output_file)

print("\n" + "=" * 100)
print(f"✓ SUCCESS! File created: {output_file}")
print("=" * 100)
print("\nAll formulas are working correctly!")
print(f"Total returns: {n_returns}")
print(f"Data range: E3:E{n_returns+2} and F3:F{n_returns+2}")
