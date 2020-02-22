import re
import requests
import time
from collections import defaultdict
#from tokenizer import tokenize,output_fifty_most_common_words
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag    

class Posting:
    def __init(self):
        self.docID = 0
        self.tf = 0
        self.df = 0
        self.word = ""
    def dfUpdate(self, df):
        self.df = df
    def idUpdate(self, id):
        self.docID = id
    def tfUpdate(self, tf):
        self.tf = tf

class InvertedIndex:
    def __init__(self):
        self.index = dict()
        self.postDict = dict()  # dictionary for Posting lists

    def __repr__(self):
        return str(self.index)

    def _isal(self, char):
        return  ((ord('A') <= ord(char) <= ord('Z')) or (ord('a') <= ord(char) <= ord('z')) or (ord(char) == ord("\'")))

    def Parse(self, text):
        word = ''
        wordList = []
        stemmer = PorterStemmer()
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
        # Indexer
        indexer = dict()

        # Get tokens from p tag and combine other tokens together in order to create indexer
        wordOccurence = dict()  # Number of times a word appear in a url
        sizeOfText = 0 # Total number of words in the url
        tfDict = dict() # Number of times a word appear in a url divided by the total number of words in the url
        df = {} # Number of urls that contain a word
        numOfUrls = len(urlList) # Use this to get idf (Number of urls divided by number of urls that contain a word)
        for url in urlList:
            id = id + 1
            x = requests.get(url)
            if x.status_code == 200:
                    soup = BeautifulSoup(x.content, "lxml")
                    parseAll = self.parsePage(soup)
                    sizeOfText = len(parseAll)
                    # Find the number of times a word appear in a url
                    for t in parseAll:
                        if t not in wordOccurence:
                            wordOccurence[t] = 1
                        else:
                            wordOccurence[t] += 1
                    # Getting tf for each words
                    for key in wordOccurence.keys():
                        tfDict[key] = wordOccurence[key] / sizeOfText
                    if id not in self.postDict:
                        self.postDict[id] = Posting()
                        self.postDict[id].idUpdate(id)

            time.sleep(0.5) # Politeness for requests.get(url)
        

def create_index(urlList):
    index = InvertedIndex()
    index.index_text(urlList)
    return index