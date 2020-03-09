import pickle
import math
import string
from indexer import InvertedIndex

def main():
    alphabets = string.ascii_lowercase
    current_dict = dict()
    N = 55393

    for i in alphabets:
        f = open(i+ ".txt", 'rb')
        current_indexer = InvertedIndex()
        current_indexer.merge(pickle.load(f))

        tf_idf_score = dict()
        f.close()

        for token, dictionary in current_indexer.getDict().items():
            df = len(dictionary.keys())
            current_dict = dict()
            for docID, tf in dictionary.items():
                current_dict[docID] = round(tf * math.log(N/df, 10), 4)
            current_indexer.getDict()[token].clear()
            current_indexer.getDict()[token] = current_dict
                
        f = open("tf_score_"+i + ".txt", 'wb')
        pickle.dump(current_indexer.getDict(), f)
        f.close()

    
if __name__ == "__main__":
    main()
