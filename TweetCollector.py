import twitter
import json
import Cookbook as cb

# Here we create a twitter api object using the tokens of our Twitter app
twitter_api = cb.oauth_login()
print(twitter_api)
#tweets = cb.StreamLoc(twitter_api, '-74,40,-73,41') #NY, NY box
cb.sentiment()