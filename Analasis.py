import DbPy as DB
import networkx as nx
import math


raw_weath_ok = DB.pullByWeather("OK")# all ok weather #find({"weatherSent" : "OK"})

raw_weath_good = DB.pullByWeather("GOOD")# all good weather

raw_weath_bad = DB.pullByWeather("BAD")#all bad weather

weath_ok_pos = [] # contains the positive tweets created during OK weather
weath_ok_neg = [] # contains the negative tweets created during OK weather
weath_ok_neu = [] # contains the neutral tweets created during OK weather
weath_ok_posneu = [] # contains the positive leaning neutral tweets created during OK weather
weath_ok_negneu = [] # contains the negative leaning neutral tweets created during OK weather

for i in raw_weath_ok:
    #sentMax = max(i['tweetSent']['neg'], i['tweetSent']['pos'], i['tweetSent']['neu'])
    if i['tweetSent']['neg'] > i['tweetSent']['pos'] and i['tweetSent']['neg'] > i['tweetSent']['neu']:
        sentMax = ('neg : {0}'.format(i['tweetSent']['neg']))
        weath_ok_neg.append(i)
    
    elif i['tweetSent']['pos'] > i['tweetSent']['neg'] and i['tweetSent']['pos'] > i['tweetSent']['neu']:
        sentMax = ('pos : {0}'.format(i['tweetSent']['pos']))
        weath_ok_pos.append(i)
    else:        
        if i['tweetSent']['neg'] > i['tweetSent']['pos'] and i['tweetSent']['neg'] > 0.25:
            sentMax2 = ('negneu : {0}'.format(i['tweetSent']['neg']))
            weath_ok_negneu.append(i)
        elif i['tweetSent']['neg'] < i['tweetSent']['pos'] and i['tweetSent']['pos'] > 0.25:
            sentMax2 = ('posneu : {0}'.format(i['tweetSent']['pos']))
            weath_ok_posneu.append(i)
        else:
            sentMax = ('neu : {0}'.format(i['tweetSent']['neu']))
            weath_ok_neu.append(i)


weath_good_pos = [] # contains the positive tweets created during GOOD weather
weath_good_neg = [] # contains the negative tweets created during GOOD weather
weath_good_neu = [] # contains the neutral tweets created during GOOD weather
weath_good_posneu = [] # contains the positive leaning neutral tweets created during GOOD weather
weath_good_negneu = [] # contains the negative leaning neutral tweets created during GOOD weather

for i in raw_weath_good:
    #sentMax = max(i['tweetSent']['neg'], i['tweetSent']['pos'], i['tweetSent']['neu'])
    if i['tweetSent']['neg'] > i['tweetSent']['pos'] and i['tweetSent']['neg'] > i['tweetSent']['neu']:
        sentMax = ('neg : {0}'.format(i['tweetSent']['neg']))
        weath_good_neg.append(i)
    
    elif i['tweetSent']['pos'] > i['tweetSent']['neg'] and i['tweetSent']['pos'] > i['tweetSent']['neu']:
        sentMax = ('pos : {0}'.format(i['tweetSent']['pos']))
        weath_good_pos.append(i)
    else:        
        if i['tweetSent']['neg'] > i['tweetSent']['pos'] and i['tweetSent']['neg'] > 0.25:
            sentMax2 = ('negneu : {0}'.format(i['tweetSent']['neg']))
            weath_good_negneu.append(i)
        elif i['tweetSent']['neg'] < i['tweetSent']['pos'] and i['tweetSent']['pos'] > 0.25:
            sentMax2 = ('posneu : {0}'.format(i['tweetSent']['pos']))
            weath_good_posneu.append(i)
        else:
            sentMax = ('neu : {0}'.format(i['tweetSent']['neu']))
            weath_good_neu.append(i)  


