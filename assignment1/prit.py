import urllib
import json

pages = 1
pagesend = 10
urlstring = "http://search.twitter.com/search.json?q=cricket&page="

while pages <= pagesend:
     response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=" + str(pages))
     load = json.load(response)
     results = load[u'results']
     print 'page number is ' + str(pages)
     pages = pages + 1
     for i in results:
          print i[u'text'] + '\n'
          
          
     
     


