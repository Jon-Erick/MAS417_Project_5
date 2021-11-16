
# Return yes or no as a string
def yesNo():
    i = 1
    print('yes or no?')
    while True:
        i = i + 1
        list = ['yes', 'no']
        a = input('')
        if i > 3:
            print('Do you want to quit? yes or no')
            b = input('')
            if b == 'yes':
                print('Quitting process')
                quit()
            i = 0

        if a not in list:
            print('Please enter yes or no')
            continue
        elif a == 'yes':
            break
        elif a == 'no':
            break
    return a


# Return requested key to compare data values
# Input is data from getApiData
# Checks for a valid key in data
def chooseKey(data):
    while True:
        print('What instrumental values do you want to compare?')
        print('Choose between: dayHigh, dayLow, open, fiftyDayAverage, fiftyTwoWeekHigh, fiftyTwoWeekLow, previousClose and twoHundredDayAverage')
        key = input('')
        if key not in data['result'][0]['summaryDetail']:
            print('Please enter a valid key')
            continue
        else:
            break
    return key