weath_bad_pos = [] # contains the positive tweets created during GOOD weather
weath_bad_neg = [] # contains the negative tweets created during GOOD weather
weath_bad_neu = [] # contains the neutral tweets created during GOOD weather
weath_bad_posneu = [] # contains the positive leaning neutral tweets created during GOOD weather
weath_bad_negneu = [] # contains the negative leaning neutral tweets created during GOOD weather

for i in raw_weath_bad:
    #sentMax = max(i['tweetSent']['neg'], i['tweetSent']['pos'], i['tweetSent']['neu'])
    if i['tweetSent']['neg'] > i['tweetSent']['pos'] and i['tweetSent']['neg'] > i['tweetSent']['neu']:
        sentMax = ('neg : {0}'.format(i['tweetSent']['neg']))
        weath_bad_neg.append(i)
    
    elif i['tweetSent']['pos'] > i['tweetSent']['neg'] and i['tweetSent']['pos'] > i['tweetSent']['neu']:
        sentMax = ('pos : {0}'.format(i['tweetSent']['pos']))
        weath_bad_pos.append(i)
    else:        
        if i['tweetSent']['neg'] > i['tweetSent']['pos'] and i['tweetSent']['neg'] > 0.25:
            sentMax2 = ('negneu : {0}'.format(i['tweetSent']['neg']))
            weath_bad_negneu.append(i)
        elif i['tweetSent']['neg'] < i['tweetSent']['pos'] and i['tweetSent']['pos'] > 0.25:
            sentMax2 = ('posneu : {0}'.format(i['tweetSent']['pos']))
            weath_bad_posneu.append(i)
        else:
            sentMax = ('neu : {0}'.format(i['tweetSent']['neu']))
            weath_bad_neu.append(i) 

G = nx.Graph
ok = weath_ok_pos+weath_ok_neg+weath_ok_neu+weath_ok_posneu+weath_ok_negneu
good = weath_good_pos+weath_good_neg+weath_good_neu+weath_good_posneu+weath_good_negneu
bad = weath_bad_pos+weath_bad_neg+weath_bad_neu+weath_bad_posneu+weath_bad_negneu

print()
print("********OK************** \n Positive length: {0} \n Negative length: {1} \n Neutral length: {2} \n Pos Neutral length: {3} \n Neg Neutral length: {4}".format(len(weath_ok_pos)/len(ok), len(weath_ok_neg)/len(ok), len(weath_ok_neu)/len(ok), len(weath_ok_posneu)/len(ok), len(weath_ok_negneu)/len(ok)))
    
print("\n ************************************* \n")

print("********GOOD************** \n Positive length: {0} \n Negative length: {1} \n Neutral length: {2} \n Pos Neutral length: {3} \n Neg Neutral length: {4}".format(len(weath_good_pos)/len(good), len(weath_good_neg)/len(good), len(weath_good_neu)/len(good), len(weath_good_posneu)/len(good), len(weath_good_negneu)/len(good)))

print("\n ************************************* \n")

print("********BAD************** \n Positive length: {0} \n Negative length: {1} \n Neutral length: {2} \n Pos Neutral length: {3} \n Neg Neutral length: {4}".format(len(weath_bad_pos)/len(bad), len(weath_bad_neg)/len(bad), len(weath_bad_neu)/len(bad), len(weath_bad_posneu)/len(bad), len(weath_bad_negneu)/len(bad)))
#weath_ok = (raw_weath_ok.find({"tweetSent" : ""}))
# set of 5 sets, each set corresponding to pos, neu, neg, posNeu, negNeu




#for i in range(len(ok) - 1):
    #w = abs(ok[i]['tweetSent']['pos'] - ok[i+1]['tweetSent']['pos'])
#G.add_weighted_edges_from([[(i, i+1, abs(ok[i]['tweetSent']['pos'] - ok[i+1]['tweetSent']['pos'])) for i in range(len(ok) - 1)]]
       # [ (ok[i], ok[i+1], w)])


