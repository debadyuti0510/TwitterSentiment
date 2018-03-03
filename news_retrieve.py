from newsapi import NewsApiClient
from pymongo import MongoClient


client = MongoClient()
db1 = client.newsdb


def search(keyWord):
    api = NewsApiClient(api_key = 'efb410a05f3e4fb2a775bdc360509a17')
    Content = api.get_everything(q = keyWord)
    db1.news.insert(Content)
   # print(Content)


#search('Trump')
