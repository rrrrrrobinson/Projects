import DbPy as DB
import networkx as nx
import math
import matplotlib.pyplot as plt
import json


raw_weath_ok = DB.pullByWeather("OK")# all ok weather #find({"weatherSent" : "OK"})

raw_weath_good = DB.pullByWeather("GOOD")# all good weather

raw_weath_bad = DB.pullByWeather("BAD")#all bad weather


# For each day type, we split the tweets up into 5 categories by tweet sentiment
#   To be in the positive or negative categories, a tweet must have a positive or negaative majority, respectivley
#   If a tweet is majority neutral, we check then check to see if it leans a certain way
#       When the tweet is majority neutral and the second majority is positive with a possitive score greater then 0.25, it is positive neutral
#       Else if the second majoirty is negative with a score greater than 0.25, it is negative neutral
#       Otherwise it is neutral
weath_ok_pos = [] # contains the positive tweets created during OK weather
weath_ok_neg = [] # contains the negative tweets created during OK weather
weath_ok_neu = [] # contains the neutral tweets created during OK weather
weath_ok_posneu = [] # contains the positive leaning neutral tweets created during OK weather
weath_ok_negneu = [] # contains the negative leaning neutral tweets created during OK weather

# Here we categorize the tweets on OK days
for i in raw_weath_ok:
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

# Here we categorize the tweets on GOOD days
for i in raw_weath_good:
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


weath_bad_pos = [] # contains the positive tweets created during BAD weather
weath_bad_neg = [] # contains the negative tweets created during BAD weather
weath_bad_neu = [] # contains the neutral tweets created during BAD weather
weath_bad_posneu = [] # contains the positive leaning neutral tweets created during BAD weather
weath_bad_negneu = [] # contains the negative leaning neutral tweets created during BAD weather

# Here we categorize the tweets on BAD days
for i in raw_weath_bad:
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



# Creating a list of tweets created on a given day for each day
ok = weath_ok_pos+weath_ok_neg+weath_ok_neu+weath_ok_posneu+weath_ok_negneu
good = weath_good_pos+weath_good_neg+weath_good_neu+weath_good_posneu+weath_good_negneu
bad = weath_bad_pos+weath_bad_neg+weath_bad_neu+weath_bad_posneu+weath_bad_negneu

print()
print("Raw Number Findings:")
print()
print("********OK************** \n Positive length: {0} \n Negative length: {1} \n Neutral length: {2} \n Pos Neutral length: {3} \n Neg Neutral length: {4}".format(len(weath_ok_pos), len(weath_ok_neg), len(weath_ok_neu), len(weath_ok_posneu), len(weath_ok_negneu)))
    
print("\n ************************************* \n")

print("********GOOD************** \n Positive length: {0} \n Negative length: {1} \n Neutral length: {2} \n Pos Neutral length: {3} \n Neg Neutral length: {4}".format(len(weath_good_pos), len(weath_good_neg), len(weath_good_neu), len(weath_good_posneu), len(weath_good_negneu)))

print("\n ************************************* \n")

print("********BAD************** \n Positive length: {0} \n Negative length: {1} \n Neutral length: {2} \n Pos Neutral length: {3} \n Neg Neutral length: {4}".format(len(weath_bad_pos), len(weath_bad_neg), len(weath_bad_neu), len(weath_bad_posneu), len(weath_bad_negneu)))

# We normalize our finding by dividing the length of each of the 5 categories by the number of tweets created on the type of day
print()
print()
print("Normalized Findings:")
print()
print("********OK************** \n Positive length: {0} \n Negative length: {1} \n Neutral length: {2} \n Pos Neutral length: {3} \n Neg Neutral length: {4}".format(len(weath_ok_pos)/len(ok), len(weath_ok_neg)/len(ok), len(weath_ok_neu)/len(ok), len(weath_ok_posneu)/len(ok), len(weath_ok_negneu)/len(ok)))
    
print("\n ************************************* \n")

print("********GOOD************** \n Positive length: {0} \n Negative length: {1} \n Neutral length: {2} \n Pos Neutral length: {3} \n Neg Neutral length: {4}".format(len(weath_good_pos)/len(good), len(weath_good_neg)/len(good), len(weath_good_neu)/len(good), len(weath_good_posneu)/len(good), len(weath_good_negneu)/len(good)))

print("\n ************************************* \n")

print("********BAD************** \n Positive length: {0} \n Negative length: {1} \n Neutral length: {2} \n Pos Neutral length: {3} \n Neg Neutral length: {4}".format(len(weath_bad_pos)/len(bad), len(weath_bad_neg)/len(bad), len(weath_bad_neu)/len(bad), len(weath_bad_posneu)/len(bad), len(weath_bad_negneu)/len(bad)))


Gok = nx.Graph() # Create our graphs for each type of day
Ggood = nx.Graph()
Gbad = nx.Graph()
color_map = [] # Create color maps for each type of day to color our nodes
color_mapg = []
color_mapb = []


