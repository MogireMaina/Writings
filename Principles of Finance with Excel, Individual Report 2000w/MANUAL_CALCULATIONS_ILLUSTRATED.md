# MANUAL CALCULATIONS - STEP BY STEP ILLUSTRATION
## Question 2: Statistical Analysis of Weekly Stock Returns

This document illustrates the **manual calculation steps** for each statistical measure, showing how to compute them by hand before verifying with Excel functions.

---

## SAMPLE DATA SETUP

For illustration purposes, let's say we have these first 5 weekly returns (hypothetical example):

**S&P 500 Returns (r_s):**
- Week 1: 0.0050 (0.50%)
- Week 2: -0.0025 (-0.25%)
- Week 3: 0.0075 (0.75%)
- Week 4: 0.0010 (0.10%)
- Week 5: -0.0040 (-0.40%)

**AAPL Returns (r_a):**
- Week 1: 0.0080 (0.80%)
- Week 2: -0.0050 (-0.50%)
- Week 3: 0.0120 (1.20%)
- Week 4: 0.0020 (0.20%)
- Week 5: -0.0060 (-0.60%)

Total observations: N = 356 (in actual data)

---

## (a) MEAN WEEKLY LOG RETURN

### Formula:
**Mean = Σx / N**

### Step-by-Step Calculation for S&P 500:

**Step 1:** Sum all returns
```
Sum = 0.0050 + (-0.0025) + 0.0075 + 0.0010 + (-0.0040) + ... (all 356 returns)
    = [sum of all 356 values]
```

**Step 2:** Divide by number of observations
```
Mean = Sum / N
     = Sum / 356
```

### Excel Formula:
```excel
=AVERAGE(E3:E358)
```
Where E3:E358 contains all S&P 500 returns.

### Manual Excel Implementation:
```excel
=SUM(E3:E358)/COUNT(E3:E358)
```

---

## (b) VARIANCE

### Formula:
**Variance = Σ(x_i - mean)² / N**

### Step-by-Step Calculation for S&P 500:

**Step 1:** Calculate the mean (from part a)
```
mean = 0.002842 (example value)
```

**Step 2:** Calculate deviation from mean for each observation
```
Week 1: 0.0050 - 0.002842 = 0.002158
Week 2: -0.0025 - 0.002842 = -0.005342
Week 3: 0.0075 - 0.002842 = 0.004658
Week 4: 0.0010 - 0.002842 = -0.001842
Week 5: -0.0040 - 0.002842 = -0.006842
... (repeat for all 356 observations)
```

**Step 3:** Square each deviation
```
Week 1: (0.002158)² = 0.000004658
Week 2: (-0.005342)² = 0.000028537
Week 3: (0.004658)² = 0.000021697
Week 4: (-0.001842)² = 0.000003393
Week 5: (-0.006842)² = 0.000046813
... (repeat for all 356 observations)
```

**Step 4:** Sum all squared deviations
```
Sum of squared deviations = 0.000004658 + 0.000028537 + 0.000021697 + ... (all 356 values)
                         = Σ(x_i - mean)²
```

**Step 5:** Divide by N
```
Variance = Sum of squared deviations / 356
         = Σ(x_i - mean)² / 356
```

### Excel Manual Formula:
```excel
=SUMPRODUCT((E3:E358-$B$6)^2)/COUNT(E3:E358)
```
Where B6 contains the mean calculated in part (a).

**Breakdown of formula:**
- `E3:E358` = all return values
- `$B$6` = mean (absolute reference)
- `(E3:E358-$B$6)` = deviations from mean
- `(E3:E358-$B$6)^2` = squared deviations
- `SUMPRODUCT(...)` = sum of squared deviations
- `/COUNT(E3:E358)` = divide by N

### Excel Built-in Function (Verification):
```excel
=VAR.P(E3:E358)
```

### Expected Result:
The difference between manual and VAR.P should be ≈ 0 (within rounding error).

---

## (c) STANDARD DEVIATION

### Formula:
**Standard Deviation = √(Variance)**

### Step-by-Step Calculation:

**Step 1:** Get variance from part (b)
```
Variance = 0.000187 (example value)
```

**Step 2:** Take square root
```
Standard Deviation = √(0.000187)
                   = 0.01368
                   = 1.368%
```

### Excel Manual Formula:
```excel
=SQRT(B11)
```
Where B11 contains the manually calculated variance.

### Excel Built-in Function (Verification):
```excel
=STDEV.P(E3:E358)
```

---

## (f) WEEKS MOVING TOGETHER/APART

### Method:
Count weeks where both returns have the same sign (both positive or both negative).

### Step-by-Step Calculation:

**Step 1:** Determine sign of each return

