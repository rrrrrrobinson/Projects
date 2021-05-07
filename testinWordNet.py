import nltk
#nltk.download()
from nltk.corpus import words
import random
from nltk.misc import wordfinder as wd
from nltk.corpus import stopwords
from nltk import *

import emoji
nmes = '😷😷😷'
#print(nmes[0] in emoji.emoji_lis)
mes = ['i','am','tesyinh','😷😷😷']
rmes = 'I am testing 😷😷😷'
#print(type(emoji.emojize(mes,use_aliases=True)))
spliter = emoji.get_emoji_regexp().split(rmes)
full = [t for t in spliter if t != '']
print(full)

my_str = "This is a string to test and see if these words are in the corpus. I'm also checking to see how long it will take"
my_str2 = "#Positive"
vocab = words.words()
print(type(vocab))

# stop_words = stopwords.words('english')


#     # seperates strings into tokens
# tt = TweetTokenizer()
# tokens = tt.tokenize(my_str2)
# #print(tokens)

#     # lemmatization (text normalization) = stripping off prefix/sufix so that the resulting form is a known word in dictionary
#     # >>> import nltk
#     # >>> nltk.download('wordnet')
# wnl = WordNetLemmatizer()
# newSet = [wnl.lemmatize(t) for t in tokens if t not in stop_words and t in vocab]
# newString = ' '.join(newSet)
# print(newString)
# a = SentimentIntensityAnalyzer().polarity_scores(newString)
# print (a)
#print(wd.wordfinder(newString))
#print(len(vocab))