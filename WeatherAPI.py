#Open Weather Map API
import json
import requests
import datetime
import time

def getWeatherData():
    # Api key from openweather 
    api_key = "886f6a4c98d1b377418e02affd7ede7a"
  
    # Lat/long of Syracuse
    lat = 43.0481
    long = -76.1474

    # To record date and time of when data were collect
    date_time = datetime.datetime.now()

    # To round seconds to then nearest whole number and cast date_time to str
    item = str(date_time)
    
    # Take out date and time seperately and split hour, mintues and second
    date = item.split()[0]
    time = item.split()[1]
    hours = time.split(':')[0]
    mins = time.split(':')[1]
    # Round the second
    secs = round(float(time.split(':')[2]))

    # Url for the http request and make current weather api call
    url = "http://api.openweathermap.org/data/2.5/weather?lat="+ str(lat) + "&lon=" + str(long) + "&appid=" + api_key + "&units=imperial"
    response = requests.get(url,  auth=('user', 'pass'))    
    # Store json object
    data = response.json()

    # Check wether the location exist
    if data["cod"] != "404":
        # Return specific data set from json object
        weather_data = data["weather"]
        main = data["main"]
        
        wind = data["wind"]
        
        # Get  single data needed
        weather = weather_data[0]['description']
        weather_id = weather_data[0]['id']
        average_temp = round((main['temp_max'] + main['temp_min']) / 2)
        wind_speed = wind['speed']
        humidity = main['humidity']
    else:        
        print("404 City Not Found")


    condition = 'NONE'
    # < 800 accounts for rain, snow, thundrstorms, and all weather types in between
    if (weather_id < 800):
        condition = 'BAD'
    # > 800 and  < 803 accounts for clear sky and partly cloudy
    elif (weather_id > 800 and weather_id < 803):
        # Temperature >= 45 and <= 80 and wind < 15 mph
        if (average_temp >= 45 and average_temp <= 80 and wind_speed <= 15):
            condition = 'GOOD'
        # Temperature < 45 and > 80 and wind > 15 mph   
        elif (average_temp < 45 or average_temp > 80 or wind_speed > 15):
            condition = 'BAD'
    # Heavy clouds and completely cloudy
    elif (weather_id >= 803):
        # Temperature >= 45 and <= 80 and wind <= 15 mph
        if (average_temp >= 45 and average_temp <= 80 and wind_speed <= 15):
            condition = 'OK'
        # Temperature < 45 and > 80 and wind > 15 mph    
        elif (average_temp < 45 or average_temp > 80 or wind_speed > 15):
            condition = 'BAD'

    return condition
