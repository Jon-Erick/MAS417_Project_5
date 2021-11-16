

import new_api_script as API
import STL_image as IMG
import ancillary_functions as AF


print('Do you want to run a default procedure?')
default = AF.yesNo()

if default == 'yes':

    # Default

    # API script
    print('Gathering data from Microsoft')
    ticker = 'MSFT'
    data = API.GetRichorDieTrying.getApiData(1,ticker)
    print('Comparing day high and fifty day average values')
    value1 = API.GetRichorDieTrying.getCompanyValues(1, data, 'dayHigh')
    value2 = API.GetRichorDieTrying.getCompanyValues(1, data, 'fiftyDayAverage')
    trend = API.GetRichorDieTrying.getTrend(1, value1, value2)
    print('day high:', value1, 'fifty day average:',  value2, 'percentage trend:', trend)
    print('Printing data')
    seedata = API.GetRichorDieTrying.printData(1,data)


    # STL script
    updown = IMG.bullOrBear(trend)
    print('The trend is', updown)
    print('Greyscaling', updown, 'image')
    grey = IMG.greyScaleImage(updown)
    print('Generating height map using trend amplitude')
    matrix = IMG.createImageMatrix(grey, trend)
    print('Tessellating height map')
    triangle = IMG.matrixProcessTriangles(matrix[0], matrix[1], matrix[2])
    print('Meshing processed image to generate a STL-file')
    mesh = IMG.createSTLMesh(triangle[0], triangle[1], ticker)


else:
    # User choice
    # API script

    print('Enter your preferred company ticker from the New York Stock Exchange')
    print('Suggestion for some tickers: Apple = AAPL, Microsoft = MSFT, Tesla = TSLA')
    print('Advanced Micro Devices = AMD, Amazon = AMZN, NVIDIA Corporation = NVDA, etc.')
    ticker = input('')
    print('Gathering data from', ticker)
    data = API.GetRichorDieTrying.getApiData(1, ticker)
    test = data.get('result')
    # Test for valid ticker
    if test == None:
        print('invalid ticker entered')
        quit()
    print('First instrument')
    key1 = AF.chooseKey(data)
    print('Second instrument')
    key2 = AF.chooseKey(data)
    # Test input
    if key1 == key2:
        print('Try again.')
        key2 = AF.chooseKey(data)


    print('Comparing', key1, 'and', key2)
    value1 = API.GetRichorDieTrying.getCompanyValues(1, data, key1)
    value2 = API.GetRichorDieTrying.getCompanyValues(1, data, key2)
    trend = API.GetRichorDieTrying.getTrend(1, value1, value2)
    print(key1,':', value1,',', key2,':', value2,',', 'percentage trend:', trend)

    print('Do you want to see the collected company data? yes or no?')
    seedata = AF.yesNo()
    if seedata == 'yes':
        API.GetRichorDieTrying.printData(1, data)


    # STL script
    updown = IMG.bullOrBear(trend)
    print('The trend is', updown)
    print('Greyscaling', updown, 'image')
    grey = IMG.greyScaleImage(updown)
    print('Generating height map using trend amplitude')
    matrix = IMG.createImageMatrix(grey, trend)
    print('Tesselating height map')
    triangle = IMG.matrixProcessTriangles(matrix[0], matrix[1], matrix[2])
    print('Meshing processed image to generate a STL-file')
    mesh = IMG.createSTLMesh(triangle[0], triangle[1], ticker)

print('The script finished successfully!')




