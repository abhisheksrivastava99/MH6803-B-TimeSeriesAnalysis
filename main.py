import os
import sys
import streamlit as st

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.data_utils import download_data_for_ticker, plot_close_prices ,plot_open_prices
from src.analysis_utils import test_stationarity, plot_first_difference, plot_acf_pacf, seasonal_decompose_and_plot

def main():
    st.title("Group 8- Time Series Analysis with Streamlit")

    ticker = st.text_input("Ticker symbol", "^STI")
    if 'last_ticker' not in st.session_state:
        st.session_state['last_ticker'] = None

    if st.session_state['last_ticker'] != ticker:
        for key in ['data', 'first_diff']:
            if key in st.session_state:
                del st.session_state[key]
        st.session_state['last_ticker'] = ticker
        st.info(f"Ticker changed to {ticker}. Resetting cached data.")
        
    today = datetime.today().date()
    one_year_ago = today - timedelta(days=365)

    # Use these dates in your Streamlit app:
    start_date = st.date_input("Start date", value=one_year_ago, min_value=one_year_ago)
    end_date = st.date_input("End date", value=today, max_value=today)


    if st.button("Download Data"):
        try:
            data = download_data_for_ticker(ticker, str(start_date), str(end_date))
            st.session_state['data'] = data
            st.session_state['first_diff'] = None
            st.success(f"Data downloaded for {ticker} from {start_date} to {end_date}.")
        except Exception as e:
            st.error(f"Error downloading data: {e}")

    if 'data' in st.session_state:
        data = st.session_state['data']

        # Show selectbox for user to choose next action
        step = st.selectbox("Choose analysis step to display:",
                            ["None", 
                             "Opening Prices",
                             "Closing Prices", 
                             "First Difference", 
                             "ACF and PACF",
                             "Stationarity Test" , 
                             "Seasonal Decomposition"])

        if step == "Closing Prices":
            fig = plot_close_prices(data, title=f"{ticker} Closing Prices")
            st.pyplot(fig)
            
        elif step == "Opening Prices":
            fig = plot_close_prices(data, title=f"{ticker} Opening Prices")
            st.pyplot(fig)

        elif step == "First Difference":
            fig, first_diff = plot_first_difference(data)
            st.session_state['first_diff'] = first_diff
            st.pyplot(fig)

        elif step == "ACF and PACF":
            if st.session_state.get('first_diff') is not None:
                fig = plot_acf_pacf(st.session_state['first_diff'])
                st.pyplot(fig)
            else:
                st.warning("Please generate the First Difference plot first.")

        elif step == "Seasonal Decomposition":
            fig = seasonal_decompose_and_plot(data, period=5)
            st.pyplot(fig)
        
        elif step == "Stationarity Test":
            fig, adf_res = test_stationarity(data['Close'])
            st.pyplot(fig)
            st.text(adf_res)

if __name__ == "__main__":
    main()
