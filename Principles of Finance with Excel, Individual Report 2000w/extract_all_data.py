"""
Extract all calculated values from the Excel file for report writing
"""

import pandas as pd
import numpy as np
from openpyxl import load_workbook

# Load the Excel file with formulas
excel_file = "Q2_Analysis_WithFormulas.xlsx"
wb = load_workbook(excel_file, data_only=True)  # data_only=True to get calculated values

print("=" * 80)
print("QUESTION 2 ANALYSIS - ALL DATA FOR REPORT")
print("=" * 80)

# Read Summary Results sheet
ws_summary = wb['Summary Results']

print("\n" + "=" * 80)
print("DATASET INFORMATION")
print("=" * 80)

# Extract dataset info
for row in ws_summary.iter_rows(min_row=4, max_row=9, values_only=True):
    if row[0] and row[1]:
        print(f"{row[0]} {row[1]}")

# Read Calculations sheet for detailed values
ws_calc = wb['Calculations']

print("\n" + "=" * 80)
print("(a) MEAN WEEKLY LOG RETURN")
print("=" * 80)

# Find mean row
for row in ws_calc.iter_rows(values_only=False):
    if row[0].value and 'Excel AVERAGE' in str(row[0].value):
        sp500_mean = row[1].value
        aapl_mean = row[2].value
        print(f"S&P 500: {sp500_mean:.10f} ({sp500_mean*100:.4f}%)")
        print(f"AAPL: {aapl_mean:.10f} ({aapl_mean*100:.4f}%)")
        print(f"\nAnnualized (multiply by 52):")
        print(f"S&P 500: {sp500_mean*52*100:.2f}% per year")
        print(f"AAPL: {aapl_mean*52*100:.2f}% per year")
        break

print("\n" + "=" * 80)
print("(b) VARIANCE")
print("=" * 80)

sp500_var_manual = None
aapl_var_manual = None
sp500_var_excel = None
aapl_var_excel = None

for idx, row in enumerate(ws_calc.iter_rows(values_only=False), 1):
    cell_val = str(row[0].value) if row[0].value else ""

    if 'Manual:' in cell_val and 'mean' in cell_val.lower() and 'variance' in str(ws_calc.cell(idx-1, 1).value or "").lower():
        sp500_var_manual = row[1].value
        aapl_var_manual = row[2].value
    elif 'VAR.P' in cell_val:
        sp500_var_excel = row[1].value
        aapl_var_excel = row[2].value

if sp500_var_manual and sp500_var_excel:
    print("S&P 500:")
    print(f"  Manual calculation: {sp500_var_manual:.10f}")
    print(f"  Excel VAR.P:        {sp500_var_excel:.10f}")
    print(f"  Difference:         {abs(sp500_var_manual - sp500_var_excel):.15f}")
    print(f"\nAAPL:")
    print(f"  Manual calculation: {aapl_var_manual:.10f}")
    print(f"  Excel VAR.P:        {aapl_var_excel:.10f}")
    print(f"  Difference:         {abs(aapl_var_manual - aapl_var_excel):.15f}")
    print(f"\nRatio: AAPL variance is {aapl_var_manual/sp500_var_manual:.2f}x higher than S&P 500")

print("\n" + "=" * 80)
print("(c) STANDARD DEVIATION")
print("=" * 80)

sp500_std_manual = None
aapl_std_manual = None
sp500_std_excel = None
aapl_std_excel = None

for idx, row in enumerate(ws_calc.iter_rows(values_only=False), 1):
    cell_val = str(row[0].value) if row[0].value else ""

    if 'SQRT' in cell_val and 'Variance' in cell_val:
        sp500_std_manual = row[1].value
        aapl_std_manual = row[2].value
    elif 'STDEV.P' in cell_val:
        sp500_std_excel = row[1].value
        aapl_std_excel = row[2].value

if sp500_std_manual and sp500_std_excel:
    print("S&P 500:")
    print(f"  Manual (SQRT):      {sp500_std_manual:.10f} ({sp500_std_manual*100:.4f}%)")
    print(f"  Excel STDEV.P:      {sp500_std_excel:.10f} ({sp500_std_excel*100:.4f}%)")
    print(f"  Difference:         {abs(sp500_std_manual - sp500_std_excel):.15f}")
    print(f"  Annualized (×√52):  {sp500_std_manual*np.sqrt(52)*100:.2f}%")
    print(f"\nAAPL:")
    print(f"  Manual (SQRT):      {aapl_std_manual:.10f} ({aapl_std_manual*100:.4f}%)")
    print(f"  Excel STDEV.P:      {aapl_std_excel:.10f} ({aapl_std_excel*100:.4f}%)")
    print(f"  Difference:         {abs(aapl_std_manual - aapl_std_excel):.15f}")
    print(f"  Annualized (×√52):  {aapl_std_manual*np.sqrt(52)*100:.2f}%")
    print(f"\nRatio: AAPL volatility is {aapl_std_manual/sp500_std_manual:.2f}x higher than S&P 500")

