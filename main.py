
import re
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys

access_token = sys.argv[1]
access_token_secret = sys.argv[2]
consumer_key = sys.argv[3]
consumer_secret = sys.argv[4]


class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=[
     "#MagicBand",
     "#VisitPandora",
     "VisitPandora",
     "WaltDisneyWorld",
     "visitpandora",
     "#Disneyland",
     "#magickingdom",
     "#Epcot",
     "#EPCOT",
     "#epcot",
     "#animalkingdom",
     "#AnimalKingdom",
     "#disneyworld",
     "#DisneyWorld",
     "Disney's Hollywood Studios",
     "#WDW",
     "#disneyland",
     "#waltdisneyworld",
     "#disneylandparis",
     "#tokyodisneyland"])
