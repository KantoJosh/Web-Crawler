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
from indexer import create_index, InvertedIndex, urlDict, numOfIndexedDoc
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag


def main():
    listFolder = os.listdir("DEV")  # gets list of sub folder names in DEV/
    urlNum = dict()
    i = 0
    for folder in listFolder:
        files = [f for f in listdir("DEV/"+folder) if isfile(join("DEV/"+folder, f))] # every file in var folder
        index = create_index(files, folder) # one index per folder in DEV
        filename = "indexer" + str(i) + ".txt"
        fileObject = open(filename, 'wb')           # create partial index per subfolder
        pickle.dump(index.getDict(), fileObject)        # dump the dictionary of the index into a file 
        fileObject.close()                     
        urlNum[folder] = 0 # Number of urls from each folder (Just testing)
        i += 1
    pickle.dump(urlDict, open('docID_to_url.txt', 'wb'))
    


    
if __name__ == "__main__":
    main()
