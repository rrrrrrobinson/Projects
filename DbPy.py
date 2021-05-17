from pymongo import MongoClient
import Cookbook

# Create mongoDb client object for database interaction
client = MongoClient("mongodb+srv://user0:gKGDWJlHy6qGZrhx@weathermentsdb.tdbnp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Choose the database we want to connect to 
db = client.get_database('WeathermentsDB')
# TweetData collection
dbTweets = db.TweetData 

# Save a tweet object to the databse we established above
def pullAllTweets():
    return dbTweets.find({})

def saveToDB(tweet):
    # Add tweetobject to remote database after transforming into a dicitonary
    dbTweets.insert_one(tweet.__dict__)
    return "tweet collected"

# Retreive all tweets from database that match the input parameter for weather type
def pullByWeather(sent):
    return dbTweets.find({"weatherSent" : sent})

