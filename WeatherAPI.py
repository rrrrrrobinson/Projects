#Open Weather Map API
import json
import requests
import datetime

def current_weather_api():
    api_key = "886f6a4c98d1b377418e02affd7ede7a"
    lat = 43.0481
    long = -76.1474
    
    date = datetime.datetime.now()


    url = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon" + str(long) + "&appid=" + api_key + "&units=imperial"
    response = requests.get(url,  auth=('user', 'pass'))

    data = response.json()

    if data["cod"] != "404":
        print(1)        
    else:
        print("404 City Not Found")

    print(data)
    
current_weather_api()
