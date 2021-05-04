'''
Weatherments Cookbook.
Here we will define functions using Twitter API endpoints to use in our mining program to 
    make it more readable
'''
import WeatherAPI as wa
import twitter
import json # ~pretty~ print
from functools import partial # maybe on this one dont know if well actually need it
import io # send to files to send to databse
from collections import Counter
import nltk.sentiment.util
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk import *
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet as wn

class TweetDB:
    weth = wa.getWeatherData()
    def __init__(self, twStr, time, weatherSent=weth):
        ls = time.split()
        self.tweetSent = sentiment(twStr) # Setniment of tweet
        self.tweet = twStr # tweet as string
        self.time = ls[3] # time in '00:00:00' format UTC
        self.date = ' '.join(ls[0:3]) # date in 'Wed Oct 10' format
        self.weatherSent = weatherSent # weather sentiment

    def setWeath(self, weathSent): # weather sentiment setter
        self.weatherSent = weathSent


#This oath function was taken from the Ch. 9 Cookbook of our textbook 
def oauth_login():
    keys = []
    with open ('keys.txt', 'rt') as myfile:  # Open keys.txt for reading
        for myline in myfile:
            x = myline.split()
            keys.append(x[0])

    CONSUMER_KEY = str(keys[0])
    CONSUMER_SECRET = str(keys[1])
    OAUTH_TOKEN = str(keys[2])
    OAUTH_TOKEN_SECRET = str(keys[3])
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api


# This function uses the stream endpoint to stream tweets from a specified location
# twitter_api is the twitter object your collecting from and location is the geocode of the focus area
def StreamLoc (twitter_api, location):
    tweetLs = []

    # Here we created our stream object
    twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
    # Here we say stream will hold all of the statuses collected from the area, location
    stream = twitter_stream.statuses.filter(locations='-74,40,-73,41')
    
    for tweet in stream:
        #timer that recalls WeatherTimer
        try:
            if tweet['truncated']: # If a tweet is truncated, get the full thing
                a = TweetDB(tweet['extended_tweet']['full_text'], tweet['created_at']) 
                tweetLs.append(a) # Here we create an instance of the class TweetDB with our tweets and append them to a return list
            else:
                a =  TweetDB(tweet['text'],tweet['created_at'])
                tweetLs.append(a)
        except:
            pass
        if (len(tweetLs) > 10): return tweetLs # this is just a tester it will stop after 10 tweets are collected
    return tweetLs


def sentiment(tweetStr):
    # seperates strings into tokens
    tt = TweetTokenizer()
    tokens = tt.tokenize(tweetStr)
    print(tokens)

    # lemmatization (text normalization) = stripping off prefix/sufix so that the resulting form is a known word in dictionary
    # >>> import nltk
    # >>> nltk.download('wordnet')
    wnl = WordNetLemmatizer()
    newSet = [wnl.lemmatize(t) for t in tokens]
    newString = ' '.join(newSet)
    print(newString)

    # not needed?
    # >>> nltk.download('sentiwordnet')
    #for i in swn.senti_synsets(newSet): 
    #   print(i)

    # https://www.nltk.org/api/nltk.sentiment.html
    # >>> nltk.download('vader_lexicon')
    # Output polarity scores for a text using Vader approach.
    a = SentimentIntensityAnalyzer().polarity_scores(newString)
    print (a)
    return a
    #return (nltk.sentiment.util.demo_vader_instance(newString)) *******OLD IMPLEMENTATION, CURRENT IS ABOVE
    
