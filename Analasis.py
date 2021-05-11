import DbPy as DB



raw_weath_ok = pullByWeather("OK")# all ok weather #find({"weatherSent" : "OK"})

raw_weath_good = pullByWeather("GOOD")# all good weather

raw_weath_bad = pullByWeather("BAD")#all bad weather

weath_ok_pos
weath_ok_neg
weath_ok_neu
weath_ok_posneu
weath_ok_negneu

for i in raw_weath_ok:
    #sentMax = max(i['tweetSent']['neg'], i['tweetSent']['pos'], i['tweetSent']['neu'])
    if i['tweetSent']['neg'] > i['tweetSent']['pos'] and i['tweetSent']['neg'] > i['tweetSent']['neu']:
        sentMax = ('neg : {0}'.format(i['tweetSent']['neg']))
        weath_ok_neg.add(i)
    
    else if i['tweetSent']['pos'] > i['tweetSent']['neg'] and i['tweetSent']['pos'] > i['tweetSent']['neu']:
        sentMax = ('pos : {0}'.format(i['tweetSent']['pos']))
        weath_ok_pos.add(i)
    else:        
        if i['tweetSent']['neg'] > i['tweetSent']['pos'] and i['tweetSent']['neg'] > '0.25':
            sentMax2 = ('negneu : {0}'.format(i['tweetSent']['neg']))
            weath_ok_negneu.add(i)
        else if i['tweetSent']['neg'] < i['tweetSent']['pos'] and i['tweetSent']['pos'] > '0.25':
            sentMax2 = ('posneu : {0}'.format(i['tweetSent']['pos']))
            weath_ok_posneu.add(i)
        else:
            sentMax = ('neu : {0}'.format(i['tweetSent']['neu']))
            weath_ok_neu.add(i)

    


    

weath_ok = (raw_weath_ok.find({"tweetSent" : ""}))
# set of 5 sets, each set corresponding to pos, neu, neg, posNeu, negNeu

