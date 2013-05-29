import sys
import json

def lines(fp):
    for i in fp:
        line = json.loads(i)
##                    opens twitter stream as Javascript object
        if u'text' in line:
             tweetsent = 0
##                     sentiment of tweet
             tweettext = line[u'text']
##                     tweet text content
             tweetwords = tweettext.split()
##                     splits tweet into component word
             nowords = len(tweetwords)
##                     no of words in tweet -- not verified
             nosentwords = 0
##                     no of words with reliable sentiment in tweet 
             for word in tweetwords:
                 if word in sent:
                        tweetsent = float(tweetsent) + float(sent[word])
                        nosentwords = nosentwords + 1
             for word in tweetwords:
                 if word not in sent:
                        sentword = tweetsent / (nowords - nosentwords)
##                    average sentiment across all non sentiment tagged words in tweet
                        print word.encode("utf-8") + '\t' + str(sentword) 
                        newsent[word] = sentword
##                    add word to dictionary, with corresponding calculated sentiment
                 elif word in newsent:
##                    if word already added to new sentiment dictionary, use
##                     previously esimated value and sum to current estimation
                        sentword = newsent[word] + tweetsent/(nowords-nosentwords)
                        newsent[word] = sentword
                        print word.encode("utf-8") + '\t' + str(sentword) 
                        
                        
                     
def dic():
##       this function creates a dictionary to map the words to sentiment scores
    global sent
    global newsent
    sent = {}
    newsent = {}
    for line in sent_file:
        sent[line.split()[0]] = line.rsplit()[-1]

def main():
    global sent_file
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    dic()
    lines(tweet_file)

if __name__ == '__main__':
    main()
