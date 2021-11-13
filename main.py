import new_api_script
import STL_image


############################
########## STEP 1 ##########
############################

print('Choose your preferred company to compare instrumental values')
print("Insert company ticker, such as AAPL for Apple, or MSFT for Microsoft")
ticker = input('')

print(ticker)
print(type(ticker))

# function call getApiData
# b = getApiData(ticker)


############################
########## STEP 2 ##########
############################
# Find a way to say what value to be compared to the other


# Return requested key to compare data values
# Input is data from getApiData
# Checks for a valid key in data
def chooseKey(data):
    while True:
        print('What instrumental values do you want to be compared to?')
        print('Choose between: dayHigh, dayLow, open, fiftyDayAverage, fiftyTwoWeekHigh, fiftyTwoWeekLow, previousClose and twoHundredDayAverage')
        key = input('')
        if key not in data['result'][0]['summaryDetail']:
            print('Please enter a valid key')
            continue
        else:
            break
    return key

# Call chooseKey function to check for a valid
# c = chooseKey(data)

# Call function getCompanyValues for the first instrument key
# d = getCompanyValues(data, c)

############################
########## STEP 3 ##########
############################

print('What instrumental value to you want to compare to?')
print('Choose between: dayHigh, dayLow, open')

# Call chooseKey function to check for a valid key
# e = chooseKey(data)

# Call function getCompanyValues for the second instrument
# f = getCompanyValues(data, e)


# Return requested key value
# Input is the API-data and requested key
# Checking that the value exists and is an integer
def getCompanyValues(data, key):
    try:
        value = int(data['result'][0]['summaryDetail'][key]['raw'])
    except ValueError:
        print('The data is not an integer, and something is wrong')
    else:
        pass
    return value


############################
########## STEP 4 ##########
############################

# Call function getTrend


# Return yes or no if want to see the percentage trend.
# Or can retrun the percentage diretly by calling the getTrend function if want to
# NOT FINISHED
def seeTrend():
    print('Do you want to see the percentage change trend between the two compared values? yes or no?')
    while True:
        try:
            ans = input('')
        except ValueError:
            print('please enter yes or no')
            continue
        else:
            break
    # return getTrend(value1, value2)
    return ans
    # This can be implemented to directly call the getTrend function if the answear is yes
    # input in getTrend must be the key value from the getCompanyValue calls
    # if ans == 'yes':
    #    return getTrend(value1, value2)
    # else:
    #    pass


if seeTrend == 'yes':
    print(getTrend())
else:
    pass

############################
########## STEP 5 ##########
############################

print('Do you want to see the avaiable instrumental data from the company', ticker, '?', 'yes or no?')
seeData = input('')
# print(seeData)

if seeData == 'yes':
    fff = aaa.printData(bbb)
elif seeData == 'no':
    pass
else:
    print('Please enter "yes" or "no"')


