# 📊 COMPLETE EXCEL FORMULA FIX GUIDE

## 🔍 ISSUES IDENTIFIED

### **Root Cause:**
The source data file "Data Q2 & Q3.xlsx" contains **43 missing AAPL price values** (from 2019-01-06 to 2019-10-27). This causes:
1. Missing log return calculations
2. All statistical formulas returning errors or blank values
3. Summary sheet showing no results

---

## ✅ SOLUTION: THREE OPTIONS

### **OPTION A: Automated Fix (RECOMMENDED)**
Use the Python script to regenerate the Excel file with clean data.

### **OPTION B: Manual Excel Fix**
Fix directly in Excel by handling missing values manually.

### **OPTION C: Adjust Formulas**
Keep missing values and adjust formulas to ignore them.

---

## 📝 OPTION A: AUTOMATED FIX (RECOMMENDED)

### **Step 1: Clean the Source Data**
✓ **Already completed!** The file `Data Q2 & Q3_CLEAN.xlsx` has been created with:
- Missing AAPL values filled using forward fill method
- All 357 weeks preserved
- No null values remaining

### **Step 2: Regenerate the Analysis File**

Run this command:
```bash
python3 create_fixed_analysis.py
```

This will create a new file: **Q2_Analysis_FIXED.xlsx** with all formulas working correctly.

---

## 🔧 OPTION B: MANUAL EXCEL FIX

### **Step 1: Fix Source Data in Excel**

1. **Open** `Data Q2 & Q3.xlsx`
2. **Go to** the "Q2 (weekly)" sheet
3. **Find missing AAPL values** (rows with blank AAPL cells)
4. **Choose a fill method:**

   **Method 1 - Forward Fill (Copy Previous Value):**
   - Select the AAPL column (Column D)
   - Press `Ctrl+G` → `Special` → `Blanks`
   - Type `=` and press `↑` (up arrow)
   - Press `Ctrl+Enter` to fill all blanks
   - Copy the entire column → Paste Special → Values

   **Method 2 - Use Formula:**
   - In the first blank AAPL cell, enter:
     ```excel
     =IF(ISBLANK(D2), D1, D2)
     ```
   - Copy this formula down the entire AAPL column
   - Replace formulas with values

### **Step 2: Fix Log Return Formulas**

1. **Open** your analysis Excel file
2. **Go to** "Data & Returns" sheet
3. **Check columns E and F** (S&P 500 and AAPL Log Returns)
4. **Verify the formula in E3:**
   ```excel
   =IF(OR(ISBLANK(C3), ISBLANK(C2), C2=0), "", LN(C3/C2))
   ```
5. **Copy E3 down** to the last row of data
6. **Verify the formula in F3:**
   ```excel
   =IF(OR(ISBLANK(D3), ISBLANK(D2), D2=0), "", LN(D3/D2))
   ```
7. **Copy F3 down** to the last row of data

### **Step 3: Fix Calculations Sheet**

1. **Go to** "Calculations" sheet
2. **Find the MEAN section** (should be around row 5-6)
3. **Verify the range** in the AVERAGE formula matches your data rows

   For example, if you have 313 returns (314 prices):
   ```excel
   =AVERAGE('Data & Returns'!E3:E315)
   ```

4. **Key formulas to check:**

   **a) Mean (Row ~6):**
   ```excel
   B6: =AVERAGE('Data & Returns'!E3:E315)
   C6: =AVERAGE('Data & Returns'!F3:F315)
   ```

   **b) Manual Variance (Row ~9):**
   ```excel
   B9: =SUMPRODUCT(('Data & Returns'!E3:E315-B6)^2)/COUNT('Data & Returns'!E3:E315)
   C9: =SUMPRODUCT(('Data & Returns'!F3:F315-C6)^2)/COUNT('Data & Returns'!F3:F315)
   ```

   **c) Excel Variance (Row ~10):**
   ```excel
   B10: =VAR.P('Data & Returns'!E3:E315)
   C10: =VAR.P('Data & Returns'!F3:F315)
   ```

   **d) Variance Difference (Row ~11):**
   ```excel
   B11: =ABS(B9-B10)
   C11: =ABS(C9-C10)
   ```

   **e) Manual Std Dev (Row ~15):**
   ```excel
   B15: =SQRT(B9)
   C15: =SQRT(C9)
   ```

   **f) Excel Std Dev (Row ~16):**
   ```excel
   B16: =STDEV.P('Data & Returns'!E3:E315)
   C16: =STDEV.P('Data & Returns'!F3:F315)
   ```

   **g) Std Dev Difference (Row ~17):**
   ```excel
   B17: =ABS(B15-B16)
   C17: =ABS(C15-C16)
   ```

   **h) Skewness (Row ~21):**
   ```excel
   B21: =SKEW('Data & Returns'!E3:E315)
   C21: =SKEW('Data & Returns'!F3:F315)
   ```

   **i) Kurtosis (Row ~22):**
   ```excel
   B22: =KURT('Data & Returns'!E3:E315)
   C22: =KURT('Data & Returns'!F3:F315)
   ```

   **j) Weeks Moving Together (Row ~26):**
   ```excel
   B26: =SUMPRODUCT((SIGN('Data & Returns'!E3:E315)=SIGN('Data & Returns'!F3:F315))*1)
   C26: =B26/COUNT('Data & Returns'!E3:E315)
   ```

   **k) Weeks Moving Apart (Row ~27):**
   ```excel
   B27: =SUMPRODUCT((SIGN('Data & Returns'!E3:E315)<>SIGN('Data & Returns'!F3:F315))*1)
   C27: =B27/COUNT('Data & Returns'!E3:E315)
   ```

   **l) Manual Covariance (Row ~31):**
   ```excel
   B31: =SUMPRODUCT(('Data & Returns'!E3:E315-B6),('Data & Returns'!F3:F315-C6))/COUNT('Data & Returns'!E3:E315)
   ```

   **m) Excel Covariance (Row ~32):**
   ```excel
   B32: =COVARIANCE.P('Data & Returns'!E3:E315,'Data & Returns'!F3:F315)
   ```

   **n) Covariance Difference (Row ~33):**
   ```excel
   B33: =ABS(B31-B32)
   ```

   **o) Manual Correlation (Row ~37):**
   ```excel
   B37: =B32/(B16*C16)
   ```

   **p) Excel Correlation (Row ~38):**
   ```excel
   B38: =CORREL('Data & Returns'!E3:E315,'Data & Returns'!F3:F315)
   ```

   **q) Correlation Difference (Row ~39):**
   ```excel
   B39: =ABS(B37-B38)
   ```

   **r) Regression Slope/Beta (Row ~43):**
   ```excel
   B43: =SLOPE('Data & Returns'!F3:F315,'Data & Returns'!E3:E315)
   ```

   **s) Regression Intercept/Alpha (Row ~44):**
   ```excel
   B44: =INTERCEPT('Data & Returns'!F3:F315,'Data & Returns'!E3:E315)
   ```

   **t) R-Square (Row ~45):**
   ```excel
   B45: =RSQ('Data & Returns'!F3:F315,'Data & Returns'!E3:E315)
   ```

