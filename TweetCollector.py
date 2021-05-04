import twitter
import json
import Cookbook as cb
import WeatherAPI as wa
import DbPy as DB


# Here we create a twitter api object using the tokens of our Twitter app
twitter_api = cb.oauth_login()
print(twitter_api)
tweets = cb.StreamLoc(twitter_api, '-74,40,-73,41') #NY, NY box
# tweets is a list of TweetDB type objects

#******** Checker to see if everything is as we want it for the database (it is) **************
# [print("sentiment " + str(i.tweetSent) + " tweetstr " + str(i.tweet) + " time " + str(i.time) + " date " \
#              + str(i.date) + " weathersent " + str(i.weatherSent)) for i in tweets]
for i in tweets:
    print("sentiment " + str(i.tweetSent) + " tweetstr " + str(i.tweet) + " time " + str(i.time) + " date " \
             + str(i.date) + " weathersent " + str(i.weatherSent))
    print(DB.saveToDB(i))