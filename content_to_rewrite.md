# Content Requiring Paraphrasing

## Introduction

This report presents three Excel-based financial analyses: NBA player salary distributions, a five-year comparison of Apple Inc. (AAPL) returns against the S&P 500, and a beta analysis of three stocks across different sectors. The NBA analysis employs 2025-2026 data for 420 players, utilizing text functions to explore compensation patterns. The AAPL analysis examines 313 weeks from November 2019 to November 2025, encompassing the COVID-19 crash, recovery, and AI-driven technology rally. The three-stock beta analysis uses 500 days of daily returns from November 2023 to November 2025 for JPMorgan Chase, Johnson & Johnson, and Apple, decomposing variance into systematic and idiosyncratic components.

---

## Question 1: NBA Salary Analysis

### Dataset and Methodology

The analysis examines 420 NBA player salaries for the 2025-2026 season, sourced from ESPN's salary database. Excel text manipulation functions including LEFT, MID, FIND, and TRIM were employed to parse composite name fields into first and last name components while extracting position designations (Guard, Forward, Center). The dataset was analyzed using COUNTIF for frequency distributions by position and team, SUMIF and AVERAGEIF for conditional aggregation calculating team-level and position-level statistics, and INDEX-MATCH-RANK combinations for identifying extrema and ranking operations. Ten distinct research questions explored total league compensation, positional salary differences, team construction strategies, and elite player concentration patterns.

### Salary Distribution and Power Law Concentration

Total NBA salary of $5.49 billion yields a mean of $13.07 million, but the median of $7.61 million reveals significant right-skewness. Just 15 players (3.6%) earning above $50 million capture $813 million (14.8% of total), mirroring power law distributions. Fix (2018) demonstrates that hierarchical organizational structures create such income distribution tails, suggesting this pattern reflects hierarchical organization. The highest-paid player (Curry, $59.61M) earns 46.8 times the minimum ($1.27M), yet the top ten show salary compression—only $5.9M separates first from tenth, suggesting superstars are underpaid relative to marginal revenue, constrained by maximum contract provisions.

### The Position Paradox

Centers (14.0%, 59 players) command the highest average salary at $13.53 million versus guards ($12.73M, 47.4%) and forwards ($13.33M, 38.6%). This 6.3% premium reflects scarcity—3.4 times fewer centers drive competitive bidding. However, the highest individual salary belongs to a guard (Curry, $59.61M), as do six of the top ten. Scarcity elevates the floor; skill determines the ceiling.

### Team Strategy Divergence

Team-level analysis reveals dramatically different roster construction philosophies. The Boston Celtics maintain an average salary of $23.11 million across just eight players, while the Brooklyn Nets average $8.37 million across sixteen players—a 2.8-fold difference. The LA Clippers lead in total expenditure at $239.8 million but rank only third in average salary, carrying thirteen players. This quality-versus-quantity tradeoff reflects different theories of roster optimization: star-heavy teams concentrate resources on proven elite talent with minimum contracts filling remaining roster spots, while depth-focused teams distribute salary more evenly to maintain rotation flexibility and injury protection. The salary data quantifies these strategic divergences clearly, though evaluating which approach correlates with team success would require performance metrics beyond this dataset.

---

## Question 2: AAPL vs S&P 500

### Return Characteristics and Risk Profile

The five-year analysis period encompasses extraordinary market conditions including the March 2020 COVID-19 crash, subsequent technology-led recovery, 2022 inflation-driven correction, and 2023-2024 AI boom. Over 313 weeks, AAPL generated a mean log return of 0.455% per week (23.6% annualized) compared to the S&P 500's 0.250% (13.0% annualized), confirming technology sector outperformance during this period. Manual variance calculations yielded 0.001673 for AAPL and 0.000740 for the S&P 500, verified against Excel's VAR.S function (0.001678 and 0.000743 respectively), with 0.32% differences attributable to rounding in intermediate calculation steps. The resulting standard deviations of 4.10% (AAPL) and 2.72% (S&P 500) indicate that AAPL exhibits 1.51 times greater volatility. However, examining the return-to-risk ratio reveals AAPL's ratio of 0.110 exceeds the S&P 500's 0.092, indicating superior return per unit of risk—1.81 times higher return for 1.51 times higher risk represents a favorable tradeoff.

### Distribution Properties and Tail Risk

Distribution properties reveal important nuances beyond mean and variance. Both securities exhibit negative skewness (AAPL: -0.49, S&P 500: -0.90), indicating asymmetric downside risk with more extreme negative returns than positive ones. Notably, the S&P 500's more negative skewness and substantially higher kurtosis (6.70 versus 2.48) indicate that the supposedly "safer" diversified index actually experienced more extreme tail events during this period. This counterintuitive finding likely reflects the March 2020 crash, which affected all constituents simultaneously, producing a larger index-level shock than AAPL's company-specific volatility. The histogram analysis confirms this pattern, with the S&P 500 showing greater concentration in the near-zero and moderate positive bins but also exhibiting more extreme negative observations in the left tail.

