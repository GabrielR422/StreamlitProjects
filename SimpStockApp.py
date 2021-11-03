import yfinance as yf
import streamlit as st
import pandas as pd
# import cufflinks as cf
import datetime

st.write("""
# Stock Price
""")

st.write('---')


# Sidebar
st.sidebar.subheader('Parameters')
start_date = st.sidebar.date_input("Start date", datetime.date(2021, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date.today())

ticker_list = pd.read_csv("StocksSymbols.csv")
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol
tickerData = yf.Ticker(tickerSymbol) # Get ticker data
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) #get the historical prices for this ticker

# Ticker information
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

string_industry = tickerData.info['industry']
st.write('**%s**' % string_industry)


st.header('**Close Price**')
st.line_chart(tickerDf.Close)

st.header('**Volume**')
st.line_chart(tickerDf.Volume)