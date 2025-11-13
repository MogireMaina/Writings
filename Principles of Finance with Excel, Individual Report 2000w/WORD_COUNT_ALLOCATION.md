# WORD COUNT ALLOCATION PLAN
## Question 2 Report: Statistical Analysis of Weekly Stock Returns

**Target:** 1,700 words (Maximum: 2,000 words)
**Strategy:** Focused, concise analysis with depth where it matters most

---

## COMPLETE DATA SUMMARY FOR REPORT

### Dataset Information
- Stock: Apple Inc. (AAPL)
- Index: S&P 500
- Frequency: Weekly
- Period: November 2019 to November 2025 (6 years)
- Observations: **313 weekly returns** (314 price points)

### Key Statistical Results

| Metric | S&P 500 | AAPL |
|--------|---------|------|
| **Mean Weekly Return** | 0.0025034847 (0.2503%) | 0.0045481394 (0.4548%) |
| **Annualized Return** | 13.02% | 23.65% |
| **Variance** | 0.0007401755 | 0.0016726277 |
| **Standard Deviation** | 0.0272061675 (2.72%) | 0.0408977719 (4.09%) |
| **Annualized Volatility** | 19.63% | 29.50% |
| **Skewness** | -0.8956 (left-skewed) | -0.4944 (left-skewed) |
| **Kurtosis (excess)** | 6.6952 (fat tails) | 2.4806 (fat tails) |

### Relationship Metrics
- **Weeks Moving Together:** 254 (81.15%)
- **Weeks Moving Apart:** 59 (18.85%)
- **Covariance:** 0.0008212996
- **Correlation:** 0.7381 (strong positive)
- **Beta:** 1.1096 (aggressive stock)
- **Alpha:** 0.0017702700 (0.177% weekly)
- **R-Square:** 0.5448 (54.48%)

---

## SECTION-BY-SECTION WORD COUNT ALLOCATION

### 1. Executive Summary (100 words)
**Purpose:** High-level overview of findings
**Key Points:**
- Dataset overview
- Main findings in bullet points
- Strong correlation, high beta
- Non-normal distributions

### 2. Introduction (150 words total)
**2.1 Dataset Description (75 words)**
- Stock/index selection rationale
- Time period and observations
- Brief context (COVID, inflation, etc.)

**2.2 Methodology (75 words)**
- Log returns explanation
- Formula: r_t = ln(P_t/P_{t-1})
- Advantages of log returns
- Brief mention of Excel formulas used

### 3. Part (a): Mean Weekly Log Return (120 words)
**Results (30 words)**
- S&P 500: 0.25% weekly (13% annualized)
- AAPL: 0.45% weekly (23.6% annualized)

**Discussion (90 words)**
- Positive returns indicate capital appreciation
- AAPL outperformance (0.45% vs 0.25%)
- Context: 6-year period includes market volatility
- Risk-return perspective (returns alone insufficient)

### 4. Part (b): Variance (110 words)
**Methodology (40 words)**
- Formula: Σ(x-mean)²/N
- Excel manual vs VAR.P comparison

**Results (30 words)**
- S&P 500: 0.00074
- AAPL: 0.00167 (2.26x higher)
- Verification: difference ≈ 0

**Discussion (40 words)**
- AAPL higher variance due to single-stock risk
- S&P 500 benefits from diversification
- Variance in squared units (hard to interpret)

### 5. Part (c): Standard Deviation (130 words)
**Methodology (30 words)**
- StdDev = √Variance
- Excel SQRT vs STDEV.P

**Results (40 words)**
- S&P 500: 2.72% weekly (19.6% annualized)
- AAPL: 4.09% weekly (29.5% annualized)
- AAPL 1.5x more volatile

**Discussion (60 words)**
- Standard deviation as key risk measure
- AAPL higher volatility (systematic + idiosyncratic risk)
- S&P 500 mainly systematic risk
- Annualization using √52 rule
- Investment implications (risk tolerance)

### 6. Part (d): Histograms (140 words)
**Methodology (30 words)**
- Bins created: S&P 500 (-15% to +15%), AAPL (-20% to +20%)
- Excel COUNTIF formulas

