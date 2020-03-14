import pickle
import math
import string
from indexer import InvertedIndex


def main():
    bookkeeper = dict()
    alphabets = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    alphabets.append("num")
    for letter in alphabets:
        inFile = open("tf_score_" + letter + ".txt", 'rb')
        outFile = open(letter +".txt", 'w')
        d = pickle.load(inFile)
        for token, info in d.items():
            bookkeeper[token] = outFile.tell()
            outFile.write("{}-{}\n".format(token.encode('utf-8'), info))
        inFile.close()
        outFile.close()
    b = open("bookkeeper.txt", 'wb')
    pickle.dump(bookkeeper, b)
    b.close()



if __name__ == "__main__":
    main()
