import tweepy
import json
from bson import json_util
from pymongo import MongoClient
CONSUMER_KEY = "97fOpMbhXgMDc8bTgXq9ybJMT"
CONSUMER_SECRET = "wIHtO7JHGkzjB5QpindcsrQ1JdINbAXA9jFSOvJfPZA4nrvVtp"
ACCESS_TOKEN = "422778126-HjWadB5Tk6x1ZwxgbEf3imT3dKMdBDszKYF73yPo"
ACCESS_TOKEN_SECRET = "yO92cNSdIvbdvH9Fbbw0ueWIbJ7iiWvLsjneuOauO1OcN"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
count=0
class Listener(tweepy.StreamListener):

    def on_data(self, data):
        try:
            data = json_util.loads(data)   #loading the json data into a python object
            client = MongoClient('mongodb://localhost:27017/')
            db = client.twitterdb   #Storing it into a local database called twitterdb
            db.tweet2.insert(data)
            print("yea")
            if db.tweet2.find().count() == 5000:
                exit()
            return True
        except Exception as e:      #Bypassing the exception that would be thrown
            return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    
    lis = Listener()
    #This handles Twitter authetification and the connection to Twitter Streaming API
    stream = tweepy.Stream(auth, lis)
    count = 0
    #This line filter Twitter Streams to capture data on random
    stream.filter(languages = ["en"], track = ['a', 'an', 'the', 'is', 'you'])
   
