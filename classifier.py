import DbPy as DB
from nltk import *
import twitter
import Cookbook as cb


twitter_api = cb.oauth_login()

test_tweets = cb.getTweetsFromPast5Days(twitter_api, '-76.33,42.90,-75.87,10mi', '5/16/2021')


'''
def makeTweetArray(dictTweets, arrayTweets):
    for i in dictTweets:
        arrayTweets.append((i['tweet'],i['weatherSent']))

# Pull all tweets from database
databaseObjects =  DB.pullAllTweets()
tweets = []

# Tweet will be the array type (tweet,weather Sentiment value)
makeTweetArray(databaseObjects,tweets)
# print(tweets)

tweetsFiltered = []

# Filter out all words in tweets that are less then 3 letters
for (words, weatherSent) in tweets:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    tweetsFiltered.append((words_filtered, weatherSent))

# Retreive all the words from all the tweets in the database and put it into a list
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words += words
    return all_words

# All words in the database
all_words = get_words_in_tweets(tweetsFiltered)

# Analyize word features and utilize the most common ones to create word_features
def get_word_features(wordlist):
    wordlist = FreqDist(wordlist)
    # Word_features = wordlist.keys() # careful here
    word_features = [w for (w, c) in wordlist.most_common(2000)] #use most_common() if you want to select the most frequent words
    return word_features

# Retrieve word_features by using the result of get_words_in_tweets
word_features = get_word_features(get_words_in_tweets(tweetsFiltered))

# Combines word_features with all the database data to create a training_set to later train with Niave Bayes Classifier
def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

# Training set of data needed for Naive Bayes Classifer
training_set = [(extract_features(d), c) for (d,c) in tweetsFiltered]

# Classifys the training set utilzing the Niave Bayes Classifer
classifier = NaiveBayesClassifier.train(training_set)
# Shows the most prominent/infleuncial words on a given weather type day
classifier.show_most_informative_features(100)'''