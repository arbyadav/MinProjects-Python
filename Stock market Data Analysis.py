import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time
##Python module to get stock data/cryptocurrencies from the Alpha Vantage API
##Alpha Vantage delivers a free API for real time financial data and most used finance indicators in a simple json or pandas format. This module implements a python interface to the free API provided by Alpha Vantage

api_key='7RRR3955PT3ET1UU'

ts=TimeSeries(key=api_key,output_format='pandas')
data,meta_data=ts.get_intraday(symbol='MSFT',interval='1min',outputsize='full')
print(data)

i=1

# while i==1 :
#     data,meta_data=ts.get_intraday(symbol='MSFT',interval='1min',outputsize='full')
#     data.to_excel("output.xlsx")
#     time.sleep(60)

close_data=data['4. close']

pct_chg=close_data.pct_change()

print(pct_chg)

last_chg=pct_chg[-1]

if abs(last_chg)>0.0004 :
    print('MSFT Alert :'+last_chg)