import json
import re
import sys
import os
from os import listdir
from os.path import isfile, join
from collections import defaultdict
from tokenizer import tokenize,output_fifty_most_common_words
#from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag

postList = defaultdict(list)

def main():
    #if len(sys.argv) <= 1:
    #    print('Need a HTML/JSON file to open')
    #    exit()
    listFile = []
    listFile = os.listdir("ANALYST")
    onlyfiles = [f for f in listdir("ANALYST\www_cs_uci_edu") if isfile(join("ANALYST\www_cs_uci_edu", f))]
    data = {}   # Empty dict
    for file in onlyfiles:
        f = open("ANALYST\www_cs_uci_edu\\" + file, 'r')
        data = json.load(f)
        url = ''
        url = data['url']
        print(url)
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
