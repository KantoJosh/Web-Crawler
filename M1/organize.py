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
    for i in final_result.getDict():
        if i[0].lower() == 'a': # i is a string
            aDict[i] = final_result.getDict()[i]  # wordDict[i] ==> List of Posting()
        elif i[0].lower() == 'b':
            bDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'b':
            cDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'd':
            dDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'e':
            eDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'f':
            fDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'g':
            gDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'h':
            hDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'i':
            iDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'j':
            jDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'k':
            kDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'l':
            lDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'm':
            mDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'n':
            nDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'o':
            oDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'p':
            pDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'q':
            qDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'r':
            rDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 's':
            sDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 't':
            tDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'u':
            uDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'v':
            vDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'w':
            wDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'x':
            xDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'y':
            yDict[i] = final_result.getDict()[i]
        elif i[0].lower() == 'z':
            zDict[i] = final_result.getDict()[i]
        else:
            numDict[i] = final_result.getDict()[i]

    # Creating separate indexers
    fileObject = open("a.txt", 'wb')
    pickle.dump(aDict, fileObject)
    fileObject.close()

    fileObject = open("b.txt", 'wb')
    pickle.dump(bDict, fileObject)
    fileObject.close()

    fileObject = open("c.txt", 'wb')
    pickle.dump(cDict, fileObject)
    fileObject.close()

    fileObject = open("d.txt", 'wb')
    pickle.dump(dDict, fileObject)
    fileObject.close()

    fileObject = open("e.txt", 'wb')
    pickle.dump(eDict, fileObject)
    fileObject.close()

    fileObject = open("f.txt", 'wb')
    pickle.dump(fDict, fileObject)
    fileObject.close()
    
    fileObject = open("g.txt", 'wb')
    pickle.dump(gDict, fileObject)
    fileObject.close()

    fileObject = open("h.txt", 'wb')
    pickle.dump(hDict, fileObject)
    fileObject.close()

    fileObject = open("i.txt", 'wb')
    pickle.dump(iDict, fileObject)
    fileObject.close()

    fileObject = open("j.txt", 'wb')
    pickle.dump(jDict, fileObject)
    fileObject.close()

    fileObject = open("k.txt", 'wb')
    pickle.dump(kDict, fileObject)
    fileObject.close()

    fileObject = open("l.txt", 'wb')
    pickle.dump(lDict, fileObject)
    fileObject.close()

    fileObject = open("m.txt", 'wb')
    pickle.dump(mDict, fileObject)
    fileObject.close()

    fileObject = open("n.txt", 'wb')
    pickle.dump(nDict, fileObject)
    fileObject.close()

    fileObject = open("o.txt", 'wb')
    pickle.dump(oDict, fileObject)
    fileObject.close()

    fileObject = open("p.txt", 'wb')
    pickle.dump(pDict, fileObject)
    fileObject.close()

    fileObject = open("q.txt", 'wb')
    pickle.dump(qDict, fileObject)
    fileObject.close()

    fileObject = open("r.txt", 'wb')
    pickle.dump(rDict, fileObject)
    fileObject.close()

    fileObject = open("s.txt", 'wb')
    pickle.dump(sDict, fileObject)
    fileObject.close()

    fileObject = open("t.txt", 'wb')
    pickle.dump(tDict, fileObject)
    fileObject.close()

    fileObject = open("u.txt", 'wb')
    pickle.dump(uDict, fileObject)
    fileObject.close()

    fileObject = open("v.txt", 'wb')
    pickle.dump(vDict, fileObject)
    fileObject.close()

    fileObject = open("w.txt", 'wb')
    pickle.dump(wDict, fileObject)
    fileObject.close()

    fileObject = open("x.txt", 'wb')
    pickle.dump(xDict, fileObject)
    fileObject.close()

    fileObject = open("y.txt", 'wb')
    pickle.dump(yDict, fileObject)
    fileObject.close()

    fileObject = open("z.txt", 'wb')
    pickle.dump(zDict, fileObject)
    fileObject.close()

    fileObject = open("num.txt", 'wb')
    pickle.dump(numDict, fileObject)
    fileObject.close()


if __name__ == "__main__":
    main()
