import requests
import pprint

# Insert Client ID
# Limited to 100 API-calls per day
api_key = '8ZIXHqsf0U9veOXecYhRM7NX2QTMQEeM5ogwJOw6'

class GetRichorDieTrying:

    def __init__(self):
        pass

    # Returns data as json file containing data from YahooFinance API
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
            print(data)
            return data
        else:
            print('Error! Returned status code %s' % response.status_code)
            print('Message: %s' % file['error']['message'])
            print('Reason: %s' % file['error']['reason'])
            quit()

    # Return requested key value
    # Input is the API-data and requested key
    # Checking that the value exists and is an integer
    def getCompanyValues(self, data, key):
        try:
            value = int(data['result'][0]['summaryDetail'][key]['raw'])
        except ValueError:
            print('The data is not an integer, and something is wrong')
        else:
            pass
        return value

    # Return percentage change between two compared data point values
    # Inputs are two separate data point values
    def getTrend(self, value1, value2):
        value3 = (value1 - value2) * 100 / value2
        return value3

    # Print data set
    # Input is data set from getApiData
    def printData(self, data):
        # Ask if want to see
        # Pretty print of json data
        pp = pprint.PrettyPrinter(indent=2, compact=True, sort_dicts=True)
        return pp.pprint(data)



# abc = GetRichorDieTrying()
# print(abc)
# print(abc.getApiData('MSFT'))


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
# a = abc.getApiData('AAPL')
# b = abc.getCompanyValues(a,'dayHigh')
# c = abc.getCompanyValues(a,'fiftyDayAverage')
# d = abc.getTrend(b,c)
# e = abc.printData(a)








########################################################################
########################################################################
############################ USER INTERFACE ############################
########################################################################
########################################################################

data = {'result': [{'summaryDetail': {'maxAge': 1, 'priceHint': {'raw': 2, 'fmt': '2', 'longFmt': '2'}, 'previousClose': {'raw': 147.87, 'fmt': '147.87'}, 'open': {'raw': 148.43, 'fmt': '148.43'}, 'dayLow': {'raw': 147.48, 'fmt': '147.48'}, 'dayHigh': {'raw': 150.09, 'fmt': '150.09'}, 'regularMarketPreviousClose': {'raw': 147.87, 'fmt': '147.87'}, 'regularMarketOpen': {'raw': 148.43, 'fmt': '148.43'}, 'regularMarketDayLow': {'raw': 147.48, 'fmt': '147.48'}, 'regularMarketDayHigh': {'raw': 150.09, 'fmt': '150.09'}, 'dividendRate': {'raw': 0.88, 'fmt': '0.88'}, 'dividendYield': {'raw': 0.006, 'fmt': '0.60%'}, 'exDividendDate': {'raw': 1636070400, 'fmt': '2021-11-05'}, 'payoutRatio': {'raw': 0.1515, 'fmt': '15.15%'}, 'fiveYearAvgDividendYield': {'raw': 1.22, 'fmt': '1.22'}, 'beta': {'raw': 1.205714, 'fmt': '1.21'}, 'trailingPE': {'raw': 26.707664, 'fmt': '26.71'}, 'forwardPE': {'raw': 24.362602, 'fmt': '24.36'}, 'volume': {'raw': 43794897, 'fmt': '43.79M', 'longFmt': '43,794,897'}, 'regularMarketVolume': {'raw': 43794897, 'fmt': '43.79M', 'longFmt': '43,794,897'}, 'averageVolume': {'raw': 75599481, 'fmt': '75.6M', 'longFmt': '75,599,481'}, 'averageVolume10days': {'raw': 58403325, 'fmt': '58.4M', 'longFmt': '58,403,325'}, 'averageDailyVolume10Day': {'raw': 58403325, 'fmt': '58.4M', 'longFmt': '58,403,325'}, 'bid': {'raw': 149.82, 'fmt': '149.82'}, 'ask': {'raw': 149.83, 'fmt': '149.83'}, 'bidSize': {'raw': 1000, 'fmt': '1k', 'longFmt': '1,000'}, 'askSize': {'raw': 1200, 'fmt': '1.2k', 'longFmt': '1,200'}, 'marketCap': {'raw': 2458170949632, 'fmt': '2.46T', 'longFmt': '2,458,170,949,632'}, 'yield': {}, 'ytdReturn': {}, 'totalAssets': {}, 'expireDate': {}, 'strikePrice': {}, 'openInterest': {}, 'fiftyTwoWeekLow': {'raw': 112.59, 'fmt': '112.59'}, 'fiftyTwoWeekHigh': {'raw': 157.26, 'fmt': '157.26'}, 'priceToSalesTrailing12Months': {'raw': 6.7196736, 'fmt': '6.72'}, 'fiftyDayAverage': {'raw': 146.44305, 'fmt': '146.44'}, 'twoHundredDayAverage': {'raw': 141.07277, 'fmt': '141.07'}, 'trailingAnnualDividendRate': {'raw': 0.85, 'fmt': '0.85'}, 'trailingAnnualDividendYield': {'raw': 0.005748293, 'fmt': '0.57%'}, 'navPrice': {}, 'currency': 'USD', 'fromCurrency': None, 'toCurrency': None, 'lastMarket': None, 'volume24Hr': {}, 'volumeAllCurrencies': {}, 'circulatingSupply': {}, 'algorithm': None, 'maxSupply': {}, 'startDate': {}, 'tradeable': False}}], 'error': None}


