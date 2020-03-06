import linecache
import re
import sys
import json
from nltk.stem import PorterStemmer
def get_stop_words(text_file):
    """Reads stop word file and adds to a set, returning it"""
    stop_words = set()
    with open(text_file) as file:
        for line in file:
            word = line.rstrip("\n")
            stop_words.add(word)
    return stop_words

def tokenize(text,freq):
    '''Reads text and modifies frequency of words in passed in dictionary'''
    STOP_WORDS = get_stop_words("stopwords.txt")
    token = []
    word_count = 0
    for char in text:
        if _isal(char):
            token.append(char)
        else:
            if len(token) > 1 and ''.join(token).lower() not in STOP_WORDS:
                word_count += 1
                freq[''.join(token).lower()] += 1
                token = []
    if len(token) > 1 and ''.join(token).lower() not in STOP_WORDS:
        freq[''.join(token).lower()] += 1
        word_count += 1
    
    return word_count
    #return freq

def tokenize_regex(exp,text):
    word_set = set()
    ps = PorterStemmer()
    for esc_char in ["\n","\r","\t"]:
            text = text.replace(esc_char," ")
    tokens = re.findall(exp,text)
    for word in tokens:
        word_set.add(ps.stem(word.lower()))
    return word_set

def frequency(exp, text):
    wordOccurence = dict()
    ps = PorterStemmer()
    for esc_char in ["\n","\r","\t"]:
            text = text.replace(esc_char," ")
    tokens = re.findall(exp,text)
    for word in tokens:
        if word not in wordOccurence:
            wordOccurence[word] = 1
        else:
            wordOccurence[word] += 1
    return wordOccurence

def _isal(char):
    '''Determines if char is alphanumeric (had to use my own version of isalnum 
    because the native version returns True for foreign characters)'''
    return  ((ord('A') <= ord(char) <= ord('Z')) or (ord('a') <= ord(char) <= ord('z')) or (ord(char) == ord("\'")))

def output_fifty_most_common_words(freq):
    i = 0
    MCwords = []
    for k in sorted(freq,key = lambda k: freq[k],reverse = True):
        if i > 100:
            break
        print(f"{k} = {freq[k]}")
        MCwords.append(freq[k])
        i += 1
    return MCwords


if __name__=="__main__":
    with open("/home/igessess/cs121/Assignment3/M1/ANALYST/www_cs_uci_edu/0a0056fb9a53ec6f190aa2b5fb1a97c33cd69726c8841f89d24fa5abd84d276c.json") as file:
        data = json.load(file)
        print(tokenize_regex("[a-zA-Z]{2,}|\d{1,}",data['content']))
