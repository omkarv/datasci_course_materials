import sys
import json

def lines(fp):
    for i in fp:
        line = json.loads(i)
##                    opens twitter stream as Javascript object
        if u'entities' in line:
             if u'hashtags' in line[u'entities']:
                 for dics in line[u'entities'][u'hashtags']:
                     if dics[u'text'] in hashcount:
                         hashcount[dics[u'text']] += float(1)
                     else:
                         hashcount[dics[u'text']] = float(1)

    hashcopy = hashcount.copy()
    while len(top_ten)<10:
       counts = hashcopy.values()
       maxcount = float(max(counts))
       for term in hashcount:
           if hashcount[term] == maxcount:
               key = term
               if len(top_ten)<10:
                   top_ten[key] = float(maxcount)
               del hashcopy[term]
    for item in top_ten:
        sys.stdout.write(item + ' ' + str(top_ten[item]) + "\n")
       
    

                        
                     
def dic():
##       this function creates a dictionary to map the words to sentiment scores
    global hashcount
    hashcount = {}
    global hashcopy
    hashcopy = {}
    global top_ten
    top_ten = {}


def main():
    global sent_file
    tweet_file = open(sys.argv[1])
    dic()
    lines(tweet_file)

if __name__ == '__main__':
    main()
