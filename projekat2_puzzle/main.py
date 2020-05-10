
import time

from projekat2_puzzle.search import aStarSearch
from projekat2_puzzle.puzzle import PuzzleProblem


def main():

    print ("Slagalica se resava...")    #za sada samo da vidimo jel radi, kasnije dodajem PySide i gui da lepo vidimo slagalice
    start = time.time()
    mama =aStarSearch( PuzzleProblem([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]))
    end = time.time()
    print ("Proteklo vreme je " + str(end - start) + ".")
    return mama




if __name__ == '__main__':

    main()

