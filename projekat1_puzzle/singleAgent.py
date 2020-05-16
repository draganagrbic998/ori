import time
from PySide2 import QtCore
from projekat1_puzzle.search import aStarSearch

class AStarWorkThread(QtCore.QThread):
    signal = QtCore.Signal(list)

    def __init__(self, puzzle_problem, startState = None):
        QtCore.QThread.__init__(self)
        self.puzzle_problem = puzzle_problem
        self.startState = startState

    def run(self):
        self.signal.emit({"FINDING SOLUTION...": self.puzzle_problem.getStartState().content})
        time.sleep(0.1)
        path = aStarSearch(self.puzzle_problem)
        for i in path:
            if path.index(i) == len(path) - 1:
                self.signal.emit({"PUZZLE SOLVER IN {} STEPS".format(len(path) - 1) : i.content})
            else:
                self.signal.emit({"SOLVING PUZZLE..." : i.content})
            time.sleep(0.1)
