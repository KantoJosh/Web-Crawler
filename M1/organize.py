import pickle
from indexer import create_index, InvertedIndex, Posting
def main():
    i = 0
    final_result = InvertedIndex()
    #wordDict = dict(list()) #dict(set())   # Can delete this comment

    # Load all indexes into one InvertedIndex() (class object for index)
    for i in range(88):
        f = open("indexer"+str(i)+".txt", 'rb')
        #testDict = pickle.load(f)  # Can delete this comment
        #final_result.merge(testDict)   # Can delete this comment
        final_result.merge(pickle.load(f))
        f.close()

    # Extract all info from class object into wordDict
    for i in final_result.getDict():
        print(i, end = ' [')
        for postList in final_result.getDict()[i]:
            for post in postList:
                print(post.docID, end = ', ')
        print(']\n')

            # Need wordDict to work (Feel free to delete this comment)
            #if i not in wordDict:
                #wordDict[i] = list()
            #wordDict[i].append(post)
            # Set method
            #if i not in wordDict:
                #wordDict[i] = set()
            #wordDict[i].add(post)
    print("length of dict", len(final_result.getDict()))

    # (Feel free to delete this comment
    # Sorting wordDict based on docID
    # sorted() is used on set (wordDict[i])
    #for i in wordDict:
        #wordDict[i] = sorted(wordDict[i], key=lambda x: x.docID) # Set method
        #wordDict[i].sort(key=lambda x: x.docID)
        #for post in wordDict[i]:
            #print(i, post.docID)

    '''
    aDict = dict(list())
    bDict = dict(list())
    cDict = dict(list())
    dDict = dict(list())
    eDict = dict(list())
    fDict = dict(list())
    gDict = dict(list())
    hDict = dict(list())
    iDict = dict(list())
    jDict = dict(list())
    kDict = dict(list())
    lDict = dict(list())
    mDict = dict(list())
    nDict = dict(list())
    oDict = dict(list())
    pDict = dict(list())
    qDict = dict(list())
    rDict = dict(list())
    sDict = dict(list())
    tDict = dict(list())
    uDict = dict(list())
    vDict = dict(list())
    wDict = dict(list())
    xDict = dict(list())
    yDict = dict(list())
    zDict = dict(list())
    numDict = dict(list())

    # Creating separate dictionaries for each alphabet
    for i in wordDict:
        if i[0].lower() == 'a': # i is a string
            aDict[i] = wordDict[i]  # wordDict[i] ==> List of Posting()
        elif i[0].lower() == 'b':
            bDict[i] = wordDict[i]
        elif i[0].lower() == 'b':
            cDict[i] = wordDict[i]
        elif i[0].lower() == 'd':
            dDict[i] = wordDict[i]
        elif i[0].lower() == 'e':
            eDict[i] = wordDict[i]
        elif i[0].lower() == 'f':
            fDict[i] = wordDict[i]
        elif i[0].lower() == 'g':
            gDict[i] = wordDict[i]
        elif i[0].lower() == 'h':
            hDict[i] = wordDict[i]
        elif i[0].lower() == 'i':
            iDict[i] = wordDict[i]
        elif i[0].lower() == 'j':
            jDict[i] = wordDict[i]
        elif i[0].lower() == 'k':
            kDict[i] = wordDict[i]
        elif i[0].lower() == 'l':
            lDict[i] = wordDict[i]
        elif i[0].lower() == 'm':
            mDict[i] = wordDict[i]
        elif i[0].lower() == 'n':
            nDict[i] = wordDict[i]
        elif i[0].lower() == 'o':
            oDict[i] = wordDict[i]
        elif i[0].lower() == 'p':
            pDict[i] = wordDict[i]
        elif i[0].lower() == 'q':
            qDict[i] = wordDict[i]
        elif i[0].lower() == 'r':
            rDict[i] = wordDict[i]
        elif i[0].lower() == 's':
            sDict[i] = wordDict[i]
        elif i[0].lower() == 't':
            tDict[i] = wordDict[i]
        elif i[0].lower() == 'u':
            uDict[i] = wordDict[i]
        elif i[0].lower() == 'v':
            vDict[i] = wordDict[i]
        elif i[0].lower() == 'w':
            wDict[i] = wordDict[i]
        elif i[0].lower() == 'x':
            xDict[i] = wordDict[i]
        elif i[0].lower() == 'y':
            yDict[i] = wordDict[i]
        elif i[0].lower() == 'z':
            zDict[i] = wordDict[i]:
        else:
            numDict[i] = wordDict[i]
    '''

    
    '''
    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabetDict = dict(list())
    numDict = dict(list())
    for i in wordDict:
        if i[0].lower() not in alphabetDict and i[0].lower() in alphabetList:
            alphabetDict[i[0].lower()] = list()
        if i[0].lower() in alphabetList:
            alphabetDict[i[0].lower()].append(wordDict[i])
    for alpha in alphabetList:
        fileObject = open(alpha + ".txt", 'wb')
        pickle.dump(alphabetDict.items(), fileObject)
        fileObject.close()

    fileObject = open ('a.txt', 'rb')
    newDict = pickle.load(fileObject)
    for i in newDict:
        print(i)
    fileObject.close()
    '''
    # No sorted() is used
    #for i in wordDict:
    #    for docID in wordDict[i]:
    #        print(i, docID)
    
    #f = open("indexer1.txt", 'rb')
    #testDict = pickle.load(f)
    #for i in testDict:
    #    for post in testDict[i]:
    #        print(i, post.docID)
    #f.close()
    

if __name__ == "__main__":
    main()
