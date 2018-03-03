from pymongo import MongoClient
import sys
import codecs
from langdetect import detect
client = MongoClient('mongodb://localhost:27017/')
db1 = client.newsdb

def retrieve():
    #Setting a range beyond which translation is done
    nonbmpmap = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    newscursor = db1.news.distinct("articles.description")  #Retrieving text attribute from mongo
    lst = list()
    i = 0
    for iterate in newscursor:
        
        try:
            res = detect(iterate.translate(nonbmpmap))
            if res == 'en':
               # print(iterate.translate(nonbmpmap))
                lst.append(iterate.translate(nonbmpmap))   #Storing it in a list
                i = i + 1
                #print(i)
        except Exception as e :
            continue
    newsfile = codecs.open("newsfile.txt",'a','utf-8')
    for item in lst:
        newsfile.write(item)
        newsfile.write('\n')#Storing the tweets extracted  in a txt file
#retrieve()

