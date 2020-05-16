import requests
import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    for item in obj['region']:
        print(item['region'])
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

apiKey = '1AEF9PXLWXI8NDQ2'
dataType = 'json'
symbol = 'BA'
response = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" +
                        symbol + "&apikey=" + apiKey +"&datatype=" + dataType)
#print(response.json())

obj = response.json()

print("price: " + str(obj['Global Quote']['05. price']))

'''
print("current price:" + str(obj['us']['current_price']))
print("30 day low:" + str(obj['us']['30_day_low']))
print("30 day high:" + str(obj['us']['30_day_high']))
'''


#jprint(response.json())
