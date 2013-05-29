import sys
import json

def lines(fp):
    global maxstate
    global maxstatesent
    maxstate = ""
    maxstatesent = 0
    for i in fp:
        line = json.loads(i)
##                    opens twitter stream as Javascript object

        if u'lang' in line:
            if "en" not in line[u'lang']:
                continue
##                    only parse if in english
        placenotfound=1
        global tweetstate
        tweetstate = ""
        while placenotfound==1:
            if u'place' in line:
                if line[u'place'] != None:
                  if line[u'place'][u'country'] == "United States":
                      for state in usstates.keys():
                          if state in line[u'place'][u'full_name']:
                             tweetstate = usstates[state]
                             placenotfound=0
         
            if u'user' in line:
                if u'location' in line[u'user']:
                     for state in usstates.keys():
                         if state in line[u'user'][u'location']:
                             tweetstate = usstates[state]
                             placenotfound=0
##            if u'coordinates' in line:
##                if line[u'coordinates'] != None:
##                    print line[u'coordinates'][u'coordinates']
##
            placenotfound = 0
                                            
        if u'text' in line and len(tweetstate)>0:
##                   only 'opens' tweet if there is a text field
             tweetsent = 0
##                     sentiment of tweet
             tweettext = line[u'text']
##                     tweet text content
             tweetwords = tweettext.split()
##                     splits tweet into component words
             for word in tweetwords:
                 if word in sent:
##                     print word, sent[word]
                     tweetsent = float(tweetsent) + float(sent[word])
             statesent[tweetstate] =+ tweetsent
    
    for state in statesent:
        if statesent[state] > maxstatesent:
            maxstatesent = statesent[state]
            maxstate = state
    print maxstate                    
            

def dic():
##       this function creates a dictionary to map the words to sentiment scores
    global sent
    sent = {}
    for line in sent_file:
        sent[line.split()[0]] = line.rsplit()[-1]

    global usstates
    usstates = {"Alabama":"AL", "Alaska": "AK" ,"Arizona": "AZ" ,"Arkansas": "AR" ,"California": "CA","Colorado": "CO","Connecticut": "CT" ,"Delaware": "DE" ,"Florida": "FL" ,"Georgia": "GA" ,"Hawaii": "HI","Idaho": "ID" ,"Illinois": "IL","Indiana": "IN" ,"Iowa": "IA","Kansas": "KS" ,"Kentucky": "KY" ,"Louisiana": "LA" ,"Maine": "ME" ,"Maryland": "MD" ,"Massachusetts": "MA" ,"Michigan": "MI" ,"Minnesota": "MN" ,"Mississippi": "MS" ,"Missouri": "MO" ,"Montana": "MT" ,"Nebraska": "NE" ,"Nevada": "NV" ,"New Hampshire": "NH" ,"New Jersey": "NJ" ,"New Mexico": "NM" ,"New York": "NY" ,"North Carolina": "NC" ,"North Dakota": "ND" ,"Ohio": "OH" ,"Oklahoma": "OK" ,"Oregon": "OR" ,"Pennsylvania": "PA" ,"Rhode Island": "RI" ,"South Carolina": "SC" ,"South Dakota": "SD" ,"Tennessee": "TN" ,"Texas": "TX" ,"Utah": "UT" ,"Vermont": "VT","Virginia": "VA" ,"Washington": "WA" ,"West Virginia":"WV" ,"Wisconsin": "WI" ,"Wyoming": "WY"}

    global statesent
    statesent ={}
    for tla in usstates.values():
        statesent[tla] = 0
  
        
    
        
def main():
    global sent_file
    sent_file = open(sys.argv[1])
    global tweet_file
    tweet_file = open(sys.argv[2])
    dic()
    lines(tweet_file)
    
    
if __name__ == '__main__':
    main()
    
