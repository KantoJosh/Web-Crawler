import pickle
from indexer import create_index, InvertedIndex, Posting
def main():
    i = 0
    final_result = InvertedIndex()
    
    # Load all indexes into one InvertedIndex() (class object for index)
    for i in range(88):
        f = open("indexer"+str(i)+".txt", 'rb')
        final_result.merge(pickle.load(f))
        f.close()
        
    alphanumIndex = [dict() for i in range(27)] # length of alphabet + number = 26 + 1 = 27
    # Creating separate dictionaries for each alphabet
    for i in final_result.getDict():
        if 97 <= ord(i[0]) <= 122: # if the key of the index is part of english alphabet
            alphanumIndex[ord(i[0]) - 97][i] = final_result.getDict()[i]    # the first index selects which partial dictionary the key belongs to
                                                                            # the second index maps the key i to the value of the key i from the merged index
        else:
            alphanumIndex[26][i] = final_result.getDict()[i]                # the key is not part of eng. alphabet -> insert in number index


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
