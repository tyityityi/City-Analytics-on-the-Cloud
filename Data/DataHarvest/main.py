import couchdb
import tweepy
from tweepy import StreamListener, Stream
from urllib3.exceptions import ProtocolError

consumer_key = 'YcvSYZK29HNjlZogfbxkQUa69'
consumer_secret = 'XOAVX0LrptA93lCfPgRD09bIhUs5V4FlIAwyRExnSmRzAdi58t'
access_token = '1385773547256115201-aLwvlrKCpkLChvvt20op2zcT69VX92'
access_token_secret = 'lVmJTwV1Mpqw15DH1e2KqYuPxIoA3mRnhmQikWhaLtn12'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

try:
    couch = couchdb.Server('http://admin:password@172.26.130.232:5984/')
except:
    print("cannot find couchDB Server\n")
    raise

try:
    database = couch['twitter']
    print("link to twitter database")
except:
    couch.create('twitter')
    database = couch['twitter']
    print("create new 'twitter' database and link to it")


class twitterStream(StreamListener):

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
