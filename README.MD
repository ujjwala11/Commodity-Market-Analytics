# 📊 Commodity Market Analytics Dashboard

## Overview

A comprehensive exploratory data analysis and risk analytics project analyzing **Gold, Silver, Crude Oil, Natural Gas, and Copper** markets from **2015–2026**.

The project focuses on understanding:

- 📈 Long-term commodity performance
- 📉 Risk and volatility behavior
- 🔄 Commodity relationships and correlations
- ⚠️ Market shocks and tail risks
- 📊 Risk-adjusted investment performance

The goal was not only to compare returns, but to understand **which commodities provide sustainable growth, stability, diversification benefits, and how market behavior changes during extreme events.**

---

# 📂 Dataset Scope

**Commodities analyzed:**

| Commodity |
|-----------|
| 🟡 Gold |
| ⚪ Silver |
| 🛢️ Crude Oil |
| 🔥 Natural Gas |
| 🟠 Copper |

**Time Period:** 2015–2026

---

# 🛠️ Data Processing & Preparation

The project included:

### Data Cleaning
- Loaded and validated multiple commodity datasets
- Checked missing values and data consistency
- Handled date indexing and chronological ordering
- Verified extreme market events present in the raw data

### Feature Engineering

Created market analytics features:

### Price Features
- Open
- High
- Low
- Close
- Trading Volume

### Return Features
- Daily returns
- Cumulative returns
- Future returns
- Multi-period returns

### Trend & Momentum Indicators
- Lag features
- Moving averages
- Rolling mean
- Rolling standard deviation
- Bollinger Bands
- EMA indicators
- RSI
- MACD

### Risk Metrics
- Rolling volatility
- Maximum drawdown
- Drawdown curves
- Rolling Sharpe Ratio
- Sortino Ratio
- Value at Risk (VaR)

---

# 🔎 Exploratory Data Analysis Findings

## 1. Commodity Performance Comparison

| Commodity | Total Return | CAGR | Annualized Volatility | Sharpe Ratio |
|---|---:|---:|---:|---:|
| 🥈 Silver | 280.13% | 12.29% | 33.42% | 0.52 |
| 🥇 Gold | 246.05% | 11.38% | 16.53% | 0.74 |
| 🟠 Copper | 119.61% | 7.07% | 24.27% | 0.40 |
| 🛢️ Crude Oil | 35.53% | 2.67% | 108.28% | -0.18 |
| 🔥 Natural Gas | -2.10% | -0.18% | 66.50% | 0.33 |

### Key Insights

1. **Silver generated the highest raw return**
   - Total return: **280.13%**
   - CAGR: **12.29%**

2. **Gold delivered the strongest risk-adjusted performance**
   - Highest Sharpe Ratio: **0.74**
   - Lowest volatility among commodities: **16.53%**

3. **Natural Gas was the weakest performer**
   - Negative total return: **-2.10%**
   - High volatility: **66.50%**

4. **Crude Oil displayed extreme instability**
   - Volatility exceeded **100%**
   - Sharpe Ratio was negative (**-0.18**)

---

# 📈 Historical Price Behavior

## Gold 🟡

- 2015–2019:
  - Range-bound around **$1,000–$1,400**

- 2020–2023:
  - Gradual rise toward **$1,600–$2,000**

- 2024–2026:
  - Strong bull run above **$5,000**
  - Later correction toward **$4,000**

**Observation:**
Gold demonstrated the strongest long-term trend consistency.

---

## Silver ⚪

- Consolidated between **$14–$20** (2015–2019)
- Recovery after COVID shock
- Reached approximately **$115 before correction**

**Observation:**
Silver amplified gold movements but with significantly higher volatility.

---

## Crude Oil 🛢️

- Normal range:
  - **$30–$80**

- April 2020:
  - Historic collapse to approximately **-$40**

- Recovery:
  - Rose above **$120** during 2021–2022

**Observation:**
Oil is highly cyclical and event-driven.

---

## Natural Gas 🔥

- Stable period:
  - **$2–$4**

- Energy crisis spike:
  - Near **$10**

- Large correction afterward

**Observation:**
Natural gas behaves more like a shock-driven market rather than a trend-following asset.

---

## Copper 🟠

- Stable:
  - **$2–$3.50**

- Industrial demand rally:
  - Around **$5**

- Structural growth:
  - Above **$6.50**

**Observation:**
Copper showed long-term structural growth characteristics.

---

# 📊 Moving Average Analysis

Analyzed:

- 30-day moving average
- 90-day moving average


| Commodity | Trend Behavior |
|-|-|
| Gold | Strong bullish structure |
| Silver | Bullish but noisy |
| Copper | Smooth structural growth |
| Crude Oil | Highly cyclical |
| Natural Gas | Mean reverting |


### Findings

- Gold maintained clean MA30 > MA90 behavior.
- Copper showed strong long-term support.
- Silver produced frequent crossover signals.
- Oil and natural gas experienced frequent regime changes.

---

# ⚠️ Return Distribution & Tail Risk

## Daily Return Statistics

