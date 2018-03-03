from newsapi import NewsApiClient
from pymongo import MongoClient


client = MongoClient()
db1 = client.newsdb


def search(keyWord):
    api = NewsApiClient(api_key = '')
    Content = api.get_everything(q = keyWord)
    db1.news.insert(Content)
   # print(Content)


#search('Trump')
