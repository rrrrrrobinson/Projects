import DbPy as DB
import networkx as nx
import math
import matplotlib.pyplot as plt


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

G = nx.Graph()
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


color_map = []
#G.add_edge(1,v_of_edge=2)
for i in range(len(ok) - 1):
#a = [(ok[i], ok[(i+1)], abs(ok[i]['tweetSent']['pos'] - ok[(i+1)]['tweetSent']['pos']) ) for i in range(ok[i:] -1)]
    u = ok[i]
    v = ok[i+1]
    w = abs(u['tweetSent']['pos'] - v['tweetSent']['pos'])
    #print(v.get('_id'))
    
    ucolor = 'black'
    if u in weath_ok_pos: 
        a = '1'+str(u.get('_id'))
        #u.get('_id') = '1'+str(u.get('_id'))
    elif u in weath_ok_neg: 
        a = '2'+str(u.get('_id'))
       # u.get('_id') = '2'+u.get('_id')
        #colormap.append('red')
    elif u in weath_ok_neu:
        a =  '3'+str(u.get('_id'))
       # u.get('_id') = '3'+u.get('_id')
        #colormap.append('grey')
    elif u in weath_ok_posneu: 
        a = '4'+str(u.get('_id'))
        #u.get('_id') = '4'+u.get('_id')
        #colormap.append('lightblue')
    else:
        a = '5'+str(u.get('_id'))
        #u.get('_id') = '5'+u.get('_id') 
        #colormap.append('lightred')
    vcolor = 'black'
    if v in weath_ok_pos: 
        b ='1'+str(v.get('_id'))
       # v.get('_id') = '1'+v.get('_id')
    elif v in weath_ok_neg: 
        b = '2'+str(v.get('_id'))
        #v.get('_id') = '2'+v.get('_id')
    elif v in weath_ok_neu: 
        b = '3'+str(v.get('_id'))
        #v.get('_id') = '3'+v.get('_id')
    elif v in weath_ok_posneu: 
        b = '4'+str(v.get('_id'))
        #v.get('_id') = '4'+v.get('_id')
    else: 
        b = '5'+str(v.get('_id'))
       # v.get('_id') = '5'+v.get('_id')
    
    #G.add_node(u.get('_id'), color=ucolor)
    #G.add_node(v.get('_id'), color=vcolor)
    
    G.add_edge(u_of_edge=a, v_of_edge=b, weight=w*5)
    #G.add_edge(u, v, weight=w)

for i in G:
    if i[0] == 1:
        color_map.append('blue')
    elif i[0] == 2:
        color_map.append('red')  
    elif i[0] == 3:
        color_map.append('grey')
    elif i[0] == 4:
        color_map.append('purple')  
    elif i[0] == 5:
        color_map.append('yellow') 

print(len(ok))
print(len(good))
print(len(bad))
print()

print(len(G.edges))
print(len(G.nodes))
#nx.coloring.greedy_color(G, strategy="largest_first")
#G.add_weighted_edges_from([[(i, i+1, abs(ok[i]['tweetSent']['pos'] - ok[i+1]['tweetSent']['pos'])) for i in range(len(ok) - 1)]]
       # [ (ok[i], ok[i+1], w)])
pos = nx.spring_layout
nx.draw(G,  node_color=color_map)
plt.show()
plt.savefig("okgraph.png")