| Week | S&P 500 | Sign | AAPL | Sign | Same? |
|------|---------|------|------|------|-------|
| 1    | 0.0050  | +    | 0.0080 | +  | YES   |
| 2    | -0.0025 | -    | -0.0050| -  | YES   |
| 3    | 0.0075  | +    | 0.0120 | +  | YES   |
| 4    | 0.0010  | +    | 0.0020 | +  | YES   |
| 5    | -0.0040 | -    | -0.0060| -  | YES   |
| ...  | ...     | ...  | ...    | ... | ...   |

**Step 2:** Count "YES" (same sign)
```
Weeks Moving Together = count of weeks where signs match
```

**Step 3:** Count "NO" (opposite sign)
```
Weeks Moving Apart = Total weeks - Weeks Moving Together
                   = 356 - Weeks Moving Together
```

**Step 4:** Calculate proportions
```
Proportion Together = Weeks Moving Together / 356
Proportion Apart = Weeks Moving Apart / 356
```

### Excel Formula:
```excel
=SUMPRODUCT((SIGN(E3:E358)=SIGN(F3:F358))*1)
```

**Breakdown:**
- `SIGN(E3:E358)` = returns +1 for positive, -1 for negative, 0 for zero
- `SIGN(E3:E358)=SIGN(F3:F358)` = TRUE when signs match, FALSE otherwise
- `*1` = converts TRUE to 1, FALSE to 0
- `SUMPRODUCT(...)` = sums all the 1s (matching weeks)

---

## (g) COVARIANCE

### Formula:
**Cov(X,Y) = Σ[(x_i - mean_x) × (y_i - mean_y)] / N**

### Step-by-Step Calculation:

**Step 1:** Calculate means (from part a)
```
mean_sp500 = 0.002842 (example)
mean_aapl = 0.004231 (example)
```

**Step 2:** Calculate deviations for each series

| Week | S&P 500 | Dev(S&P) | AAPL | Dev(AAPL) |
|------|---------|----------|------|-----------|
| 1    | 0.0050  | 0.002158 | 0.0080 | 0.003769 |
| 2    | -0.0025 | -0.005342| -0.0050| -0.009231|
| 3    | 0.0075  | 0.004658 | 0.0120 | 0.007769 |
| 4    | 0.0010  | -0.001842| 0.0020 | -0.002231|
| 5    | -0.0040 | -0.006842| -0.0060| -0.010231|
| ...  | ...     | ...      | ...    | ...      |

**Step 3:** Multiply deviations for each week
```
Week 1: 0.002158 × 0.003769 = 0.000008134
Week 2: (-0.005342) × (-0.009231) = 0.000049313
Week 3: 0.004658 × 0.007769 = 0.000036192
Week 4: (-0.001842) × (-0.002231) = 0.000004110
Week 5: (-0.006842) × (-0.010231) = 0.000069998
... (repeat for all 356 observations)
```

**Step 4:** Sum all products
```
Sum = 0.000008134 + 0.000049313 + 0.000036192 + ... (all 356 values)
    = Σ[(x_i - mean_x) × (y_i - mean_y)]
```

**Step 5:** Divide by N
```
Covariance = Sum / 356
```

### Excel Manual Formula:
```excel
=SUMPRODUCT((E3:E358-$B$6),(F3:F358-$C$6))/COUNT(E3:E358)
```

**Breakdown:**
- `E3:E358-$B$6` = S&P 500 deviations from mean
- `F3:F358-$C$6` = AAPL deviations from mean
- `SUMPRODUCT(...)` = multiplies corresponding deviations and sums
- `/COUNT(E3:E358)` = divide by N

### Excel Built-in Function (Verification):
```excel
=COVARIANCE.P(E3:E358,F3:F358)
```

---

## (h) CORRELATION

### Formula:
**Corr(X,Y) = Cov(X,Y) / (StdDev_X × StdDev_Y)**

### Step-by-Step Calculation:

**Step 1:** Get covariance (from part g)
```
Covariance = 0.000234 (example)
```

**Step 2:** Get standard deviations (from part c)
```
StdDev_SP500 = 0.01368 (example)
StdDev_AAPL = 0.02154 (example)
```

**Step 3:** Multiply standard deviations
```
Product of StdDevs = 0.01368 × 0.02154
                   = 0.000294667
```

**Step 4:** Divide covariance by product
```
Correlation = 0.000234 / 0.000294667
            = 0.7941
```

### Excel Manual Formula:
```excel
=B33/(B18*C18)
```
Where:
- B33 = covariance
- B18 = S&P 500 standard deviation
- C18 = AAPL standard deviation

### Excel Built-in Function (Verification):
```excel
=CORREL(E3:E358,F3:F358)
```

---

## (j) REGRESSION STATISTICS

