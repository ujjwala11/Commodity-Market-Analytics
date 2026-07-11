# 🌎 Commodity Market Analytics: Gold, Silver, Oil, Natural Gas & Copper

## 📌 Overview

This project performs **end-to-end commodity market analysis** on major global commodities:

- 🥇 Gold
- 🥈 Silver
- 🛢️ Crude Oil
- 🔥 Natural Gas
- 🔩 Copper

The objective is to analyze historical commodity behavior, identify market patterns, study volatility, compare commodities, and extract meaningful insights using **data analytics and time-series analysis**.

The project focuses primarily on:

✅ Data cleaning & validation  
✅ Exploratory Data Analysis (EDA)  
✅ Time-series analysis  
✅ Market trend analysis  
✅ Feature engineering  
✅ Commodity comparison  

---

# 📊 Dataset

The dataset contains historical market information:

| Feature | Description |
|---|---|
| 📅 Date | Trading date |
| 🔓 Open | Opening price |
| 📈 High | Highest price of the day |
| 📉 Low | Lowest price of the day |
| 💰 Close | Closing price |
| 📊 Volume | Trading volume |

---

# 🧹 Data Preparation

Before analysis, the data pipeline handled:

### Data Cleaning

✔ Converted dates into proper datetime format  
✔ Sorted data chronologically  
✔ Checked missing values  
✔ Removed duplicate records  
✔ Validated time-series consistency  

---

### Feature Creation

Additional analytical features were generated:

### 📅 Time Features

- Year
- Month
- Quarter
- Day of Week

### 📈 Price-Based Features

- Daily Returns
- Lag Prices
    - Lag 1 day
    - Lag 7 days
    - Lag 14 days
    - Lag 30 days

### 📉 Volatility Features

- Rolling Mean
- Rolling Standard Deviation
- Volatility Indicators

### 📊 Technical Indicators

- Moving Averages
- Bollinger Bands
- RSI
- MACD
- ATR

---

# 🔎 Exploratory Data Analysis Findings

## 1️⃣ Commodity Price Trends 📈

Key observations:

- 🥇 **Gold** showed consistent long-term growth with periods of increased volatility.
- 🥈 **Silver** followed similar trends but experienced larger fluctuations.
- 🛢️ **Crude Oil** showed strong price swings influenced by market conditions.
- 🔥 **Natural Gas** had the highest volatility among analyzed commodities.
- 🔩 **Copper** displayed cyclical behavior linked to industrial demand.

---

# 2️⃣ Return Distribution Analysis 📊

Analysis of daily returns showed:

- Most daily movements were relatively small.
- Extreme price changes occurred occasionally during volatile periods.
- Commodity returns showed heavy-tail behavior instead of a perfect normal distribution.

### Key Insight:

> Commodity markets are generally stable but are affected by occasional large market movements.

---

# 3️⃣ Volatility Analysis ⚡

Rolling volatility analysis revealed:

### Findings:

1. 🔥 Natural Gas showed the highest volatility.

2. 🛢️ Crude Oil experienced frequent volatility spikes.

3. 🥇 Gold maintained comparatively lower volatility, behaving as a more stable commodity.

4. 📉 Volatility increased significantly during major market movements.

---

# 4️⃣ Moving Average Analysis 📈

Created:

- 7-day Moving Average
- 30-day Moving Average
- 50-day Moving Average

### Findings:

- Short-term moving averages captured recent momentum.
- Long-term moving averages highlighted broader market direction.
- Moving average crossovers helped identify possible trend transitions.

---

# 5️⃣ Bollinger Band Analysis 📉

Generated:

- Upper Band
- Middle Band
- Lower Band
- Band Width

### Insights:

- 📊 Wider bands indicated high-volatility periods.
- 📉 Narrow bands represented market consolidation.
- Price movements outside bands often occurred during strong market movements.

---

# 6️⃣ Historical Price Pattern Analysis 🔁

Created lag features:

- Lag 1
- Lag 7
- Lag 14
- Lag 30

### Findings:

- Previous price behavior strongly influenced current market conditions.
- Medium-term historical prices captured momentum patterns.
- Lag-based features were among the strongest analytical indicators.

---

# 7️⃣ Commodity Relationship Analysis 🔗

Cross-commodity analysis showed:

- 🥇 Gold and 🥈 Silver had similar movement patterns.
- 🔩 Copper behaved differently due to industrial demand factors.
- 🛢️ Energy commodities showed higher volatility compared to metals.

---

# 8️⃣ Seasonality Analysis 📅

Analyzed:

- Monthly trends
- Quarterly patterns
- Day-of-week effects

### Findings:

- Calendar-based patterns had limited influence.
- Price history and volatility were stronger drivers of commodity behavior.

---

# 9️⃣ Feature Engineering Pipeline ⚙️

Created features across multiple categories:

## 📈 Momentum Features

- Daily Returns
- Multi-period Returns
- Lag Features

## 📊 Trend Features

- Moving Averages
- EMA Indicators
- Price vs Moving Average

## ⚡ Volatility Features

- Rolling Volatility
- ATR
- Bollinger Band Width

## 📉 Market Condition Features

- RSI
- MACD
- Volatility Regimes

---

# 🤖 Machine Learning Exploration 

Machine learning models were explored to understand whether engineered features could capture future market behavior.

Models tested:

- Linear Regression
- Random Forest
- XGBoost

Experiments included:

- Future price prediction
- Direction classification
- Trend classification

### Findings:

- Models captured historical price patterns.
- Lag features and technical indicators provided useful signals.
- Short-term commodity forecasting remained difficult due to market randomness and external factors.



# 📌 Key Learnings

Through this project:

✅ Built a complete financial data analysis pipeline
✅ Worked with real-world time-series data
✅ Engineered financial indicators
✅ Learned challenges of financial prediction
✅ Evaluated trading strategies using risk metrics
✅ Applied quantitative analysis techniques

