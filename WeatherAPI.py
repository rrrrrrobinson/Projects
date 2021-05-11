#Open Weather Map API
import json
import requests
import datetime
import time

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
        #return specific data set from json object
        weather_data = data["weather"]
        main = data["main"]
        
        wind = data["wind"]
        
        #get  single data needed
        weather = weather_data[0]['description']
        weather_id = weather_data[0]['id']
        average_temp = round((main['temp_max'] + main['temp_min']) / 2)
        wind_speed = wind['speed']
        humidity = main['humidity']
    else:        
        print("404 City Not Found")

    #print datas needed and formatting 
    # print("Date: " + date)
    # print("Time: " + hours + ':' + mins + ':' + str(secs))
    # print("Location: " +  data['name'])
    # print("Weather: " + weather)
    # print("Temperture(Fahrenheit): " + str(round(main['temp'])) + '(H:' + str(round(main['temp_max']))+ '\L:' + str(round(main['temp_min'])) + ')')
    # print("Humidity: " + str(humidity) + "%")
    # print("Wind Speed(MPH): " + str(wind_speed))
    # print(' ')
    
    #determine wheather it is a good or bad weather
    if (weather_id < 800):
        condition = 'BAD'

    elif (weather_id > 800 and weather_id < 803):
        if (average_temp >= 45 and average_temp <= 80 and wind_speed <= 15):
            condition = 'GOOD'
            
        elif (average_temp < 45 or average_temp > 80 or wind_speed > 15):
            condition = 'BAD'

    elif (weather_id >= 803):
        if (average_temp >= 45 and average_temp <= 80 and wind_speed <= 15):
            condition = 'OK'
            
        elif (average_temp < 45 or average_temp > 80 or wind_speed > 15):
            condition = 'BAD'


    return condition

    #def WeatherTimer() 
        #current = getWeatherData()
        #after set amount time
        #current = getWeatherData()
        #pulls new weather data every 30 minutes  
# class Weath():
#         def __init__(self):
#             self.condition = getWeatherData()

#         def update(self):
#             self.condition = getWeatherData()
# class Weath:
#     def __init__(self):
#         self.condition = getWeatherData()
#         #sent = Weath()

#         start = time.time()
#         while(True):
#             if(int(time.time()-start) == 10):
#                     self.condition = getWeatherData()
#                     start = start + 10
        #after timer
  

#print(getWeatherData())
