import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag
from collections import defaultdict
# Test
from lxml import etree
from tokenizer import tokenize,output_fifty_most_common_words

visited = defaultdict(int)
wordFreq = defaultdict(int)
longestPageURLCount = 0
longestPageURL = ""
subdomains = defaultdict(int)
text_list = []



def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
    """Given url and response object, if response is  """
    if not resp.error and resp.status == 200 and resp.raw_response != None:
        raw = resp.raw_response.content
        print(len(visited))
    else:
        return []
    #soup = BeautifulSoup(raw, 'html.parser')   # Regular parser from Python
    soup = BeautifulSoup(raw, "lxml")   # Third-party parser (It works faster and better than html.parser according to beautifulsoup website)
    # Testing out (Finding text contents)


    text_set = set()  # Set of texts from url
    for t in soup.find_all("p"):
        text_set.add(t.text)   # filters out duplicate content
        parseText = t.text
        for escape_char in ["\n","\t","\r"]:
            parseText = parseText.replace(escape_char, " ")
        word_count = tokenize(parseText,wordFreq)  ## modifies wordFreq in tokenize
        global longestPageURLCount
        global longestPageURL
        if word_count > longestPageURLCount:
            longestPageURLCount = word_count
            longestPageURL = url
        

    links = []
    for a in soup.find_all('a', href = True):
        #print("before=",a['href'],"after=",urljoin(url,a['href']))
        abs_url = urldefrag(urljoin(url,a['href']))[0]
        if(is_valid(abs_url)):
            parsed = urlparse(abs_url)
            #domain + path + params + query. Doesn't include scheme because some links have both http and https
            check_duplicate = parsed.netloc.lower() + parsed.path.lower() + parsed.params.lower() + parsed.query.lower()
            if(check_duplicate not in visited): #add to dict to avoid downloading a URL that has been crawled already
                visited[check_duplicate] = 0
                links.append(abs_url)

    #Question 4
    parsed = urlparse(url)
    if re.match(".*ics\.uci\.edu\/*", parsed.netloc) and len(links) > 0:
        sub = parsed.netloc.split(".")[0]
        if(sub != "www"):
            subdomains[parsed.netloc] += len(links)
    return links

def is_valid(url):
    try:
        parsed = urlparse(url)
        ##print("PARSED: ",parsed)
        path_params = parsed.path.lower().split("/")
        #remove empty strings
        for param in path_params:
            if param == "":
                path_params.remove(param)
        #Check to see that path params arent repeating, i.e, stayconnected/stayconnected/stayconnected/stayconnected
        if(len(set(path_params)) < len(path_params)):
            print("nice try                    bitch")
            return False
        if parsed.scheme not in set(["http", "https"]):
            return False
        if not re.match(r"(.*(ics\.uci\.edu\/*|cs\.uci\.edu\/*|informatics\.uci\.edu\/*|stat\.uci\.edu\/*|\.today\.uci\.edu\/department\/information_computer_sciences).*)", parsed.netloc):
            return False


        # Remove php from re.match if you don't want php links to be removed. I added it just in case.
        return re.match(r"(.*(\.ics\.uci\.edu\/*|\.cs\.uci\.edu\/|\.informatics\.uci\.edu\/|\.stat\.uci\.edu\/|today\.uci\.edu\/department\/information_computer_sciences).*)",
                        url) and not re.match(r".*php.*|.*dyn\/release\/api.*|.*\~kyoungwl\/links.*|.*\~minyounk.*|.*\~pfbaldi\/\?page=photo.*|.*flamingo.ics.uci.edu.*" + 
                        "|.*\~sgirish\/links.*|.*wics\-hosts\-a\-toy\-hacking.*|.*\~wscacchi.*|.*\~fielding\/pubs.*|.*\~hyungiko.*|.*\~dms/papers\/2001\/icdcs01_2.*|.*[2-99]\/\?tribe_event_display=past&tribe_paged=[1-6].*|" + 
                        ".*ca\/replicators.*|.*.mdogucu.ics.uci.edu\/teaching.*|.*photo-jan-.*|.*ics_x33.*|.*details.php.*|.*04-FabFlixsTestData.txt.*|.*ChainListHandout.*|" + 
                        ".*ProxmapHandout.*|.*DeepLearn17-Outline.*|.*dynamo.ics.uci.edu\/api\/.*|.*fano.ics.uci.edu.*|.*?afg+[0-90]+_page_id=1.*|.*sld.*|.*hall_of_fame\/index.php.*|" + 
                        ".*stayconnected\/index.php.*|.*=xml.*|.*attachment.*|.*php\/stayconnected.*|.*php\/mentor.*|.*php\/hall_of_fame.*|.*?share=twitter*|.*?share=facebook*|" + 
                        ".*?ical=1|.*java.io.*|.*java.util.*|.*java.lang.*|.*java.awt.*|.*mailman.*|.*machine-learning-databases.*|.*vod-detail-id.*|.*vod-type-id.*|.*replytocom.*|.*download.*|" + 
                        ".*calendar.*|.*Abstract.*|.*login.*|.*wics.ics.uci.edu/events.*|.*agelfand.*|.*emj.ics.uci.edu/.*|.*ics.uci.edu/honors.*|.*img.*|.*pdf.*|.*gallery.*|.*google.*|.*grape.ics.uci.edu.*|" + 
                        ".*cbcl.ics.uci.edu.*|.*swiki.ics.uci.edu.*|.*archive.ics.uci.edu/ml/datasets.php.*|.*welling.*|.*/page/.*|.*publication.*|.*openhouse.*",url) and not re.match(
                r".*(css|js|bmp|gif|jpe?g|ico"
                + r"|png|tiff?|mid|mp2|mp3|mp4|PMAV24Oct2012"
                + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf|ppsx|icdcs01_2|mat|\.m|\.Z"
                + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names|PDF|Thesis|thesis"
                + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso|img|supportICS"
                + r"|epub|dll|cnf|tgz|sha1|mpg|zImage_paapi|war|apk|tsv|java|svn|JPG"
                + r"|thmx|mso|arff|rtf|jar|csv|vlsisoc2010|CollabCom|DS_Store|gif"
                + r"|rm|smil|wmv|swf|wma|zip|rar|gz|c|py|h|ps.Z|lif|cp|scm|sql|db|R|pag|dir)$", url) and not re.match(
                    r".*~eppstein/pix.*|.*computableplant.ics.uci.edu/papers.*|.*intranet.ics.uci.edu.*|.*www-db.ics.uci.edu.*|.*doku.php/people.*|.*Ihler-Photos.*|.*theory/269.*|.*pubs.*|.*sli.ics.uci.edu.*|.*aviral/papers.*|.*cert.ics.uci.edu.*", url)
# Links that should/shouldn't be removed: .*\~ziv\/diss.*|.*\~fielding\/pubs.*|.*~dechter\/publications.*
# https://www.ics.uci.edu/~ziv/diss/, https://www.ics.uci.edu/~fielding/pubs/ , https://www.ics.uci.edu/~dechter/publications/
    except TypeError:
        print ("TypeError for ", parsed)
        raise
