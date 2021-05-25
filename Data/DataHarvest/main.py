# COMP90024     Group 66
# Ziyang Zhang 	1139552
# Yanjun Ma     1184516
# Tianyi Zheng 	1024493
# Yining Ding 	874213
# Zixin Zhang 	1087336
# Description   This document demonstrates how to harvest tweets by using twitter API and save the tweets into 'twitter' database in CouchDB

import couchdb
import tweepy
from tweepy import StreamListener, Stream
from urllib3.exceptions import ProtocolError

consumer_key = 'vkZtp8hpIapvdzJA7RJYgpSpR'
consumer_secret = 'VLJbzDxyXQQV2I85o72abZtiewSRHduzMS0PfoTOcTE4IR27D4'
access_token = '1385937899875553283-wcAfjYDfMmdlh1YcLVguTOvaqLWrOY'
access_token_secret = 'nJ7mKoXMNDSQBU2sWP62Owk3qvy9QyERsGYZq5r1uFVTT'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

try:
    couch = couchdb.Server('http://admin:password@172.26.130.232:5984/')
except:
    print("cannot find couchDB Server\n")
    raise

try:
    database = couch['twitter']
    print("link to ‘twitter’ database")
except:
    couch.create('twitter')
    database = couch['twitter']
    print("create new 'twitter' database and link to it")


class twitterStream(StreamListener):
    number = int(sys.argv[1]) if len(sys.argv) > 1 else 100

    def on_error(self, status):
        print(status)

    def on_status(self, status):
        id_str = status.id_str
        text = status.text
        try:
            location = status.place.name
        except AttributeError:
            location = status.place
        coordinates = status.geo
        language = status.lang
        friends_count = status.user.friends_count
        database.save({"id": id_str, "text": text, 'coordinates': coordinates, "location": location,
                       "language": language, "friends_count": friends_count})
        twitterStream.number -= 1
        if twitterStream.number == 0:
            exit(0)


l = twitterStream()
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

stream = Stream(auth, l)
api = tweepy.API(auth)

GEOBOX_AUSTRALIA = [113.338953078, -43.6345972634, 153.569469029, -10.6681857235]

while True:
    try:
        stream.filter(locations=GEOBOX_AUSTRALIA)
    except ProtocolError:
        continue
