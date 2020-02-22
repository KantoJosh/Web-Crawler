import json
import re
import sys
import os
import urllib
import time
import requests
from os import listdir
from os.path import isfile, join
from collections import defaultdict
from tokenizer import tokenize,output_fifty_most_common_words
from indexer import create_index
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag

postList = defaultdict(list)

def main():
    #if len(sys.argv) <= 1:
    #    print('Need a HTML/JSON file to open')
    #    exit()
    listFolder = []
    cwd = os.getcwd()
    print(cwd)
    listFolder = os.listdir("ANALYST")  # Gives a list of folder from the given folder
    data = []
    urlDict = defaultdict(list)
    urlNum = dict()
    urlNumInt = 0
    url = ''
    for folder in listFolder:
        files = []
        files = [f for f in listdir("ANALYST/"+folder) if isfile(join("ANALYST/"+folder, f))]
        for file in files:
            f = open("ANALYST/" + folder + "/" + file, 'r')
            data = json.load(f)
            url = data['url'] # Extracts url from json content (data)
            if url not in urlDict[folder]: # Check for duplicate urls
                urlDict[folder].append(url)
                urlNumInt += 1
        urlNum[folder] = urlNumInt # Number of urls from each folder (Just testing)
        urlNumInt = 0
    for folder in listFolder:
        create_index(urlDict[folder])
        #for url in urlDict[folder]:
            #x = requests.get(url)   # Requests html from the website
            #if x.status_code == 200:
            #    soup = BeautifulSoup(x.content, "lxml")
            #    index = create_index(soup, url)
                # Create indexer function here (Index texts w/ tokenization, stem, and so on)
            #time.sleep(0.5)
            #exit()
            
    #print(urlDict)
    ##### Testing out json and os functions #####
    #onlyfiles = [f for f in listdir("ANALYST\www_cs_uci_edu") if isfile(join("ANALYST\www_cs_uci_edu", f))]
    #data = {}   # Empty dict
    #for file in onlyfiles:
    #    f = open("ANALYST\www_cs_uci_edu\\" + file, 'r')
    #    data = json.load(f)
    #    url = ''
    #    url = data['url']
    #    print(url)
    #with open('test.json', 'r') as f:
    #    data = json.load(f)
    #print(data)
    #url = ''
    #url = data['url']
    #print(url)
    #i = 0
    #for file in onlyfiles:
    #    print(file)
    #    i = i + 1
    #    if i == 10:
    #        break
    
if __name__ == "__main__":
    main()
