'''
Weatherments Cookbook.
Here we will define functions using Twitter API endpoints to use in our mining program to 
    make it more readable
'''
import twitter
import json # ~pretty~ print
from functools import partial # maybe on this one dont know if well actually need it
import io # send to files to send to databse
from collections import Counter
import nltk.sentiment.util
from nltk import *
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import wordnet as wn

class TweetDB:
    def __init__(self, twStr, weatherSent='none'):
        self.tweetSent = sentiment(twStr[0]) # Setniment of tweet
        self.tweet = twStr[0] # tweet as string
        self.time = twStr[1][3] # time in '00:00:00' format
        self.date = twStr[1][0:3] # date in 'Wed Oct 10' format
        self.weatherSent = weatherSent # weather sentiment

    def setWeath(self, weathSent): # weather sentiment setter
        self.weatherSent = weathSent


#This oath function was taken from the Ch. 9 Cookbook of our textbook 
def oauth_login():
    keys = []
    with open ('keys.txt', 'rt') as myfile:  # Open lorem.txt for reading
        for myline in myfile:
            keys.append(myline)
    
    CONSUMER_KEY = keys[0]
    CONSUMER_SECRET = keys[1]
    OAUTH_TOKEN = keys[2]
    OAUTH_TOKEN_SECRET = keys[3]
    
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
    # Here we say the string stream will hold all of the statuses collected from the area location
    stream = twitter_stream.statuses.filter(locations='-74,40,-73,41')
    c = 0
    for tweet in stream:
        try:
            if tweet['truncated']: # If a tweet is truncated, get the full thing
                #  a = TweetDB(tweet['extended_tweet']['full_text'], tweet['created_at'])
                #  tweetLs.append(a)
                #****Above to be uncommented, below deleted once sentiment() is fully working
                tweetSet = (tweet['extended_tweet']['full_text'], tweet['created_at'])
                tweetLs.append(tweetSet)
            else:
                #a =  TweetDB(tweet['text'],tweet['created_at'])
                #tweetLs.append(a)
                #****Above to be uncommented, below deleted once sentiment() is fully working
                tweetSet = (tweet['text'], tweet['created_at'])
                tweetLs.append(tweetSet)
        except:
            pass
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
    print(nltk.sentiment.util.demo_vader_instance(newString))
    return (nltk.sentiment.util.demo_vader_instance(newString))
    #print(nltk.sentiment)
