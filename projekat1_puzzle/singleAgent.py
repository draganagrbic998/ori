from time import sleep
from PySide2 import QtCore
from projekat1_puzzle.search import a_star_search

class AStarWorkThread(QtCore.QThread):

    signal = QtCore.Signal(list)

    def __init__(self, puzzle_problem):
        QtCore.QThread.__init__(self)
        self.puzzle_problem = puzzle_problem

    def run(self):
        self.signal.emit({"FINDING SOLUTION...": self.puzzle_problem.get_start_state().content})
        sleep(0.1)
        path = a_star_search(self.puzzle_problem)

        for i in range(len(path)):
            state = path[i]
            if i == len(path) - 1:
                self.signal.emit({"PUZZLE SOLVED IN {} STEPS".format(len(path) - 1) : state.content})
            else:
                self.signal.emit({"SOLVING PUZZLE..." : state.content})
            sleep(0.1)