print("\n" + "=" * 80)
print("(e) SKEWNESS AND KURTOSIS")
print("=" * 80)

sp500_skew = None
aapl_skew = None
sp500_kurt = None
aapl_kurt = None

for row in ws_calc.iter_rows(values_only=False):
    cell_val = str(row[0].value) if row[0].value else ""

    if cell_val == "Skewness (Excel SKEW)" or (cell_val == "Skewness" and row[1].value is not None):
        sp500_skew = row[1].value
        aapl_skew = row[2].value
    elif cell_val == "Kurtosis (Excel KURT)" or (cell_val == "Kurtosis" and row[1].value is not None):
        sp500_kurt = row[1].value
        aapl_kurt = row[2].value

if sp500_skew is not None:
    print("S&P 500:")
    print(f"  Skewness:  {sp500_skew:.6f}", end="")
    if sp500_skew < -0.5:
        print(" (Strongly left-skewed - negative returns more extreme)")
    elif sp500_skew < 0:
        print(" (Left-skewed - slight negative tail)")
    elif sp500_skew < 0.5:
        print(" (Right-skewed - slight positive tail)")
    else:
        print(" (Strongly right-skewed - positive returns more extreme)")

    print(f"  Kurtosis:  {sp500_kurt:.6f}", end="")
    if sp500_kurt > 3:
        print(f" (Leptokurtic - fat tails, {sp500_kurt-3:.2f} excess kurtosis)")
    elif sp500_kurt > 0:
        print(f" (Leptokurtic - {sp500_kurt:.2f} excess kurtosis)")
    else:
        print(" (Platykurtic - thin tails)")

if aapl_skew is not None:
    print(f"\nAAPL:")
    print(f"  Skewness:  {aapl_skew:.6f}", end="")
    if aapl_skew < -0.5:
        print(" (Strongly left-skewed - negative returns more extreme)")
    elif aapl_skew < 0:
        print(" (Left-skewed - slight negative tail)")
    elif aapl_skew < 0.5:
        print(" (Right-skewed - slight positive tail)")
    else:
        print(" (Strongly right-skewed - positive returns more extreme)")

    print(f"  Kurtosis:  {aapl_kurt:.6f}", end="")
    if aapl_kurt > 3:
        print(f" (Leptokurtic - fat tails, {aapl_kurt-3:.2f} excess kurtosis)")
    elif aapl_kurt > 0:
        print(f" (Leptokurtic - {aapl_kurt:.2f} excess kurtosis)")
    else:
        print(" (Platykurtic - thin tails)")

print("\n" + "=" * 80)
print("(f) WEEKS MOVING TOGETHER/APART")
print("=" * 80)

weeks_together = None
weeks_apart = None
prop_together = None
prop_apart = None

for row in ws_calc.iter_rows(values_only=False):
    cell_val = str(row[0].value) if row[0].value else ""

    if 'together' in cell_val.lower() and 'same' in cell_val.lower():
        weeks_together = row[1].value
        prop_together = row[2].value
    elif 'apart' in cell_val.lower() and 'opposite' in cell_val.lower():
        weeks_apart = row[1].value
        prop_apart = row[2].value

if weeks_together is not None:
    print(f"Weeks moving together (same sign):  {int(weeks_together)} ({prop_together*100:.2f}%)")
    print(f"Weeks moving apart (opposite sign): {int(weeks_apart)} ({prop_apart*100:.2f}%)")
    print(f"\nInterpretation: AAPL and S&P 500 move in the same direction {prop_together*100:.1f}% of the time")

print("\n" + "=" * 80)
print("(g) COVARIANCE")
print("=" * 80)

cov_manual = None
cov_excel = None

for row in ws_calc.iter_rows(values_only=False):
    cell_val = str(row[0].value) if row[0].value else ""

    if 'Manual:' in cell_val and 'mean_x' in cell_val:
        cov_manual = row[1].value
    elif 'COVARIANCE.P' in cell_val:
        cov_excel = row[1].value

if cov_manual is not None and cov_excel is not None:
    print(f"Manual calculation:      {cov_manual:.10f}")
    print(f"Excel COVARIANCE.P:      {cov_excel:.10f}")
    print(f"Difference:              {abs(cov_manual - cov_excel):.15f}")
    print(f"\nPositive covariance indicates AAPL and S&P 500 tend to move together")

print("\n" + "=" * 80)
print("(h) CORRELATION")
print("=" * 80)

corr_manual = None
corr_excel = None

for row in ws_calc.iter_rows(values_only=False):
    cell_val = str(row[0].value) if row[0].value else ""

    if 'Manual:' in cell_val and 'StdDev' in cell_val:
        corr_manual = row[1].value
    elif 'CORREL' in cell_val:
        corr_excel = row[1].value

