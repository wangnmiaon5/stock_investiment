################################################
# 2018 stock investment
################################################


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
from pandas_datareader import data


os.chdir('/Users/miaowang/Box Sync/2017DS/stock_investment_2018')
os.chdir('/Users/yipan/Desktop/stock_investment')

############################################
#### get the stock price from google finance
############################################
tickers = ['AMTD']
# Define which online source one should use
data_source = 'google'
start_date = '2008-01-01'
end_date = '2018-3-10'
panel_data = data.DataReader(tickers, data_source, start_date, end_date)
# Getting just the adjusted closing prices. This will return a Pandas DataFrame
# The index in this DataFrame is the major index of the panel_data.
close = panel_data.ix['Close']
# Getting all weekdays between 01/01/2000 and 12/31/2016
all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
# All we need to do is reindex close using all_weekdays as the new index
close = close.reindex(all_weekdays)
def get_year(x):
    return x.date().year
close['date'] = close.index
close['year'] = close['date'].apply(get_year)
price = close.groupby(['year']).median()
price.index = pd.PeriodIndex(price.index, freq='A-SEP')


############################################
#### get fundamental data from gm package
############################################
import good_morning as gm
dir(gm)
kr = gm.KeyRatiosDownloader()
kr_frames = kr.download('AMTD')
data1 = kr_frames[0].T
data1.index = data1.index.values.astype(str)
data2 = kr_frames[1].iloc[kr_frames[1].index.get_loc('EBT Margin')]
data2.index = data2.index.values.astype(str)

data = data1.join(price, how='outer')
price.index = pd.PeriodIndex(start='2008', end='2018', freq='A')


def join_dfs(ldf, rdf):
    return ldf.join(rdf, how='inner')

final_df = reduce(join_dfs, data) #that's the magic
final_df.head()

data.T
data2.index
month['Fund'] = month.index

to_del = perf2.loc[perf2['Fund'].isin(drop_list)].index.tolist()

data1['2020'] = (data1['2018']/data1['2008'])**(1/(2018.00-2008.00-1))-1

print (data2.index=='Revenue')

data2.iloc[data2.index.get_loc('Revenue')]



data2.get_loc('Renenue')

data1 = kr_frames[0].T[['Book Value Per Share * USD', 
                 'Free Cash Flow USD Mil', 
                 'Free Cash Flow Per Share * USD',
                 'Dividends USD',
                 'Earnings Per Share USD', 
                 'Shares Mil',
                 'Payout Ratio % *',
                 'EBT Margin']]


pd.concat(data1,data2)



pieces = [df[:3], df[3:7], df[7:]]

In [4]: concatenated = concat(pieces)


df = df.assign(delta_A=np.zeros(len(df.A)))
df['delta_A'][0] = 0  # start at 'no-change'
df['delta_A'][1:] = df.A[1:].values - df.A[:-1].values




df.reindex(df.index.drop(1))


data1.columns = data1.index

data1.reset_index(drop=False, inplace=True)

df.reset_index().T
data = data1.reset_index(drop=False, inplace=True)
data.T

kr2 = gm.FinancialsDownloader()
kr_fins = kr2.download('AMTD')



month = perf.groupby(['Fund', '1M breach']).size().reset_index(name='counts').pivot(index = 'Fund', columns = '1M breach', values = 'counts')




