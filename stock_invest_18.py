################################################
# 2018 stock investment
################################################

from yahoo_finance import Share

dir(Share)

yahoo = Share('GILD')
print (yahoo.get_open())
print (yahoo.get_price())
print (yahoo.get_trade_datetime())


from yahoo_finance import Share as sh 
st = sh ('NFLX') 
print (st.get_historical('2017-05-01', '2017-05-12'))


################ how to download repository from github then install into python
"""
cd Box\ Sync/2017DS/stock_investment_2018/
git clone https://github.com/petercerno/good-morning.git
cd your-local-repo
pip install -e .
reference: https://github.com/petercerno/good-morning
"""
import os
import numpy as np
import pandas as pd
import datetime

os.chdir('/Users/yipan/Desktop/stock_investment')
import good_morning as gm
dir(gm)
kr = gm.KeyRatiosDownloader()
kr_frames = kr.download('AMTD')
print (kr_frames[0])

kr = gm.FinancialsDownloader()
kr_fins = kr.download('AAPL')


from pandas_datareader import data

from pandas_datareader import data
import pandas as pd


# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', 'SPY']

# Define which online source one should use
data_source = 'google'

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2000-01-01'
end_date = '2018-3-10'

# User pandas_reader.data.DataReader to load the desired data. As simple as that.
panel_data = data.DataReader(tickers, data_source, start_date, end_date)


# Getting just the adjusted closing prices. This will return a Pandas DataFrame
# The index in this DataFrame is the major index of the panel_data.
close = panel_data.ix['Close']

# Getting all weekdays between 01/01/2000 and 12/31/2016
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')

# How do we align the existing prices in adj_close with our new set of dates?
# All we need to do is reindex close using all_weekdays as the new index
close = close.reindex(all_weekdays)

close.describe()