# Since we are pulling from our databse each entry has a unique id that can be accessed with entry.get('_id')
#   In order to color them accordingly on our graph, we attach a set identifiyer onto the start of each id
#       Color identifierys go from 1-5 corresponding to positive, negative, neutral, positive leaning neutral, and negative leaning neutral respectivley 
#   Below we attach these color identifiers 
for i in range(len(good) - 1):
    u = good[i]
    v = good[i+1]
    
    if u in weath_good_pos: 
        a = '1'+str(u.get('_id'))
    elif u in weath_good_neg: 
        a = '2'+str(u.get('_id'))
    elif u in weath_good_neu:
        a =  '3'+str(u.get('_id'))
    elif u in weath_good_posneu: 
        a = '4'+str(u.get('_id'))
    else:
        a = '5'+str(u.get('_id'))

    if v in weath_good_pos: 
        b ='1'+str(v.get('_id'))
    elif v in weath_good_neg: 
        b = '2'+str(v.get('_id'))
    elif v in weath_good_neu: 
        b = '3'+str(v.get('_id'))
    elif v in weath_good_posneu: 
        b = '4'+str(v.get('_id'))
    else: 
        b = '5'+str(v.get('_id'))
    # Here we add an edge between a tweet in the list good and its neighbor where the weight is the difference in their positivity scores
    # We divide the edge weight by 2 here to make our graph look cleaner and more similar to the other days as we have much less GOOD day tweets thatn BAD and OK
    Ggood.add_edge(u_of_edge=a, v_of_edge=b, weight=abs(u['tweetSent']['pos'] - v['tweetSent']['pos'])/2)


for i in range(len(ok) - 1):  
    u = ok[i]
    v = ok[i+1]
    
    if u in weath_ok_pos: 
        a = '1'+str(u.get('_id'))
    elif u in weath_ok_neg: 
        a = '2'+str(u.get('_id'))
    elif u in weath_ok_neu:
        a =  '3'+str(u.get('_id'))
    elif u in weath_ok_posneu: 
        a = '4'+str(u.get('_id'))
    else:
        a = '5'+str(u.get('_id'))

    if v in weath_ok_pos: 
        b ='1'+str(v.get('_id'))
    elif v in weath_ok_neg: 
        b = '2'+str(v.get('_id'))
    elif v in weath_ok_neu: 
        b = '3'+str(v.get('_id'))
    elif v in weath_ok_posneu: 
        b = '4'+str(v.get('_id'))
    else: 
        b = '5'+str(v.get('_id'))
    # Here we add an edge between a tweet in the list good and its neighbor where the weight is the difference in their neutrality scores
    Gok.add_edge(u_of_edge=a, v_of_edge=b, weight=abs(u['tweetSent']['neu'] - v['tweetSent']['neu']))



for i in range(len(bad) - 1):
    u = bad[i]
    v = bad[i+1]
    
    if u in weath_bad_pos: 
        a = '1'+str(u.get('_id'))
    elif u in weath_bad_neg: 
        a = '2'+str(u.get('_id'))
    elif u in weath_bad_neu:
        a =  '3'+str(u.get('_id'))
    elif u in weath_bad_posneu: 
        a = '4'+str(u.get('_id'))
    else:
        a = '5'+str(u.get('_id'))

    if v in weath_bad_pos: 
        b ='1'+str(v.get('_id'))
    elif v in weath_bad_neg: 
        b = '2'+str(v.get('_id'))
    elif v in weath_bad_neu: 
        b = '3'+str(v.get('_id'))
    elif v in weath_bad_posneu: 
        b = '4'+str(v.get('_id'))
    else: 
        b = '5'+str(v.get('_id'))

    # Here we add an edge between a tweet in the list good and its neighbor where the weight is the difference in their negativity scores
    Gbad.add_edge(u_of_edge=a, v_of_edge=b, weight=abs(u['tweetSent']['neg'] - v['tweetSent']['neg']))

# Here we initialize our color maps for each graph according to the color identifyer attached earlier
for i in Gok:
    if i[0] == '1':
        color_map.append('blue') # Blue is a positive tweet
    elif i[0] == '2':
        color_map.append('red')  # Red is a negative tweet
    elif i[0] == '3':
        color_map.append('grey') # Grey is a neutral tweet
    elif i[0] == '4':
        color_map.append('cyan')  # Cyan is a positive neutral tweet
    elif i[0] == '5':
        color_map.append('yellow') # Yellow is a negative neutral tweet
for i in Ggood: # Same mapping as above
    if i[0] == '1':
        color_mapg.append('blue')
    elif i[0] == '2':
        color_mapg.append('red')  
    elif i[0] == '3':
        color_mapg.append('grey')
    elif i[0] == '4':
        color_mapg.append('cyan')  
    elif i[0] == '5':
        color_mapg.append('yellow') 
for i in Gbad: # Same mapping as above
    if i[0] == '1':
        color_mapb.append('blue')
    elif i[0] == '2':
        color_mapb.append('red')  
    elif i[0] == '3':
        color_mapb.append('grey')
    elif i[0] == '4':
        color_mapb.append('cyan')  
    elif i[0] == '5':
        color_mapb.append('yellow') 


plt.figure('GOOD Day')
nx.draw(Ggood,  node_size=10, node_color=color_mapg)

plt.figure('OK Day')
nx.draw(Gok,  node_size=10, node_color=color_map)

plt.figure('BAD Day')
nx.draw(Gbad,  node_size=10, node_color=color_mapb)

plt.show()
plt.savefig("okgraph.png")
