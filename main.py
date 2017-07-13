
import re
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API
access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


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
     "#Disneyland",
     "#universalstudios",
     "#universalstudiosFlorida",
     "#UniversalStudiosFlorida",
     "#universalstudioslorida",
     "#magickingdom",
     "#Epcot",
     "#EPCOT",
     "#epcot",
     "#animalkingdom",
     "#AnimalKingdom",
     "#disneyworld",
     "#DisneyWorld",
     "Disney's Hollywood Studios",
     "#Efteling",
     "#efteling",
     "De Efteling",
     "Universal Studios Japan",
     "#WDW",
     "#dubaiparksandresorts",
     "#harrypotterworld",
     "#disneyland",
     "#UniversalStudios",
     "#waltdisneyworld",
     "#disneylandparis",
     "#tokyodisneyland",
     "#themepark"])
