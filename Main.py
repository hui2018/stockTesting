from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import pandas


ts = TimeSeries(key='1AEF9PXLWXI8NDQ2', output_format='pandas')

#print interval
data, meta_data = ts.get_intraday(symbol='MSFT',interval='5min', outputsize='full')
#pprint(data.head(5))

#search
'''
symbol = "BA"
test = ts.get_symbol_search(symbol)
pprint(test)
'''

#print dividend amount
'''
check = ts.get_daily_adjusted(outputsize='compact', symbol='BA')
pprint(check)
'''

list = ts.get_quote_endpoint(symbol='BA')
for a in list:
    print(a["Global Quote"]["02. open"])
#print(list)


'''
ts = TimeSeries(key='1AEF9PXLWXI8NDQ2')
ts = TimeSeries(key='AEF9PXLWXI8NDQ2',output_format='pandas')
data, meta_data = ts.get_intraday('GOOGL')

print(data)
'''
