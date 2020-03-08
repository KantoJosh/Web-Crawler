import pickle
import math
from collections import defaultdict
from indexer import create_index, InvertedIndex
def main():
    i = 0
    final_result = InvertedIndex()
    
    # Load all indexes into one InvertedIndex() (class object for index)
    for i in range(88):
        f = open("indexer"+str(i)+".txt", 'rb')
        final_result.merge(pickle.load(f))
        f.close()
        
    alphanumIndex = [dict() for i in range(27)] # length of alphabet + number = 26 + 1 = 27

    # Just printing out the outputs of a large index (Delete this if needed)
    #for key, value in final_result.getDict().items():
    #   for key2, value2 in value.items():
    #        print(key, key2, value2)

    tf_score = defaultdict()
    N = len(final_result.getDict().keys())   # Total number of documents/urls
    for key, value in final_result.getDict().items():   # key = "token" & value = dictionary
        df = len(value.keys()) # Get the number of documents/urls that contain "token"
        for key2, value2 in value.items():  # key2 = docID & value2 = tf
            tf_score[key][key2] = value2 * math.log(N/df, 10)   # tf * log(N/df); tf ==> (1 + log(tf) in indexer.py)
    # Creating separate dictionaries for each alphabet
    for i in tf-score:  # i is the "token" & tf_score[i] is the dictionary containing {docID:tf-idf}
        if 97 <= ord(i[0]) <= 122: # if the key of the index is part of english alphabet
            alphanumIndex[ord(i[0]) - 97][i] = tf_score[i]    # the first index selects which partial dictionary the key belongs to
                                                                            # the second index maps the key i to the value of the key i from the merged index
        else:
            alphanumIndex[26][i] = tf_score[i]                # the key is not part of eng. alphabet -> insert in number index
    '''
    for i in final_result.getDict():
        if 97 <= ord(i[0]) <= 122: # if the key of the index is part of english alphabet
            alphanumIndex[ord(i[0]) - 97][i] = final_result.getDict()[i]    # the first index selects which partial dictionary the key belongs to
                                                                            # the second index maps the key i to the value of the key i from the merged index
        else:
            alphanumIndex[26][i] = final_result.getDict()[i]                # the key is not part of eng. alphabet -> insert in number index
    '''

    ## create partial file for each letter and dump the dict into that file
    ASCII_code = 97 # ascii of 'a'
    for i in range(len(alphanumIndex)): # == 27
        if i == len(alphanumIndex)-1: # at the last index, reserved for numbers
            filename = "num"
        else:
            filename = chr(ASCII_code+i)
        
        fileObject = open(f"{filename}.txt","wb")
        pickle.dump(invIndexList[i],fileObject)
        fileObject.close()

if __name__ == "__main__":
    main()
