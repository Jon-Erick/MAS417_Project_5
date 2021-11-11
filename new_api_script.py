import requests
import pprint

# Insert Client ID
api_key = '8ZIXHqsf0U9veOXecYhRM7NX2QTMQEeM5ogwJOw6'

print('What company, what to compare')
print('all the possible value: dayHigh compared to fifty day average ')


class GetRichorDieTrying:

    def __init__(self):
        pass

    # Returns json file containing data from YahooFinance API
    # Input is stock ticker to requested company
    def getApiData(self, ticker):
        # query parameters for API
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
        # requests library
        response = requests.get(url, params=querystring, headers=headers)
        # format data to json
        file = response.json()
        # Exception handling
        if response.status_code == 200:
            print('Returned status code %s' % response.status_code)
            print('Data retrieved from yahoofinance!')
            # retrieved json-file
            data = file['quoteSummary']
            return data
        else:
            print('Error! Returned status code %s' % response.status_code)
            print('Message: %s' % file['error']['message'])
            print('Reason: %s' % file['error']['reason'])
            quit()

    # Return requested data point value
    # Inputs are data set from getApiData and requested data point
    def getCompanyValues(self, data, value):
        return data['result'][0]['summaryDetail'][value]['raw']

    # Return percentage change between two compared data point values
    # Inputs are two separate data point values
    def getTrend(self, value1, value2):
        return (value1 - value2) * 100 / value2

    # Print data set
    # Input is data set from getApiData
    def printData(self, data):
        # Ask if want to see
        # Pretty print of json data
        pp = pprint.PrettyPrinter(indent=2, compact=True, sort_dicts=True)
        return pp.pprint(data)



abc = GetRichorDieTrying()
print(abc)
print(abc.getApiData('M123'))


# Make a test to verify if the recieved dict includes error or not. Expanding the getApiData exception handling.!!
# def checkDataOutput(output):
  #  if ['result'][0] == 'None' not output:
        # pass

# Exception handling for input. Verify string, not int or wrong ticker
# def checkInput(ticker):
    # if ticker == string # and valid ticker
        # pass



# print('dayHigh,fiftyDayAverage, chogi chogi.....')
# print('first value to compare')

#b = abc.getCompanyValues(a,'dayHigh')
#c = abc.getCompanyValues(a,'fiftyDayAverage')
#d = abc.getTrend(b,c)
#e = abc.printData(a)