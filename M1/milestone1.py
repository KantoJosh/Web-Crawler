import json
import re
import sys
import os
import urllib
import time
import requests
import pickle
from os import listdir
from os.path import isfile, join
from collections import defaultdict
#from tokenizer import tokenize,output_fifty_most_common_words
from indexer import create_index, InvertedIndex
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag

postList = defaultdict(list)

def main():
    #if len(sys.argv) <= 1:
    #    print('Need a HTML/JSON file to open')
    #    exit()
    listFolder = []
    cwd = os.getcwd()
    #print(cwd)
    listFolder = os.listdir("DEV")  # Gives a list of folder from the given folder
    data = []
    urlDict = defaultdict(list)
    urlNum = dict()
    urlNumInt = 0
    url = ''
    for folder in listFolder:
        files = []
        files = [f for f in listdir("DEV/"+folder) if isfile(join("DEV/"+folder, f))]
        for file in files:
            f = open("DEV/" + folder + "/" + file, 'r')
            data = json.load(f)
            url = data['url'] # Extracts url from json content (data)
            if url not in urlDict[folder]: # Check for duplicate urls
                urlDict[folder].append(url)
                urlNumInt += 1
        urlNum[folder] = urlNumInt # Number of urls from each folder (Just testing)
        urlNumInt = 0
    final_index = InvertedIndex()
    for folder in listFolder:
        index = create_index(urlDict[folder])
        final_index.merge(index.getDict())
        #for url in urlDict[folder]:
            #x = requests.get(url)   # Requests html from the website
            #if x.status_code == 200:
            #    soup = BeautifulSoup(x.content, "lxml")
            #    index = create_index(soup, url)
                # Create indexer function here (Index texts w/ tokenization, stem, and so on)
            #time.sleep(0.5)
            #exit()
    filename = "indexer.txt"
    fileObject = open(filename, 'wb')
    pickle.dump(final_index, fileObject)
    fileObject.close()
    fileObject = open(filename, 'r')
    new_index = pickle.load(fileObject)
    fileObject.close()

    
if __name__ == "__main__":
    main()
