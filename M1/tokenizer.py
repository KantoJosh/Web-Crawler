import linecache
import re
import sys

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