### **Step 4: Verify Summary Results Sheet**

1. **Go to** "Summary Results" sheet
2. **Check that all formulas** link to the correct cells in the Calculations sheet
3. **Example formulas:**
   ```excel
   Mean Weekly Return (S&P 500): =Calculations!B6
   Mean Weekly Return (AAPL):    =Calculations!C6
   Variance (S&P 500):           =Calculations!B10
   Variance (AAPL):              =Calculations!C10
   ```

---

## ⚙️ OPTION C: ADJUST FORMULAS TO HANDLE MISSING VALUES

If you want to keep the missing values in the source data, adjust formulas to skip them:

### **Use AVERAGEIF instead of AVERAGE:**
```excel
=AVERAGEIF('Data & Returns'!E3:E315,"<>0")
```

### **Use array formulas with filtering:**
```excel
=AVERAGE(IF('Data & Returns'!E3:E315<>0,'Data & Returns'!E3:E315))
```
(Press `Ctrl+Shift+Enter` to make it an array formula)

---

## 🎯 EXPECTED RESULTS

After fixing, you should see these values (based on your provided data):

| Metric | S&P 500 | AAPL |
|--------|---------|------|
| Mean | 0.002503485 | 0.004548139 |
| Variance (Manual) | 0.000740176 | 0.001672628 |
| Variance (Excel VAR.P) | 0.000740176 | 0.001672628 |
| Std Dev (Manual) | 0.027206167 | 0.040897772 |
| Std Dev (Excel STDEV.P) | 0.027206167 | 0.040897772 |
| Skewness | -0.89559749 | -0.494444175 |
| Kurtosis | 6.695217061 | 2.480645924 |
| Weeks Moving Together | 254 | 0.811501597 (proportion) |
| Weeks Moving Apart | 59 | 0.188498403 (proportion) |
| Covariance (Manual) | 0.0008213 | - |
| Covariance (Excel) | 0.0008213 | - |
| Correlation (Manual) | 0.73813295 | - |
| Correlation (Excel) | 0.73813295 | - |
| Slope (Beta) | 1.109601088 | - |
| Intercept (Alpha) | 0.00177027 | - |
| R-Square | 0.544840251 | - |

---

## 🚨 COMMON ERRORS AND FIXES

### **#NAME? Error**
- **Cause:** Excel doesn't recognize the function name
- **Fix:** Check spelling (e.g., `AVERAGE` not `AVARAGE`)

### **#DIV/0! Error**
- **Cause:** Division by zero or empty range
- **Fix:** Ensure data ranges contain values

### **#REF! Error**
- **Cause:** Formula references deleted cells
- **Fix:** Update cell references

### **#VALUE! Error**
- **Cause:** Wrong data type (e.g., text in number formula)
- **Fix:** Check for text values in numeric columns

### **Blank/Missing Results**
- **Cause:** Formula range doesn't match data range
- **Fix:** Adjust E3:E315 to match your actual data rows

---

## 📞 NEED HELP?

If you continue to see errors:
1. Check that column references match (E for S&P 500 returns, F for AAPL returns)
2. Verify row ranges match your data (E3:E315 assumes 313 returns)
3. Ensure all formulas use single quotes around sheet names with spaces: `'Data & Returns'!`
4. Save and reopen the file to force recalculation
