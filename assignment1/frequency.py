import sys
import json

def lines(fp):
    global dic
    wordcount = 0
    dic = {}
    for i in fp:
 
        line = json.loads(i)
##                    opens twitter stream as Javascript object
        if u'text' in line:
##                   only 'opens' tweet if there is a text field
             tweettext = line[u'text']
##                     tweet text content
             tweetwords = tweettext.split()
##                     splits tweet into component words
             for word in tweetwords:
                 if word in dic:
                     wordcount = wordcount + 1
                     dic[word] = dic[word] + 1
                 else:
                     wordcount = wordcount + 1
                     dic[word] = 1
    for words in dic:
        wfrequency = float(dic[words])/float(wordcount)
        print words.encode("utf-8") + '\t' + str(wfrequency)

   
    
def main():
    tweet_file = open(sys.argv[1])
    lines(tweet_file)
    
if __name__ == '__main__':
    main()
    