if corr_manual is not None and corr_excel is not None:
    print(f"Manual calculation:  {corr_manual:.6f}")
    print(f"Excel CORREL:        {corr_excel:.6f}")
    print(f"Difference:          {abs(corr_manual - corr_excel):.15f}")
    print(f"\nInterpretation:")
    if corr_excel > 0.7:
        print(f"  Strong positive correlation ({corr_excel:.2f})")
    elif corr_excel > 0.4:
        print(f"  Moderate positive correlation ({corr_excel:.2f})")
    elif corr_excel > 0:
        print(f"  Weak positive correlation ({corr_excel:.2f})")
    print(f"  {corr_excel**2*100:.1f}% of variation is shared (R²)")

print("\n" + "=" * 80)
print("(j) REGRESSION STATISTICS")
print("=" * 80)

beta = None
alpha = None
r_squared = None

for row in ws_calc.iter_rows(values_only=False):
    cell_val = str(row[0].value) if row[0].value else ""

    if 'Slope (Beta)' in cell_val or cell_val == "Slope (Beta)":
        beta = row[1].value
    elif 'Intercept (Alpha)' in cell_val or cell_val == "Intercept (Alpha)":
        alpha = row[1].value
    elif 'R-Square' in cell_val and 'Verification' not in cell_val:
        r_squared = row[1].value

if beta is not None:
    print(f"Beta (Slope):         {beta:.6f}")
    print(f"  Interpretation: For every 1% move in S&P 500, AAPL moves {beta:.2f}% on average")
    if beta > 1.2:
        print(f"  Classification: High beta - aggressive/volatile stock")
    elif beta > 0.8:
        print(f"  Classification: Market beta - moves with market")
    else:
        print(f"  Classification: Low beta - defensive stock")

if alpha is not None:
    print(f"\nAlpha (Intercept):    {alpha:.6f} ({alpha*100:.4f}%)")
    if abs(alpha) < 0.001:
        print(f"  Interpretation: Minimal excess return")
    elif alpha > 0:
        print(f"  Interpretation: Positive alpha - outperforms after adjusting for beta")
    else:
        print(f"  Interpretation: Negative alpha - underperforms after adjusting for beta")

if r_squared is not None:
    print(f"\nR-Square:             {r_squared:.6f} ({r_squared*100:.2f}%)")
    print(f"  Interpretation: {r_squared*100:.1f}% of AAPL variance explained by S&P 500")
    print(f"  Systematic risk:    {r_squared*100:.1f}%")
    print(f"  Idiosyncratic risk: {(1-r_squared)*100:.1f}%")
    print(f"\nVerification: R² = Correlation²")
    if corr_excel is not None:
        print(f"  Correlation² = {corr_excel:.6f}² = {corr_excel**2:.6f}")
        print(f"  R² from regression = {r_squared:.6f}")
        print(f"  Match: {abs(r_squared - corr_excel**2) < 0.000001}")

print("\n" + "=" * 80)
print("SUMMARY TABLE FOR REPORT")
print("=" * 80)

summary_data = {
    'Metric': ['Mean Weekly Return', 'Variance', 'Standard Deviation', 'Skewness', 'Kurtosis'],
    'S&P 500': [
        f"{sp500_mean:.8f}" if sp500_mean else "N/A",
        f"{sp500_var_manual:.8f}" if sp500_var_manual else "N/A",
        f"{sp500_std_manual:.8f}" if sp500_std_manual else "N/A",
        f"{sp500_skew:.6f}" if sp500_skew is not None else "N/A",
        f"{sp500_kurt:.6f}" if sp500_kurt is not None else "N/A"
    ],
    'AAPL': [
        f"{aapl_mean:.8f}" if aapl_mean else "N/A",
        f"{aapl_var_manual:.8f}" if aapl_var_manual else "N/A",
        f"{aapl_std_manual:.8f}" if aapl_std_manual else "N/A",
        f"{aapl_skew:.6f}" if aapl_skew is not None else "N/A",
        f"{aapl_kurt:.6f}" if aapl_kurt is not None else "N/A"
    ]
}

df_summary = pd.DataFrame(summary_data)
print("\n", df_summary.to_string(index=False))

print("\n\nRelationship Metrics:")
print(f"  Covariance:           {cov_excel:.10f}" if cov_excel else "  Covariance: N/A")
print(f"  Correlation:          {corr_excel:.6f}" if corr_excel else "  Correlation: N/A")
print(f"  Beta:                 {beta:.6f}" if beta else "  Beta: N/A")
print(f"  Alpha:                {alpha:.6f}" if alpha else "  Alpha: N/A")
print(f"  R²:                   {r_squared:.6f}" if r_squared else "  R²: N/A")

print("\n" + "=" * 80)
print("DATA EXTRACTION COMPLETE")
print("=" * 80)