**S&P 500 Discussion (45 words)**
- Central concentration around mean
- Approximate symmetry with negative skew
- Fat tails visible
- Range and extreme events

**AAPL Discussion (45 words)**
- Wider distribution (reflects higher volatility)
- More dispersed returns
- Company-specific events visible
- Comparison to S&P 500

**Insights (20 words)**
- Visual confirmation of variance results
- Non-normality evident

### 7. Part (e): Skewness and Kurtosis (160 words)
**Skewness Results & Discussion (80 words)**
- S&P 500: -0.896 (strongly left-skewed)
- AAPL: -0.494 (moderately left-skewed)
- Interpretation: negative returns more extreme than positive
- Crash risk visible (COVID-19, etc.)
- Investor implications (downside risk)
- Left skew common in equity markets

**Kurtosis Results & Discussion (80 words)**
- S&P 500: 6.70 excess kurtosis (very fat tails)
- AAPL: 2.48 excess kurtosis (fat tails)
- Leptokurtic distributions
- Extreme events more frequent than normal distribution predicts
- "Black swan" events underestimated by normal models
- Implications for VaR, option pricing
- Need for robust risk models

### 8. Part (f): Co-movement Analysis (100 words)
**Results (30 words)**
- Together: 254 weeks (81.15%)
- Apart: 59 weeks (18.85%)
- Excel SUMPRODUCT formula

**Discussion (70 words)**
- High co-movement expected (AAPL in S&P 500)
- Systematic risk drives most movements
- 18.85% apart = idiosyncratic risk
- Limited diversification benefit
- Simple sign-based analysis limitation
- Leads to more sophisticated measures (correlation)

### 9. Part (g): Covariance (100 words)
**Methodology (30 words)**
- Formula: Σ(x-mean_x)(y-mean_y)/N
- Manual vs COVARIANCE.P

**Results (20 words)**
- Covariance: 0.00082
- Verification: difference ≈ 0

**Discussion (50 words)**
- Positive covariance confirms co-movement
- Scale-dependent (hard to interpret absolute value)
- Key to portfolio variance formula
- Foundation for beta calculation
- Limitation: unbounded, unit-dependent

### 10. Part (h): Correlation (140 words)
**Methodology (30 words)**
- Formula: Cov/(σ_x × σ_y)
- Manual vs CORREL
- Standardizes covariance

**Results (20 words)**
- Correlation: 0.7381
- Strong positive relationship

**Discussion (90 words)**
- 73.8% correlation = strong positive relationship
- 54.5% of variation shared (R²)
- AAPL highly market-sensitive
- Reasons: AAPL is S&P 500 component, tech sector dynamics, macro factors
- Correlation not constant over time (crisis periods higher)
- Implications: limited diversification, effective hedging possible
- Relationship to R² (preview regression)

### 11. Part (i): Scatter Diagram (80 words)
**Visual Analysis (80 words)**
- Upward-sloping cloud confirms positive correlation
- Points don't fall on perfect line (idiosyncratic risk)
- Slope interpretation (beta > 1)
- Outliers represent extreme market events
- Trendline = regression line
- Visual representation of systematic vs idiosyncratic risk
- Leads into regression analysis

### 12. Part (j): Regression Statistics (240 words)
**Beta Analysis (100 words)**
- Beta: 1.1096
- Interpretation: 1% S&P 500 move → 1.11% AAPL move
- Aggressive/cyclical stock
- Formula: Cov/Var or SLOPE function
- Drivers: growth profile, tech sector, market sentiment
- Higher systematic risk than market
- Suitable for risk-tolerant investors
- Amplifies market movements (both up and down)

**Alpha Analysis (70 words)**
- Alpha: 0.00177 (0.177% weekly, ~9.2% annualized)
- Positive excess return beyond beta prediction
- Potential sources: innovation, brand strength, management
- CAPM context (should be zero in efficient markets)
- Statistical significance caveat (would need t-test)
- Outperformance interpretation