| Commodity | Daily Volatility | Worst Day | 95% VaR |
|-|-:|-:|-:|
| Gold | 1.04% | -11.37% | -1.62% |
| Silver | 2.10% | -31.35% | -3.06% |
| Crude Oil | 6.82% | -305.97% | -4.05% |
| Natural Gas | 4.19% | -47.48% | -6.12% |
| Copper | 1.53% | -22.25% | -2.34% |

---

## Stability Ranking

Most stable → Least stable

1. 🥇 Gold
2. 🥈 Copper
3. Silver
4. Natural Gas
5. Crude Oil


## Tail Risk Ranking

Highest → Lowest

1. Crude Oil
2. Natural Gas
3. Silver
4. Copper
5. Gold


### Key Finding

Commodity returns were **not normally distributed**.

All markets displayed:

- Heavy tails
- Extreme events
- Market shocks
- Non-linear risk behavior

---

# 📉 Rolling Volatility Analysis

Average 30-day volatility:

| Commodity | Average Volatility | Maximum |
|-|-:|-:|
| Natural Gas | 59.53% | 228.40% |
| Crude Oil | 47.45% | 985.01% |
| Silver | 29.39% | 137.48% |
| Copper | 22.94% | 79.60% |
| Gold | 15.24% | 48.79% |

### Insights

- Gold remained the most stable commodity.
- Natural Gas had the highest sustained volatility.
- Crude Oil volatility was dominated by the 2020 negative-price event.

---

# 🔗 Commodity Correlation Analysis

## Static Correlations

| Relationship | Correlation |
|-|-:|
| Gold–Silver | 0.77 |
| Silver–Copper | 0.40 |
| Gold–Copper | 0.28 |


### Findings

### Gold & Silver

Correlation:

**0.77**

- Strong relationship
- Similar precious metal drivers


### Silver & Copper

Correlation:

**0.40**

- Explained by silver's industrial usage


### Energy vs Metals

Crude Oil showed near-zero correlation with metals.

Natural Gas had the weakest relationships.

---

# 📉 Risk Analytics

## Maximum Drawdown

| Commodity | Maximum Drawdown |
|-|-:|
| Gold | -24.97% |
| Copper | -35.64% |
| Silver | -49.56% |
| Natural Gas | -83.73% |
| Crude Oil | -149.25% |


## Findings

1. Gold had the lowest downside risk.
2. Silver experienced deeper corrections despite higher returns.
3. Natural Gas suffered prolonged drawdowns.
4. Crude Oil experienced extreme downside due to the 2020 negative-price event.

---

# 📈 Rolling Sharpe Ratio Analysis

Findings:

### Gold
- Highest average rolling Sharpe
- Most consistent risk-adjusted performance

### Silver
- Strong short-term periods
- Higher volatility reduced consistency

### Copper
- Stable moderate performance

### Natural Gas
- Highly inconsistent

### Crude Oil
- Weakest risk-adjusted performance

---

# 📊 Sortino Ratio Analysis

Sortino Ratio evaluates returns against downside risk only.

Findings:

🥇 Gold:
- Best downside-adjusted performance

🥈 Copper:
- Balanced risk/reward

🥉 Silver:
- Strong returns but larger downside swings

🔥 Natural Gas:
- High downside exposure

🛢️ Crude Oil:
- Negative Sortino ratio

---

# 🤖 Machine Learning Experiment (Secondary)

A small predictive modeling experiment was conducted to explore whether historical market features could predict future movements.

Models tested:

- Logistic Regression
- Random Forest
- XGBoost

Tasks explored:

- Future return prediction
- Direction classification
- Trend classification

Features used:

- Lag prices
- Rolling statistics
- Volatility indicators
- Bollinger Bands
- Momentum indicators

The ML results showed that commodity movement is highly noisy and difficult to predict consistently.

The project therefore focuses primarily on:

✅ Exploratory Analytics  
✅ Risk Analysis  
✅ Market Understanding  

rather than predictive modeling.

---

# 💡 Final Business Insights

## Best Risk-Adjusted Commodity

🥇 **Gold**

Reasons:

- Highest Sharpe Ratio: **0.74**
- Lowest volatility
- Lowest maximum drawdown
- Strong long-term appreciation


---

## Highest Growth Potential

🥈 **Silver**

Reasons:

- Highest total return: **280.13%**
- Highest CAGR: **12.29%**

Tradeoff:

- Almost double gold's volatility
- Larger drawdowns


---

## Balanced Industrial Commodity

🟠 **Copper**

Characteristics:

- Moderate return
- Moderate volatility
- Structural growth linked to industrial demand


---

## Diversification Asset

🛢️ **Crude Oil**

Characteristics:

- Low correlation with metals
- Useful diversification role

Risk:

- Extreme downside events


---

## Most Event Driven Market

🔥 **Natural Gas**

Characteristics:

- Highest volatility
- Weak correlations
- Poor long-term return consistency



# Conclusion

This project demonstrates that commodity analysis requires more than comparing returns.

Through performance analysis, volatility measurement, correlation analysis, drawdown analysis, and risk-adjusted metrics:

- Gold emerged as the most reliable long-term asset.
- Silver delivered superior returns with higher risk.
- Copper represented balanced industrial growth.
- Energy commodities showed extreme sensitivity to shocks.

The analysis highlights why **risk-adjusted evaluation and dynamic market analysis are essential when studying commodity markets.**
