import re
import requests
import time
import math
import pickle
import json
from collections import defaultdict
from tokenizer import tokenize_regex, frequency
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag    
# Global variable
numOfIndexedDoc = 0
uniqueWords = set()
urlDict = dict()
docID = 0

# So you finish indexer w/ docID and tf first. Then use indexer (loop all) to get df for each word/docID...?

# Class for inverted index
class InvertedIndex:
    def __init__(self):
        self.index = dict(dict()) # indexer
        #self.postDict = dict()  # dictionary for Posting lists

    def __repr__(self):
        return str(self.index)

    def getDict(self):
        return self.index

    def merge(self, ArguIndex): # ArguIndex is a dictionary of dictionary {'token': {docId:tf, docID:tf,...}}
        for k in ArguIndex.keys():  # k is token
            if k in self.index:
                for j in ArguIndex[k].keys():   # j is docID
                    #j not in self.index[k]:
                    self.index[k][j] = ArguIndex[k][j]
            else:
                self.index[k] = ArguIndex[k]    # index[k] returns a dictionary
        #for k in index.keys():
        #    if k in self.index:
        #        self.index[k].append(index[k])
        #    else:
        #        self.index[k] = [index[k]]
        

    def parse(self, text):
        return tokenize_regex("[a-zA-Z]{2,}|\d{1,}",text)

    def parsePage(self, soup):
        return self.parse(soup.get_text())

    def frequency(self, soup):
        return frequency("[a-zA-Z]{2,}|\d{1,}",soup.get_text())

    def index_text(self, fileList, folder):
        # Get tokens from p tag and combine other tokens together in order to create indexer
        wordOccurence = dict()  # Number of times a word appear in a url   (KEEP)
        global uniqueWords
        global numOfIndexedDoc
        global urlDict
        global docID
        word_set = set()
        sizeOfText = 0 # Total number of words in the url (KEEP)
        tfDict = dict() # Number of times a word appear in a url divided by the total number of words in the url
        #df = {} # Number of urls that contain a word
        #numOfUrls = len(urlList) # Use this to get idf (Number of urls divided by number of urls that contain a word) (KEEP)
        for f in fileList:
            docID += 1
            numOfIndexedDoc += 1 # Number of indexed documents
            fileObj = open("DEV/" + folder + "/" + f, 'r')
            data = json.load(fileObj)
            urlDict[docID] = data['url']
            soup = BeautifulSoup(data['content'], "lxml") # Get delicious soup from html file
            tfDict = dict() #(KEEP)
            wordOccurence = self.frequency(soup)
            parseAll = self.parsePage(soup) # Tokenize and stem text into tokens (p, bold, headers, and title)

            # Getting tf for each words (Only works for one url for each iteration)
            for key in wordOccurence.keys():# (KEEP FOR LOOP)
                if wordOccurence[key] == 0:
                    tfDict[key] = 0
                else:
                    tfDict[key] = 1 + math.log(wordOccurence[key], 10)

            word_set.update(parseAll)  # Combines all words (from all urls inside urlDict)

            for t in parseAll:
                postDict = defaultdict()
                postDict[docID] = tfDict[key]
                #self.index[t] = postDict
                if t not in self.index:
                    self.index[t] = postDict
                else:
                    self.index[t][docID] = tfDict[key]


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
