import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
import statsmodels.api as sm
import pandas as pd

def plot_first_difference(data, column='Close', title="First Difference of Closing Prices", figsize=(14, 7)):
    first_diff = data[column].diff().dropna()
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(first_diff.index, first_diff)
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Difference')
    plt.tight_layout()
    plt.close(fig)
    return fig, first_diff


def test_stationarity(timeseries, rolling_window=12, figsize=(12, 6), title='Rolling Mean and Standard Deviation'):
    """
    Plots rolling mean and std deviation and performs the Augmented Dickey-Fuller test.

    Parameters:
    - timeseries: pandas Series of the time series data to test
    - rolling_window: window size for rolling mean/std calculation (default 12)
    - figsize: figure size tuple for the plot
    - title: title for the plot

    Returns:
    - fig: matplotlib figure with rolling stats plotted
    - adf_result_str: formatted string of ADF test results for display
    """
    rolmean = timeseries.rolling(rolling_window).mean()
    rolstd = timeseries.rolling(rolling_window).std()

    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(timeseries, color='blue', label='Original')
    ax.plot(rolmean, color='red', label=f'Rolling Mean ({rolling_window})')
    ax.plot(rolstd, color='black', label=f'Rolling Std ({rolling_window})')
    ax.legend(loc='best')
    ax.set_title(title)
    plt.tight_layout()
    plt.close(fig)

    adft = adfuller(timeseries, autolag='AIC')
    output = pd.Series(adft[0:4], index=['Test Statistic', 'p-value', 'Used Lag', 'Number of Observations Used'])
    for key, val in adft[4].items():
        output[f'Critical Value ({key})'] = val

    adf_result_str = "Results of Dickey-Fuller Test:\n" + output.to_string()

    return fig, adf_result_str
    

def plot_acf_pacf(data, lags=40, title_prefix='STI Daily Returns (First Difference)', figsize=(14, 10)):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=figsize)

    sm.graphics.tsa.plot_acf(data, lags=lags, ax=ax1)
    ax1.set_title(f'Autocorrelation of {title_prefix}')
    ax1.set_xlabel('Lag')
    ax1.set_ylabel('Autocorrelation')

    sm.graphics.tsa.plot_pacf(data, lags=lags, ax=ax2)
    ax2.set_title(f'Partial Autocorrelation of {title_prefix}')
    ax2.set_xlabel('Lag')
    ax2.set_ylabel('Partial Autocorrelation')

    plt.tight_layout()
    plt.close(fig)
    return fig
    
def seasonal_decompose_and_plot(data, column='Close', model='multiplicative', period=5, figsize=(12, 8)):
    decomposition = sm.tsa.seasonal_decompose(data[column], model=model, period=period)
    fig = decomposition.plot()
    fig.set_size_inches(*figsize)
    plt.tight_layout()
    plt.close(fig)
    return fig
