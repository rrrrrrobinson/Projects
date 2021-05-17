import twitter
import json
import Cookbook as cb
import WeatherAPI as wa
import DbPy as DB


# Here we create a twitter api object using the tokens of our Twitter app
twitter_api = cb.oauth_login()
print(twitter_api)

# Here we call our function that implements Twitter's Streaming API on 2 diagonal corners of Syracuse's corrdinates
tweets = cb.StreamLoc(twitter_api, '-76.33,42.90,-75.87,43.14') #Syracuse, NY SW and NE corner
# Tweets is a list of TweetDB type objects containing the tweet, the time and date it was created,
# The sentiment of the tweet, and the sentiment of the weather at the time of creation

for i in tweets:
    # A print statement to get a glimpse of our TweetDB objects as theyre added to the database
    print("sentiment " + str(i.tweetSent) + " tweetstr " + str(i.tweet) + " time " + str(i.time) + " date " \
             + str(i.date) + " weathersent " + str(i.weatherSent))
    
    # Here we store our TweetDB objects to our database
    #print(DB.saveToDB(i)) 
    
# Tells us how big the batch we just collected was 
print(len(tweets))