# Final Project Report: Financial Analysis (Week 1)

## 1. Task 1: Exploratory Data Analysis (EDA)
- **Dataset**: `raw_analyst_ratings.csv` (~1.4M articles).
- **Trends**: High volatility and publication spikes observed in **March 2020** (COVID-19 impact).
- **Publishers**: Top contributors include **Paul Quintaro**, **Lisa Levin**, and **Benzinga Newsdesk**.
- **Keywords**: Common financial terms like `earnings`, `eps`, `shares`, and `stocks` predominate.

## 2. Task 2: Quantitative Analysis (Technical Indicators)
- **Tools**: **TA-Lib** used for technical analysis.
- **Indicators Calculated**:
  - **Simple Moving Averages (SMA 20, 50)**: Used to identify trend direction.
  - **Relative Strength Index (RSI)**: Used to identify overbought/oversold conditions.
  - **Moving Average Convergence Divergence (MACD)**: Used for momentum analysis.
- **Results**: Indicators successfully generated and visualized for **AAPL**, **AMZN**, **GOOGL**, etc.

## 3. Task 3: Correlation Analysis (Sentiment vs. Returns)
- **Sentiment Analysis**: Used **TextBlob** to process news headlines.
- **Correlation Result (AAPL)**:
  - Found a **Pearson correlation coefficient of 0.1581** between daily news sentiment and daily stock returns.
  - Suggests a slight positive relationship, indicating that news sentiment can be a leading or coincident indicator for market movements.
- **Alignment**: Dates were normalized and aligned between the news and stock datasets to ensure accuracy.

## 4. Technical Infrastructure
- **Python Environment**: Set up with a dedicated `venv`.
- **CI/CD**: Configured GitHub Actions for automated unit testing (`unittests.yml`).
- **Organization**: Followed a modular directory structure with `src/`, `notebooks/`, and `scripts/`.

### Key Files Generated:
- `notebooks/eda_analysis.ipynb`
- `notebooks/quantitative_analysis.ipynb`
- `notebooks/correlation_analysis.ipynb`
- `results/aapl_sentiment_correlation.png`
- `results/aapl_final_analysis.csv`
