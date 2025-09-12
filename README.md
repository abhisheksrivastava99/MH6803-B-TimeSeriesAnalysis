# MH6803-B-TimeSeriesAnalysis
# Time Series Analysis Streamlit App

Interactive analysis and visualization of financial time series data using Streamlit.  
Download price data for any ticker, perform key transformations and generate statistical plots—all in an intuitive web app.

## Features

- Fetch historical price data for any Yahoo Finance ticker using `yfinance`
- Explore **opening** and **closing prices** with dynamic charts
- Compute and visualize the **first difference** to analyze returns
- Plot **autocorrelation (ACF) and partial autocorrelation (PACF)**
- Perform the **Augmented Dickey-Fuller test** for stationarity with automatic summary
- Run **seasonal decomposition** to separate trend and seasonality
- Fully interactive analysis via Streamlit UI

## Project Structure

```.
├── main.py
├── dict_file.csv
├── requirements.txt
└── src/
    ├── __init__.py
    ├── analysis_utils.py
    └── data_utils.py
```


## Usage

1. Enter a ticker symbol (e.g., `^STI`, `AAPL`, `GOOGL`).
2. Select a start date and end date for your analysis.
3. Click **Download Data** to fetch prices.
4. Choose an analysis step; visualizations/results appear instantly.
   
**Deploy and explore financial time series data interactively, right in your browser!**
