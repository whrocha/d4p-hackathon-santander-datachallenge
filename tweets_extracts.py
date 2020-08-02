import datetime
import jsonpickle
import json
import pymongo
import tweepy

from pymongo import MongoClient

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, tweet):

        print("----- New Tweet ! ------")

        tweet_json = json.loads(jsonpickle.encode(tweet._json, unpicklable=False))
        tweet_db = db.tweet_stream_db
        tweet_db_id = tweet_db.insert_one(tweet_json).inserted_id

        print("Write at " + str(datetime.datetime.now()))

while True:

    try:

        print('Starting tweet extraction')

        client = pymongo.MongoClient("mongodb+srv://dbUser:@cluster0.vbnow.mongodb.net/hackathon_santander?retryWrites=true&w=majority")
        db = client.hackathon_santander

        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''

        OAuth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        OAuth.set_access_token(access_token, access_token_secret)

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

        filters = [
            '#compredopequeno',
            'comprar roupa',
            'comprar bebida',
            'comprar calça',
            'comprar comida',
            'comprar esportes',
        ]

        myStream.filter(track=filters)

    except Exception as e:

        print('Exception: ', e)

        pass
