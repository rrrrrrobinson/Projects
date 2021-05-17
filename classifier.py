import DbPy as DB
from nltk import *
import twitter
import Cookbook as cb


twitter_api = cb.oauth_login()

# test_tweets = cb.getTweetsFromPast5Days(twitter_api)

# Test Tweets that are not included in the training set, because they will be classified later
test_tweets = [('Syracuse hung in there in the first but their shot selection has to be better. Played catch with McElroy too much.… https://t.co/K1xGaCIiix','Actual: GOOD'),
               ('It really just be me and my son he’s my only friend','Actual: GOOD'),
               ('@mlhelmke1 People need to get the vaccine to protect themselves and those in their inner circle and those that choo… https://t.co/raeOJ1Zp1h','Actual: GOOD'),
               ('@TheRickyDavila Wouldn’t be surprised to see some people dancing in the streets!','Actual: GOOD'),
               ('@MarkRuffalo once again bring the hero we all need.','Actual: OK'),
               ('RT @lwcesf: .@binghamtonu and @PrezHarvey are failing their students of color by not providing a more diverse and accessible counseling cen…','Actual: OK'),
               ('@sexybulba As well you should angel you’re perfect','Actual: GOOD'),
               ('Safe Travels: Sleep in the trees with these magical Upstate NY treehouses https://t.co/nBkbejK12D','Actual: GOOD')]




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
classifier.show_most_informative_features(100)

# Loop through test tweets and classify them
for (t,a) in test_tweets:
    # print "{0} : {1}".format(t, classifier.classify(extract_features(t.split())))
    print ("{0} : {1} ... {2}".format(t, classifier.classify(extract_features([e.lower() for e in t.split() if len(e) >= 3])),a))