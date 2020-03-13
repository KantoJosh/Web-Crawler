import pickle
from nltk.stem import PorterStemmer
import time
from collections import defaultdict
def intersection(l1, l2): 
    l3 = [value for value in l1 if value in l2] 
    return l3 


#def get_key(val, my_dict):  #because stored as url:doc_id but we need to store it as doc_id:url
#    for key, value in my_dict.items(): 
#         if val == value: 
#             return key 

STOP_WORDS = {'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 
'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 
'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', 
"here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', 
"it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 
'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 
'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", 
"they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", 
"we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 
'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves'}

if __name__ == "__main__":
    translate = pickle.load(open("docID_to_url.txt", "rb")) #keeps track of which doc_id is assigned to which url, need to store as doc_id:url instead of url:doc_id
    bookkeeper = pickle.load(open("bookkeeper.txt", "rb"))
    ps = PorterStemmer()
    while True:
        try:
            query = input("Search for: ").strip("\n").split(" ")
            start = time.time()
            
            for word in query:
                if word in STOP_WORDS:
                    query.remove(word)
            print("QUERY AFTER STOP WORD FILTER: ", query)
            if query[0] == "":
                print("Empty query. Exiting program")
                break
            elif len(query) == 1:
                item = ps.stem(query[0].lower()) #lowercase. need to stem
                #print(f"Item = {item}")
                file_name = item[0] + ".txt" #take first letter of term and open the corresponding index file
                file = open(file_name, 'r') #TODO: grab term from bookkeeper index and use seek() to retrieve token line
                offset = bookkeeper[item]# look for item from query in bookkeeper map
                file.seek(offset)
                result = file.readline().split("-")
                #print(f"Result = {result}")
                docID_map = eval(result[1]) # map of docIDs to tf scores

                with open("docID_to_url.txt","rb") as f:
                    urlDict = pickle.load(f)

                end = time.time()
                print("TIME = ", end - start)
                
                i = 10
                for docID in sorted(docID_map,key = lambda k: docID_map[k], reverse = True):
                    print(urlDict[docID])
                    i -= 1
                    if i == 0:
                        break
                file.close()
            else:
                combined_tfidf_score_map  = defaultdict(int)# maps docID to 
                results = []
                for item in query: #loop through each term in search query
                    l = []
                    item = ps.stem(item.lower()) #lowercase. need to stem
                    file_name = item[0] + ".txt" #take first letter of term and open the corresponding index file
                    file = open(file_name, 'r') #TODO: grab term from bookkeeper index and use seek() to retrieve token line
                    offset = bookkeeper[item]# look for item from query in bookkeeper map
                    file.seek(offset)
                    result = file.readline().split("-")
                    docID_map = eval(result[1]) # map of docIDs to tf scores

                    for docID in docID_map:
                        combined_tfidf_score_map[docID] += docID_map[docID]
                    

                with open("docID_to_url.txt","rb") as f:
                    urlDict = pickle.load(f)

                end = time.time()
                print("TIME = ", end - start)

                i = 10
                for docID in sorted(combined_tfidf_score_map,key = lambda k: docID_map[k], reverse = True):
                    print("AA")
                    print(urlDict[docID])
                    i -= 1
                    if i == 0:
                        break
                file.close() 
                    
            
        except Exception as e:
            print(str(e))
            break