### Formulas:
**Beta (Slope) = Cov(X,Y) / Var(X)**
**Alpha (Intercept) = Mean(Y) - Beta × Mean(X)**
**R² = Correlation²**

### Step-by-Step Calculation for BETA:

**Step 1:** Get covariance of AAPL and S&P 500 (from part g)
```
Cov(AAPL, S&P500) = 0.000234 (example)
```

**Step 2:** Get variance of S&P 500 (from part b)
```
Var(S&P500) = 0.000187 (example)
```

**Step 3:** Divide covariance by variance
```
Beta = Cov(AAPL, S&P500) / Var(S&P500)
     = 0.000234 / 0.000187
     = 1.2513
```

**Interpretation:** For every 1% move in S&P 500, AAPL moves 1.25% on average.

### Excel Manual Formula for Beta:
```excel
=B33/B11
```
Where:
- B33 = covariance
- B11 = S&P 500 variance

### Excel Built-in Function (Verification):
```excel
=SLOPE(F3:F358,E3:E358)
```
Note: SLOPE(Y, X) - AAPL is Y (dependent), S&P 500 is X (independent)

---

### Step-by-Step Calculation for ALPHA:

**Step 1:** Get means (from part a)
```
Mean(AAPL) = 0.004231 (example)
Mean(S&P500) = 0.002842 (example)
```

**Step 2:** Get beta (calculated above)
```
Beta = 1.2513
```

**Step 3:** Calculate alpha
```
Alpha = Mean(AAPL) - Beta × Mean(S&P500)
      = 0.004231 - (1.2513 × 0.002842)
      = 0.004231 - 0.003556
      = 0.000675
      = 0.0675%
```

**Interpretation:** AAPL generates 0.0675% weekly return beyond what beta predicts.

### Excel Manual Formula for Alpha:
```excel
=C6-B43*B6
```
Where:
- C6 = AAPL mean
- B43 = Beta
- B6 = S&P 500 mean

### Excel Built-in Function (Verification):
```excel
=INTERCEPT(F3:F358,E3:E358)
```

---

### Step-by-Step Calculation for R²:

**Step 1:** Get correlation (from part h)
```
Correlation = 0.7941 (example)
```

**Step 2:** Square the correlation
```
R² = (0.7941)²
   = 0.6306
   = 63.06%
```

**Interpretation:** 63% of AAPL's return variance is explained by S&P 500 movements.

### Excel Manual Formula for R²:
```excel
=B38^2
```
Where B38 = correlation

### Excel Built-in Function (Verification):
```excel
=RSQ(F3:F358,E3:E358)
```

---

## VERIFICATION CHECKLIST

For each calculation, verify:

1. **Manual vs. Excel Function Difference ≈ 0**
   - Variance: |Manual - VAR.P| < 0.00000001
   - Std Dev: |Manual - STDEV.P| < 0.00000001
   - Covariance: |Manual - COVARIANCE.P| < 0.00000001
   - Correlation: |Manual - CORREL| < 0.00000001

2. **Internal Consistency**
   - StdDev = √(Variance)
   - R² = Correlation²
   - Beta = Covariance / Variance
   - Alpha = Mean(Y) - Beta × Mean(X)

3. **Logical Ranges**
   - Correlation: -1 ≤ r ≤ 1
   - R²: 0 ≤ R² ≤ 1
   - Variance ≥ 0
   - StdDev ≥ 0

---

## SUMMARY OF EXCEL FORMULAS USED

| Calculation | Manual Formula | Excel Function | Purpose |
|-------------|----------------|----------------|---------|
| Mean | =SUM(...)/COUNT(...) | =AVERAGE(...) | Central tendency |
| Variance | =SUMPRODUCT((x-mean)^2)/N | =VAR.P(...) | Dispersion measure |
| Std Dev | =SQRT(variance) | =STDEV.P(...) | Risk measure |
| Skewness | Complex | =SKEW(...) | Asymmetry measure |
| Kurtosis | Complex | =KURT(...) | Tail heaviness |
| Co-movement | =SUMPRODUCT((SIGN(x)=SIGN(y))*1) | N/A | Direction matching |
| Covariance | =SUMPRODUCT((x-mean_x),(y-mean_y))/N | =COVARIANCE.P(...) | Joint variability |
| Correlation | =Cov/(StdDev_x*StdDev_y) | =CORREL(...) | Standardized relationship |
| Beta | =Cov/Var_x | =SLOPE(y,x) | Systematic risk |
| Alpha | =Mean_y-Beta*Mean_x | =INTERCEPT(y,x) | Excess return |
| R² | =Correlation^2 | =RSQ(y,x) | Goodness of fit |

---

**END OF MANUAL CALCULATIONS ILLUSTRATION**
