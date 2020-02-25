import re
import requests
import time
import math
import pickle
import json
from collections import defaultdict
from tokenizer import tokenize_regex
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag    
# Global variable
numOfIndexedDoc = 0
uniqueWords = set()
urlDict = dict()
docID = 0

# Class for posting list
# So you finish indexer w/ docID and tf first. Then use indexer (loop all) to get df for each word/docID...?
class Posting:
    def __init__(self,tfidf):
        global docID
        self.docID = docID
        self.tf = 0
        #self.df = 0
        self.tfidf = tfidf
        docID += 1

    #def dfUpdate(self):
    #    self.df = self.df + 1
    # Update tf
    def tfUpdate(self, tf):
        self.tf = tf

    # Returns tf
    def gettf(self):
        return self.tf

    # Print docID and tf
    def print(self):
        print(self.docID, self.tf)
        
    # Print a list of docID and tf-idf
    def showList(self):
        print([self.docID, self.tfidf])

# Class for inverted index
class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(list()) # indexer
        #self.postDict = dict()  # dictionary for Posting lists

    def __repr__(self):
        return str(self.index)

    def getDict(self):
        return self.index

    def merge(self, index):
        return self.index.update(index)

    def parse(self, text):
        return tokenize_regex("[a-zA-Z]{2,}|\d{1,}",text)

    def parsePage(self, soup):
        return self.parse(soup.get_text())
        

    def index_text(self, fileList, folder):
        # Get tokens from p tag and combine other tokens together in order to create indexer
        #wordOccurence = dict()  # Number of times a word appear in a url   (KEEP)
        global uniqueWords
        global numOfIndexedDoc
        global urlDict
        global docID
        word_set = set()
        #sizeOfText = 0 # Total number of words in the url (KEEP)
        #tfDict = dict() # Number of times a word appear in a url divided by the total number of words in the url
        #df = {} # Number of urls that contain a word
        #numOfUrls = len(urlList) # Use this to get idf (Number of urls divided by number of urls that contain a word) (KEEP)
        for f in fileList:
            docID += 1
            numOfIndexedDoc += 1 # Number of indexed documents
            fileObj = open("DEV/" + folder + "/" + f, 'r')
            data = json.load(fileObj)
            urlDict[data['url']] = docID
            soup = BeautifulSoup(data['content'], "lxml") # Get delicious soup from html file
            #wordOccurence = dict() (KEEP)
            #tfDict = dict() (KEEP)
            parseAll = self.parsePage(soup) # Tokenize and stem text into tokens (p, bold, headers, and title)
            #sizeOfText = len(parseAll)  # Get the total size of tokens (KEEP)

            # Find the number of times a word appear in a url (Only works for one url for each iteration)
            #for t in parseAll: (KEEP FOR LOOP)
            #    if t not in wordOccurence:
            #        wordOccurence[t] = 1
            #    else:
            #        wordOccurence[t] += 1

            # Getting tf for each words (Only works for one url for each iteration)
            #for key in wordOccurence.keys(): (KEEP FOR LOOP)
            #    tfDict[key] = wordOccurence[key] / sizeOfText

            word_set.update(parseAll)  # Combines all words (from all urls inside urlDict)

            for t in parseAll:
                post = Posting(0)
                #post.tfUpdate(tfDict.get(t)) (KEEP)
                postList = [post]
                if t not in self.index:
                    self.index[t] = postList
                else:
                    self.index[t].append(post)


        #tf = 0 (KEEP)
        uniqueWords.update(word_set)
        #uniqueWords = uniqueWords | word_set # wordDictionary is the set for one folder whereas uniqueWords is the set for all folders

        #for word in word_set: # Calculating tf-idf (KEEP FOR LOOP)
        #    for postList in self.index.get(word):
        #        tf = postList.gettf()
        #        postList.tfidfUpdate(tf * (math.log(numOfUrls/len(self.index.get(word)))))
        

def create_index(fileList, folder):
    index = InvertedIndex()
    index.index_text(fileList, folder)
    print("Number of indexed documents:", numOfIndexedDoc)
    print("Number of unique words:", len(uniqueWords))
    return index