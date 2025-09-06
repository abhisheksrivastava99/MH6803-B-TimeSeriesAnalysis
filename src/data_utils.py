import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt

def download_data_for_ticker(ticker_symbol, start_date, end_date):
    print(f"Downloading data for {ticker_symbol} from {start_date} to {end_date}...")
    data = yf.download(ticker_symbol, start=start_date, end=end_date)
    print("Missing values in the dataset:")
    print(data.isnull().sum())
    return data


def plot_close_prices(data, title="Closing Prices", figsize=(14, 7)):
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(data.index, data['Close'])
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.tight_layout()
    plt.close(fig)
    return fig

def plot_open_prices(data, title="Opening Prices", figsize=(14, 7)):
    fig = plt.figure(figsize=figsize)
    data['Open'].plot()
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.tight_layout()
    plt.close(fig)
    return fig