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

#This oath function was taken from the Ch. 9 Cookbook of our textbook 
def oauth_login(): 
    CONSUMER_KEY = 'rrrdYKyayW330BVVGEb4nMsHH'
    CONSUMER_SECRET = 'tC2sMcGf3QwDuS4jvvp4X1JKmJs4MqkTggvST0906CPBPE4fgs'
    OAUTH_TOKEN = '1368678652058218504-NbUWEatUhUFjbElHASrmQKe8BGjMyE'
    OAUTH_TOKEN_SECRET = 'HwcXId3HVhZxJ1WXFj3rrPss7ESxGd4qdYbpYGZRjVDYv'
    
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api