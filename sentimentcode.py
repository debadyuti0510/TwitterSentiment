from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from news_retrieve import search
import re
from collections import Counter
from newsstore import retrieve
import codecs
import spacy
from graphplot import plotsent

def SentimentScore (sentence):
    blob = TextBlob(sentence)
    score = blob.sentiment.polarity
    return score

nlp = spacy.load('en_core_web_sm')
tweetfile = codecs.open("tweetfile.txt", 'r','utf-8')
tweets = tweetfile.readlines()
s = set(stopwords.words('english'))
s.add('RT')
s.add('@')
s.add('\n')
#words = filter(lambda w: not w in s, tweets.split())
#words = re.findall(r,'\w+',tweets)
#name_tree = nltk.ne_chunk(nltk.tag.pos_tag(tweets.split()), binary=True)
words = list()
for tweetiterate in tweets:
    line = nlp(tweetiterate)
    for sent in line.sents:
        tmp = nlp(str(sent))
        for ent in tmp.ents:
            words.append(ent.text)
words = filter(lambda w: not w in s, words)
#print(words)
lower_words = [word.lower() for word in words]
word_count = Counter(words)
top_five = word_count.most_common(5)
print(top_five)
for key in top_five:
    search(key)

retrieve()
tweetfile.close()
tweetfile = codecs.open("tweetfile.txt",'r','utf-8')
tweets = tweetfile.readlines()
newsfile = codecs.open("newsfile.txt",'r','utf-8')
news = newsfile.readlines()
i = 0
for key in top_five:
    pos_count = 0
    neg_count = 0
    neu_count = 0
    total_count = 0
    news_count = 0
    pos_news = 0
    neg_news = 0
    neu_news = 0
    tweetlst = list()
    newslst = list()
    for tweetiterate in tweets:
        if key in tweetiterate.split():
            tweetlst.append(tweetiterate)
            total_count = total_count + 1
    for newsiterate in news:
        if key in newsiterate.split():
            newslst.append(newsiterate)
            news_count = news_count + 1
    for tweetiterate in tweetlst:
        score = SentimentScore(tweetiterate)
        if score > 0:
            pos_count = pos_count + 1
            
        elif score < 0:
            neg_count = neg_count + 1
        else:
            neu_count = neu_count + 1
    for newsiterate in newslst:
        news_score = SentimentScore(newsiterate)
        if news_score > 0:
            pos_news = pos_news + 1
            
        elif score < 0:
            neg_news = neg_news + 1
        else:
            neu_news = neu_news + 1
    plotsent(pos_count, neg_count, neu_count, str(key) + ' - Tweet')
    plotsent(pos_news, neg_news, neu_news, str(key) + ' - News')
    
        
        
            
    

