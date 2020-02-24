import re
import requests
import time
import math
import pickle
from collections import defaultdict
#from tokenizer import tokenize,output_fifty_most_common_words
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag    

# Global variable
numOfIndexedDoc = 0
uniqueWords = set()

# Class for posting list
# So you finish indexer w/ docID and tf first. Then use indexer (loop all) to get df for each word/docID...?
class Posting:
    def __init(self):
        self.docID = 0
        self.tf = 0
    #    self.df = 0
        self.tfidf = 0

    #def dfUpdate(self):
    #    self.df = self.df + 1
    # Update docID
    def idUpdate(self, id):
        self.docID = id
    # Update tf
    def tfUpdate(self, tf):
        self.tf = tf
    # Update tf-idf
    def tfidfUpdate(self, tfidf):
        self.tfidf = tfidf
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
        self.index = dict(list()) # indexer
        #self.postDict = dict()  # dictionary for Posting lists

    def __repr__(self):
        return str(self.index)

    def getDict(self):
        return self.index

    def merge(self, index):
        return self.index.update(index)

    def _isal(self, char):
        return  ((ord('A') <= ord(char) <= ord('Z')) or (ord('a') <= ord(char) <= ord('z')) or (ord(char) == ord("\'")) or (ord('0') <= ord(char) <= ord('9')))

    def Parse(self, text):
        word = ''
        wordList = []
        stemmer = PorterStemmer()
        for escape_char in ["\n", "\t", "\r"]:
            text = text.replace(escape_char, " ")
        for char in text:
            if self._isal(char):    # Check for A-Z, a-z
                word += char
            else:
                if word != "":
                    if stemmer.stem(word.lower()) not in wordList:  # Check for duplicates
                        wordList.append(stemmer.stem(word.lower()))
                word = ""
        if word != "" and stemmer.stem(word.lower()) not in wordList:  # Just in case the last word will not be left out...
            wordList.append(stemmer.stem(word.lower()))
        return wordList

    def parsePage(self, soup):
        parseText = []
        parseTitle = []
        parseHeader = []
        parseBold = []
        for t in soup.find_all("title"):
            parseTitle = self.Parse(t.text)
        for t in soup.find_all("b"):
            parseBold = self.Parse(t.text)
        for t in soup.find_all(re.compile('^h[1-6]$')):
            parseHeader = self.Parse(t.text)
        for t in soup.find_all("p"):
            parseText = self.Parse(t.text)
        return parseText + parseTitle + parseHeader + parseBold
        

    def index_text(self, urlList):
        # docID
        id = 0

        # Get tokens from p tag and combine other tokens together in order to create indexer
        #wordOccurence = dict()  # Number of times a word appear in a url   (KEEP)
        global uniqueWords
        global numOfIndexedDoc
        wordDictionary = set()
        #sizeOfText = 0 # Total number of words in the url (KEEP)
        #tfDict = dict() # Number of times a word appear in a url divided by the total number of words in the url
        #df = {} # Number of urls that contain a word
        #numOfUrls = len(urlList) # Use this to get idf (Number of urls divided by number of urls that contain a word) (KEEP)
        for url in urlList:
            numOfIndexedDoc += 1 # Number of indexed documents
            id = id + 1 # id for docID
            x = requests.get(url)   # Get html file
            if x.status_code == 200:
                    soup = BeautifulSoup(x.content, "lxml") # Get delicious soup from html file
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

                    parseAll = list(set(parseAll)) # Removes duplicates 
                    wordDictionary.update(set(parseAll))  # Combines all words (from all urls inside urlDict)

                    for t in parseAll:
                        post = Posting()
                        post.idUpdate(id)
                        post.tfidfUpdate(0)
                    #    post.tfUpdate(tfDict.get(t)) (KEEP)
                        postList = []
                        postList.append(post)
                        if t not in self.index:
                            self.index[t] = postList
                        else:
                            self.index[t].append(post)

            time.sleep(0.5) # Politeness for requests.get(url)

        #tf = 0 (KEEP)
        uniqueWords.update(wordDictionary)
        #uniqueWords = uniqueWords | wordDictionary # wordDictionary is the set for one folder whereas uniqueWords is the set for all folders

        #for word in wordDictionary: # Calculating tf-idf (KEEP FOR LOOP)
        #    for postList in self.index.get(word):
        #        tf = postList.gettf()
        #        postList.tfidfUpdate(tf * (math.log(numOfUrls/len(self.index.get(word)))))
        

def create_index(urlList):
    index = InvertedIndex()
    index.index_text(urlList)
    print("Number of indexed documents:", numOfIndexedDoc)
    print("Number of unique words:", len(uniqueWords))
    return index