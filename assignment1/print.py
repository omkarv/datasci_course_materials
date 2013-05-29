import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft")
load = json.load(response)


def load():
     print load
end
