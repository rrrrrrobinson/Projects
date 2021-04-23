#Open Weather Map API
import json
import requests
import datetime

api_key = "886f6a4c98d1b377418e02affd7ede7a"
lat = 43.0481
long = -76.1474

date = datetime.datetime.now()

def weather_data_api(aKey, aLat, aLong):  
    url = "http://api.openweathermap.org/data/2.5/weather?lat="+ str(aLat) + "&lon=" + str(aLong) + "&appid=" + aKey + "&units=imperial"
    response = requests.get(url,  auth=('user', 'pass'))

    data = response.json()

    if data["cod"] != "404":
        weather = data["weather"]
        main = data["main"]
        wind = data["wind"]
        print("Weather: " + weather[0]['description'])
        print("Temperture(Fahrenheit): " + str(round(main['temp'])) + '(H:' + str(round(main['temp_max']))+ '\L:' + str(round(main['temp_min'])) + ')')
        print("Wind Speed(MPH): " + str(wind['speed']))
        
    else:
        print("404 City Not Found")


print(date)    
weather_data_api(api_key, lat, long)
