import pandas as pd
import requests
from datetime import datetime

# Insert Client ID
api_key = '8ZIXHqsf0U9veOXecYhRM7NX2QTMQEeM5ogwJOw6'

# url = 'https://yfapi.net/v11/finance/quoteSummary/AAPL?lang=en&region=US&modules=summaryDetail%2C%20sectorTrend%2C%20recommendationTrend'



''' Maybe include input as a ticker and make the function use the input ticker'''

def getApiData(ticker):
    querystring = {
        "symbols": ticker,
        "lang": "en",
        "region": "US",
        "modules": "summaryDetail%2C%20sectorTrend%2C%20recommendationTrend"
    }
    url = 'https://yfapi.net/v11/finance/quoteSummary/' + ticker + '?lang=en&region=US&modules=summaryDetail%2C%20sectorTrend%2C%20recommendationTrend'
    # Request data from API
    headers = {'x-api-key': api_key}

    # HTTPS request
    # response = requests.get("GET", url, headers=headers, params=querystring)
    response = requests.get(url, params=querystring, headers=headers)
    json = response.json()

    # Verify data gathering
    if response.status_code == 200:
        print('Returned status code %s' % response.status_code)
        print('Data retrieved from yahoofinance!')
        data = json['quoteSummary']
        print(data)
        return data
    else:
        print('Error! Returned status code %s' % response.status_code)
        print('Message: %s' % json['error']['message'])
        print('Reason: %s' % json['error']['reason'])

# def getDataValues():
test = getApiData('AAPL')


print('This is a test')

df = pd.json_normalize(test)
print(df)

'''
df = pd.DataFrame(test)
for i in range(len(data)):
    row = pd.DataFrame(data[i][])
print(df)
'''
'''
df = pd.DataFrame(data)
columns = ['previousClose', 'open', 'dayLow', 'dayHigh', 'dividendRate', 'dividendYield',
           'payoutRatio', 'fiveYearAvgDividendYield', 'fiftyTwoWeekLow', 'fiftyTwoWeekHigh',
           'fiftyDayAverage', 'twoHundredDayAverage']
df2 = df[columns].copy()
'''

# Use pandas library to insert the observation data into a table format.
# print(data)
# Return a Dataframe with all of the observation in a table format
# dataframe = pd.DataFrame()
# df = pd.DateTime()
'''
columns = ['dayHigh', 'fiftyDayAverage']
# df2 = df[columns].copy()

print(columns)
'''
'''
inputdata ={}
valueList = []
  valueList.extend(inputdata["quoteSummary"]["result"][0]["SummaryDetail"]["dayHigh"][0]["fmt"])
  valueList.extend(inputdata["quoteSummary"]["result"][0]["SummaryDetail"]["fiftyDayAverage"][0]["fmt"])
'''

####################################################
'''
if "dayHigh": > "fiftyDayAverage": 
 print('bull')
 else
 print('bear')
'''

