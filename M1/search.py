import pickle
from nltk.stem import PorterStemmer

def intersection(l1, l2): 
    l3 = [value for value in l1 if value in l2] 
    return l3 

def get_key(val, my_dict):  #because stored as url:doc_id but we need to store it as doc_id:url
    for key, value in my_dict.items(): 
         if val == value: 
             return key 

if __name__ == "__main__":
    bookkeeper = pickle.load(open("docID_to_url.txt", "rb")) #keeps track of which doc_id is assigned to which url, need to store as doc_id:url instead of url:doc_id
    ps = PorterStemmer()
    while True:
        try:
            query = input("Search for: ").split(" ")
            if query[0] == "":
                print("Empty query. Exiting program")
                break
            else:
                results = []
                for item in query:
                    l = []
                    item = item.lower()
                    file_name = item[0] + ".txt"
                    file = open(file_name, 'rb')
                    index = pickle.load(file)
                    for p in index[ps.stem(item.lower())]:
                        for posting in p:
                            l.append(posting.docID)
                    results.append(l)

                if len(results) == 1: #only one search term
                    for i in range(5): #print top 5 results
                        print(get_key(results[0][i],bookkeeper))

                elif len(results) > 0: #finds the intersection of urls that contain all the words of the search terms
                    final_results = results[0]
                    for i in range(len(results)-1):
                        final_results = intersection(final_results, results[i+1])

                    for i in range(5): #print top 5 results
                        print(get_key(final_results[i], bookkeeper))

                else:
                    print("No results found.")
                    
        except Exception as e:
            print(str(e))
            break