**R-Square Analysis (70 words)**
- R²: 0.5448 (54.48%)
- 54.48% variance explained by S&P 500 (systematic risk)
- 45.52% unexplained (idiosyncratic risk)
- Verification: 0.7381² = 0.5448 ✓
- Risk decomposition implications
- Beta-hedging effectiveness
- Diversification potential

### 13. Conclusion (160 words)
**Key Findings Summary (80 words)**
- Positive returns: S&P 500 13% annualized, AAPL 23.6% annualized
- AAPL 1.5x more volatile (29.5% vs 19.6%)
- Both left-skewed with fat tails
- Strong correlation (0.738), high co-movement (81%)
- Beta 1.11 (aggressive), Alpha 0.18% weekly
- 54% variance market-driven, 46% idiosyncratic

**Investment Implications (50 words)**
- AAPL offers higher returns with higher risk
- Limited diversification benefit vs S&P 500
- Suitable for risk-tolerant investors
- Fat tails require robust risk management
- High beta = greater systematic risk

**Methodological Validation (30 words)**
- All calculations verified (manual vs Excel functions)
- Internal consistency confirmed (R²=Corr², etc.)
- Technical proficiency demonstrated

### 14. References (30 words)
- Excel functions documentation
- Academic sources (Markowitz, Sharpe, CAPM)
- Data sources
- Course materials

### 15. Appendix (Minimal - 50 words)
- Excel file structure overview
- Sheet descriptions
- Formula examples
- Quality controls

---

## TOTAL WORD COUNT ALLOCATION

| Section | Words | Cumulative |
|---------|-------|------------|
| Executive Summary | 100 | 100 |
| Introduction | 150 | 250 |
| (a) Mean | 120 | 370 |
| (b) Variance | 110 | 480 |
| (c) Standard Deviation | 130 | 610 |
| (d) Histograms | 140 | 750 |
| (e) Skewness & Kurtosis | 160 | 910 |
| (f) Co-movement | 100 | 1,010 |
| (g) Covariance | 100 | 1,110 |
| (h) Correlation | 140 | 1,250 |
| (i) Scatter Diagram | 80 | 1,330 |
| (j) Regression | 240 | 1,570 |
| Conclusion | 160 | 1,730 |
| References | 30 | 1,760 |
| Appendix | 50 | 1,810 |

**Total Target: 1,810 words**
(Allows for ~10% variance, staying well under 2,000 maximum)

---

## WRITING PRINCIPLES

1. **Conciseness:** Every sentence must add value
2. **Precision:** Use exact values from analysis
3. **Integration:** Connect sections logically
4. **Balance:** Equal weight to calculation methodology and interpretation
5. **Evidence:** Back all statements with data
6. **Technical rigor:** Show both manual and Excel function approaches
7. **Practical relevance:** Link statistical findings to investment decisions

---

## PRIORITY SECTIONS (Where to spend words)

**HIGH PRIORITY (More detailed):**
1. Regression analysis (240 words) - Most important for finance
2. Skewness & Kurtosis (160 words) - Key for risk understanding
3. Conclusion (160 words) - Synthesis and implications
4. Introduction (150 words) - Sets context
5. Correlation (140 words) - Fundamental relationship measure
6. Histograms (140 words) - Visual understanding

**MEDIUM PRIORITY (Balanced):**
7. Standard Deviation (130 words) - Key risk measure
8. Mean (120 words) - Foundation metric
9. Variance (110 words) - Building block
10. Covariance (100 words) - Technical but important
11. Co-movement (100 words) - Intuitive measure

**LOWER PRIORITY (Concise):**
12. Scatter diagram (80 words) - Visual, less text needed
13. Appendix (50 words) - Reference only
14. References (30 words) - List format

---

## EFFICIENCY STRATEGIES

1. **Use tables** instead of prose for results
2. **Bullet points** for key findings
3. **Integrate verification** within discussion (don't separate)
4. **Cross-reference** instead of repeating (e.g., "as shown in Part c")
5. **Combine related points** (e.g., manual + Excel in one discussion)
6. **Focus interpretation** on investment implications, not just statistics

---

**ALLOCATION COMPLETE - READY FOR REPORT DRAFTING**
