import re
from collections import defaultdict
#from tokenizer import tokenize,output_fifty_most_common_words
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from urllib.parse import urlparse, urljoin, urldefrag    

class InvertedIndex:
    def __init__(self):
        self.index = dict()
        self.docId = dict()

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
    
    def index_text(self, soup, url):
        # list of texts
        parseText = []
        parseTitle = []
        parseHeader = []
        parseBold = []
        # docID
        id = 0
        # Indexer
        indexer = dict()
        
        # Get tokens from title tag
        for t in soup.find_all("title"):
            parseTitle = self.Parse(t.text)

        # Get tokens from bold tag
        for t in soup.find_all("b"):
            parseBold = self.Parse(t.text)

        # Get tokens from header tags
        for t in soup.find_all(re.compile('^h[1-6]$')):
            parseHeader = self.Parse(t.text)

        # Get tokens from p tag and combine other tokens together in order to create indexer
        for t in soup.find_all("p"):
            id = id + 1
            parseText = self.Parse(t.text)  # Tokens
            parseAll = parseText + parseBold + parseHeader + parseTitle
            for token in parseAll:
                # Add posting into indexer (Find tf-idf and id for posting lists)
                if token not in indexer:
                    indexer[token] = [id, 0]
                else:
                    indexer[token].append([id, 0])

def create_index(soup, url):
    index = InvertedIndex()
    index.index_text(soup, url)
    return index