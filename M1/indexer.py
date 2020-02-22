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
        wordList = list()
        stemmer = PorterStemmer()
        for char in text:
            if self._isal(char):    # Check for A-Z, a-z
                word += char
            else:
                if word != "":
                    wordList.append(stemmer.stem(word.lower()))
                word = ""
        if word != "":  # Just in case the last word will not be left out...
            wordList.append(stemmer.stem(word.lower()))
        return wordList
    
    def index_text(self, soup, url):
        parseText = []
        id = 0
        for t in soup.find_all("p"):
            id = id + 1
            parseText = self.Parse(t.text)  # Tokens

def create_index(soup, url):
    index = InvertedIndex()
    index.index_text(soup, url)
    return index