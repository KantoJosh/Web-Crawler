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
    #cwd = os.getcwd()
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
    #final_index = InvertedIndex()
    i = 0
    for folder in listFolder:
        index = create_index(urlDict[folder])
        filename = "indexer" + str(i) + ".txt"
        fileObject = open(filename, 'wb')
        pickle.dump(index.getDict(), fileObject)
        fileObject.close()
        i += 1
        #final_index.merge(index.getDict())


    
if __name__ == "__main__":
    main()
