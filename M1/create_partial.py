import pickle
import math
import string
from indexer import InvertedIndex


def main():
    bookkeeper = dict()
    for letter in string.ascii_lowercase:
        inFile = open("tf_score_" + letter + ".txt", 'rb')
        outFile = open(letter +".txt", 'w')
        d = pickle.load(inFile)
        for token, info in d.items():
            bookkeeper[token] = outFile.tell()
            outFile.write("{}-{}\n".format(token, info))
        inFile.close()
        outFile.close()
    b = open("bookkeeper.txt", 'wb')
    pickle.dump(bookkeeper, b)
    b.close()



if __name__ == "__main__":
    main()