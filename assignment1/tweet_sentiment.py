import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    tweetcount = 0
    for i in fp:
        line = json.loads(i)
##                    opens twitter stream as Javascript object
        if u'text' in line:
##                   only 'opens' tweet if there is a text field
             tweetsent = 0
##                     sentiment of tweet
             tweetcount = tweetcount + 1
##                    tweet no.
             tweettext = line[u'text']
##                     tweet text content
             tweetwords = tweettext.split()
##                     splits tweet into component words
             for word in tweetwords:
                 if word in sent:
##                     print word, sent[word]
                     tweetsent = float(tweetsent) + float(sent[word])
        print str(tweetsent)
    
def dic():
##       this function creates a dictionary to map the words to sentiment scores
    global sent
    sent = {}
    for line in sent_file:
        sent[line.split()[0]] = line.rsplit()[-1]
        
def main():
    global sent_file
    sent_file = open(sys.argv[1])
    global tweet_file
    tweet_file = open(sys.argv[2])
    dic()
    lines(tweet_file)
    
    
if __name__ == '__main__':
    main()
    
