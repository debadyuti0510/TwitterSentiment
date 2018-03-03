# TwitterSentiment
# Precog
Python code modules for the tasks assigned in precog

The entire code is split into 5 modules:
### Module 1 : TweetFeed
**Description:** This module is used to grab random tweets from twitter streams using tweepy API

**Dependencies:** 
1.MongoClient from Pymongo
2.tweepy API and its sub modules
3.bson to make it possible to store the data in mongoDB

**Input:** No input required  
**Output:** Add 5000 tweets twice to mongoDB under twitterdb -> tweet1 and tweet2 collections

### Module 2 : tweetret
**Description:** This module is used to get json files from mongoDB back and extract the text content alone while writing to tweetfile.txt

**Dependencies:**
1.MongoClient from Pymongo
2.Counter from collections
3. sys and codecs to translate
4. langdetect to ensure the tweets are in English

**Input:** The twitter collection from pervious module i.e tweet1 and tweet2
**Output:** The text part of the json file in the files tweetfile.txt

### Module 3:sentimentcode
**Description:** Gets the named entities from tweetfile.txt and then finds the 5 most frequently occuring words. Then it calls search() and retrieve() from modules 4 and 5. Then, it does sentiment analysis and compares the polarity and calls plotsent() from module 6 to plot the comparison for each named entity. 
**Dependencies:**
1.re module
2.Collections from Counter
3.spacy for named entities
4.Module 4
5.Module 5
6.Module 6
7.codecs for encoding issues
8.nltk
**Input:**Tweetfile.txt  
**Output:** Final result with the plotted comparison

### Module 4: news_retrieve
**Description:** Gets the news for the keyword specified using news API and write to a mongoDB collection newsdb -> news

**Dependencies:**
1.NewsApiClient from newsapi
2.MongoClient from pymongo

**Input:** Keyword to search for i.e one of the named entities from module 3. 
**Output:** Writing newsapi Json files to mongoDB directly

### Module 5: newsstore
**Description:**Store the descriptions from the mongoDB records onto the file newsfile.txt.

**Dependencies:**
1.MongoClient from pymongo
2.sys
3.codecs
4.langdetect

**Input:** mongoDB collection having news
**Output:** News descriptions in the newsfile.txt
### Module 6: graphplot
**Description:**Plots the grap according to the sentiment data generated by the module 3. 

**Dependencies:**
1.numpy
2.matplotlib.pyplot

**Input:**The values that need to be plotted into a graph along with the title 
**Output:** Sentiment output for the input data in a graphical form.

All the respective text files and code modules have been uploaded 

**collection-2--1435878013956894491.wt, collection-4--1435878013956894491.wt, collection-8--1435878013956894491.wt ** - consists of the used collections of the mongoDB

