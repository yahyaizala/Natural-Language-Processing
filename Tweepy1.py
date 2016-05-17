#-*- coding:utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#import sys
consumer_key="consumer_key"
consumer_secret="consumer_secret"
access_token="access_token"
access_token_secret="access_token_secret"
''''
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text

me=api.followers()
for flow in me:
    print flow.screen_name
'''
import  json
class TSteamListener(StreamListener):
    def on_data(self, raw_data):
        with open("twets","a") as f:
            f.write(raw_data)
    def on_error(self, status_code):
        print status_code
if __name__ == '__main__':
    listener=TSteamListener()
    auth=OAuthHandler(consumer_key=consumer_key,consumer_secret=consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream=Stream(auth,listener)
    stream.filter(track=["deniz gezmis"])
    #tweets=json.loads(open("twets").read())
    #tweetText=[t["text"] for t in tweets]
    #print tweetText


