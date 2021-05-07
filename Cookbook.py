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
from nltk.corpus import words
from nltk.corpus import stopwords
import string

class TweetDB:
    weth = wa.getWeatherData() # Create a local variable of the weather sentiment by making a call to the Weather API
    def __init__(self, twStr, time, weatherSent=weth):
        ls = time.split() # Splitting the time returned by twitter into the format we want
        self.tweetSent = sentiment(twStr) # Setniment of tweet using out function sentiment()
        self.tweet = twStr # tweet as string
        self.time = ls[3] # time in '00:00:00' format UTC
        self.date = ' '.join(ls[0:3]) # date in 'Wed Oct 10' format
        self.weatherSent = weatherSent # weather sentiment

    #def setWeath(self, weathSent): # weather sentiment setter
    #    self.weatherSent = weathSent


#This oath function was taken from the Ch. 9 Cookbook of our textbook 
def oauth_login():
    keys = []
    with open ('keys.txt', 'rt') as myfile:  # Open keys.txt for reading
        for myline in myfile: # Grabbing the keys from our secret key file
            x = myline.split()
            keys.append(x[0])

    CONSUMER_KEY = str(keys[0])
    CONSUMER_SECRET = str(keys[1])
    OAUTH_TOKEN = str(keys[2])
    OAUTH_TOKEN_SECRET = str(keys[3])
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET) # Creating our authenication object
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api


# This function uses the stream endpoint to stream tweets from a specified location
# twitter_api is the twitter object your collecting from and location is the geocode of the focus area
def StreamLoc (twitter_api, location):
    tweetLs = [] # return list of tweets, filled below

    # Here we created our stream object
    twitter_stream = twitter.TwitterStream(auth=twitter_api.auth)
    # Here we say stream will hold all of the statuses collected from the area, location
    stream = twitter_stream.statuses.filter(locations=location)
    
    for tweet in stream: # For every tweet we collect, we create a TweetDB object
        try:
            if tweet['truncated']: # If a tweet is truncated, get the full thing
                # Here we create an instance of the class TweetDB with our tweets
                a = TweetDB(tweet['extended_tweet']['full_text'], tweet['created_at']) 
                if a.tweetSent == 0: # If the tweet did not have any recognizable feature, we do not append it
                    pass 
                else: tweetLs.append(a) # We then append our TweetDB object to a return list
            else:
                a =  TweetDB(tweet['text'],tweet['created_at']) # Untruncated tweet
                if a.tweetSent == 0:
                    pass
                else: tweetLs.append(a)
        except:
            pass
        #if (len(tweetLs) > 10): return tweetLs # this is just a tester it will stop after 10 tweets are collected
    return tweetLs


def sentiment(tweetStr):

    # import stopwords to eliminate them from the sting before sentiment analysis
    stop_words = stopwords.words('english')
    vocab = words.words() # vocab is the list of words in nltk

    tokens = tokenize.word_tokenize(tweetStr) # a regular tokenizer to break out string into tokens
    print (tokens)


    # lemmatization (text normalization) = stripping off prefix/sufix so that the resulting form is a known word in dictionary
    # >>> import nltk
    # >>> nltk.download('wordnet')
    wnl = WordNetLemmatizer()
    # Here we lemmatize the words so long as they are not stopwords or punctuation 
    newSet = [wnl.lemmatize(t) for t in tokens if t not in stop_words and t not in string.punctuation]
    after = len([lt for lt in newSet if lt in vocab])
    if after == 0: # If no words in the tweet that arent stopwords, puncuation or aren't recognized by NLTK
        return 0 # return 0 to be caught in our StreamLoc() functino so the tweet is not added to the list TweetDB objects
    newString = ' '.join(newSet) # rejoin our words with a space between each
    #print(newString)

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
    


