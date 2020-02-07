import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag
from collections import defaultdict

visited = defaultdict(int)

def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
    # Implementation requred.
    if not resp.error and resp.status == 200 and resp.raw_response != None:
        raw = resp.raw_response.content
    else:
        return []
    soup = BeautifulSoup(raw, 'html.parser')
    links = []
    for a in soup.find_all('a', href = True):
        #print("before=",a['href'],"after=",urljoin(url,a['href']))
        abs_url = urldefrag(urljoin(url,a['href']))[0]
        if(is_valid(abs_url)):
            parsed = urlparse(abs_url)
            check_duplicate = parsed.netloc.lower() + parsed.path.lower() + parsed.params.lower() + parsed.query.lower()
            if(check_duplicate not in visited):
                visited[check_duplicate] = 0
                links.append(abs_url)
    return links

def is_valid(url):
    try:
        parsed = urlparse(url)
        path_params = parsed.path.lower()
        
        #Check to see that path params arent repeating, i.e, stayconnected/stayconnected/stayconnected/stayconnected
        if(len(path_params) > 1):
            for i in range(len(path_params)-1):
                if(path_params[i] == path_params[i+1]):
                    return False

        if parsed.scheme not in set(["http", "https"]):
            return False
        return re.match(r"(.*(\.ics\.uci\.edu\/*|\.cs\.uci\.edu\/|\.informatics\.uci\.edu\/|\.stat\.uci\.edu\/|today\.uci\.edu\/department\/information_computer_sciences).*)",
                        url) and not re.match(r".*replytocom.*|.*pdf.*",url) and not re.match(
                r".*(css|js|bmp|gif|jpe?g|ico"
                + r"|png|tiff?|mid|mp2|mp3|mp4"
                + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf|ppsx"
                + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
                + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
                + r"|epub|dll|cnf|tgz|sha1"
                + r"|thmx|mso|arff|rtf|jar|csv"
                + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise
