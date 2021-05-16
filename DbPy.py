#pip install virtualenvwrapper
from pymongo import MongoClient
import Cookbook

client = MongoClient("mongodb+srv://user0:gKGDWJlHy6qGZrhx@weathermentsdb.tdbnp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.get_database('WeathermentsDB')
dbTweets = db.TweetData # tweetData collection

def saveToDB(tweet):
    dbTweets.insert_one(tweet.__dict__)
    return "tweet collected"

def saveToDBWithWeather(tweet):
    tweet.setWeath(WeatherAPI.getWeatherData())
    dbTweets.insert_one(tweet.__dict__)

def pullByWeather(sent):
    a = dbTweets.find({"weatherSent" : sent})
    return a

