#Open Weather Map API
import json
import requests
import datetime

def getWeatherData():
    #api key from openweather 
    api_key = "886f6a4c98d1b377418e02affd7ede7a"

    #lat/long of Syracuse
    lat = 43.0481
    long = -76.1474

    #to record date and time of when data were collect
    date_time = datetime.datetime.now()

    #to round seconds to then nearest whole number
    #cast date_time to str
    item = str(date_time)
    
    #take out date and time seperately and split hour, mintues and second
    date = item.split()[0]
    time = item.split()[1]
    hours = time.split(':')[0]
    mins = time.split(':')[1]

    #round the second
    secs = round(float(time.split(':')[2]))



    #url for the http request
    #this is current weather api
    url = "http://api.openweathermap.org/data/2.5/weather?lat="+ str(lat) + "&lon=" + str(long) + "&appid=" + api_key + "&units=imperial"
    response = requests.get(url,  auth=('user', 'pass'))
    
    #store json object
    data = response.json()

    #check wether the location exist
    if data["cod"] != "404":

        #return specific data from json object
        weather = data["weather"]
        main = data["main"]
        wind = data["wind"]
     
    else:        
        print("404 City Not Found")


    #print datas needed and formatting 
    print("Date: " + date)
    print("Time: " + hours + ':' + mins + ':' + str(secs))
    print("Weather: " + weather[0]['description'])
    print("Temperture(Fahrenheit): " + str(round(main['temp'])) + '(H:' + str(round(main['temp_max']))+ '\L:' + str(round(main['temp_min'])) + ')')
    print("Wind Speed(MPH): " + str(wind['speed']))

   