### Co-Movement Analysis and Correlation Structure

The co-movement analysis reveals that AAPL and the S&P 500 moved in the same direction 254 weeks (81.15% of observations) and opposite directions 59 weeks (18.85%). This strong directional correlation is quantified by the correlation coefficient of 0.738, verified through manual calculation (0.736) and Excel's CORREL function. The manual covariance calculation of 0.000821 closely matches Excel's COVARIANCE.S result of 0.000824, with minor differences due to rounding. While the 81% co-movement rate indicates strong linkage to broad market movements, the 19% divergence rate is economically significant—these 59 weeks likely correspond to Apple-specific events such as product launches, earnings surprises, or regulatory developments that move the stock independently of market trends. This 19% represents the opportunity space for active stock selection to add value beyond passive index exposure.

### Regression and Beta Analysis

Regression yielded beta 1.11, alpha 0.177% weekly (9.2% annualized), and R² 54.5%. Beta above unity confirms AAPL amplifies market movements. R² reveals market explains 54.5% of variance; the remaining 45.5% represents company-specific factors—product innovation, Services growth, management decisions. This unexplained variance is where Tim Cook's leadership creates value beyond market beta.

### Beta Instability Evidence

AAPL's beta is 1.11 (five-year) but 1.20 (two-year 2023-2025)—an 8% difference reflecting genuine instability. Choudhry & Wu (2009) confirm market betas are time-varying and change asymmetrically across regimes. The 2023-2025 AI rally and volatility spikes increased market sensitivity. Beta estimates are period-dependent, not constant parameters.

---

## Question 3: Three-Stock Beta Analysis

### Methodology and Beta Estimation

The analysis examines 500 days of daily continuously compounded returns from November 7, 2023, to November 4, 2025, for three stocks spanning different sectors: JPMorgan Chase (financials), Johnson & Johnson (healthcare), and Apple (technology). Beta calculation followed the covariance-variance formula (β = Cov(r_i, r_m) / Var(r_m)), yielding betas of 0.935 for JPM, 0.028 for JNJ, and 1.204 for AAPL. Verification using Excel's SLOPE function produced identical results to eight decimal places, confirming computational accuracy. Three scatter plots with fitted trendlines visually confirm these relationships, with JPM and AAPL showing clear positive slopes and JNJ exhibiting near-zero slope.

### Sector-Specific Risk Drivers

JPMorgan's beta (0.935) is near market-neutral; R² (39.5%) indicates 60.5% is bank-specific: interest margins, credit quality, regulatory costs. JNJ's beta (0.028) and R² (0.06%) show near-complete market independence—99.94% company-specific. Healthcare demand is inelastic; returns driven by drug pipelines, FDA approvals, patent expirations. Corporate Finance Institute (2024) confirms healthcare's defensive characteristics stem from stable demand. AAPL's beta (1.204) and R² (46.9%) reflect discretionary spending sensitivity—balanced 47% systematic, 53% idiosyncratic.

### Variance Decomposition

Residual returns (ε_it = r_it - α - β×r_mt) yielded zero means for all stocks, confirming regression properties. Residual variances quantify idiosyncratic risk: JPM 0.000133, JNJ 0.000120, AAPL 0.000163. Variance decomposition (σ²_i = β²×σ²_m + σ²_ε) verified exactly, matching to ten decimals. For JPM, systematic risk is 39.5% of total; JNJ only 0.06%; AAPL 46.9%.

### Portfolio Implications

Equal-weighted portfolio declining 7.2% when market drops 10% quantifies diversification benefit—JNJ's low beta and cross-stock idiosyncratic diversification. Risk decomposition indicates optimal analysis: JNJ requires fundamental analysis (market timing irrelevant); AAPL needs both macro and micro analysis; JPM requires financial sector expertise. Quantitative Finance Stack Exchange (2024) clarifies CAPM makes no R² prediction—models can hold with low R² if volatility is idiosyncratic. Different sectors require tailored approaches based on risk composition.

---

## Conclusion

This analysis demonstrates Excel's comprehensive capabilities from text manipulation to statistical verification. NBA salary analysis revealed power law distributions and dual scarcity-star power effects. AAPL-SPX comparison exposed counterintuitive patterns—the index showed heavier tails than the stock during this extraordinary period—while confirming 45.5% of AAPL variance stems from company-specific factors. Three-stock beta analysis quantified sector characteristics, with healthcare providing diversification and technology delivering growth. Comparing Questions 2 and 3 revealed observable beta instability (1.11 vs 1.20), confirming parameters vary across periods. Excel provides computational accuracy; value lies in economic interpretation—transforming calculations into actionable insights.
