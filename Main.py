from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import pandas

ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
pprint(data.head(2))

'''
ts = TimeSeries(key='1AEF9PXLWXI8NDQ2')
ts = TimeSeries(key='AEF9PXLWXI8NDQ2',output_format='pandas')
data, meta_data = ts.get_intraday('GOOGL')

print(data)
'''
