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


def main():
    #if len(sys.argv) <= 1:
    #    print('Need a HTML/JSON file to open')
    #    exit()
    #cwd = os.getcwd()
    #print(cwd)
    listFolder = os.listdir("DEV")  # Gives a list of folder from the given folder
    #data = []
    #urlDict = dict()
    urlNum = dict()
    urlNumInt = 0
    #url = ''
    i = 0
    #docID = 0
    for folder in listFolder:
        files = []
        files = [f for f in listdir("DEV/"+folder) if isfile(join("DEV/"+folder, f))]
        index = create_index(files, folder) # one index per folder in DEV
        filename = "indexer" + str(i) + ".txt"
        fileObject = open(filename, 'wb')
        pickle.dump(index.getDict(), fileObject)
        fileObject.close()
        i += 1
        urlNum[folder] = urlNumInt # Number of urls from each folder (Just testing)
        urlNumInt = 0
    #final_index = InvertedIndex()
    '''
    i = 0
    for folder in listFolder:
        index = create_index(urlDict[folder])
        filename = "indexer" + str(i) + ".txt"
        fileObject = open(filename, 'wb')
        pickle.dump(index.getDict(), fileObject)
        fileObject.close()
        i += 1
        #final_index.merge(index.getDict())
    '''


    
if __name__ == "__main__":
    main()
