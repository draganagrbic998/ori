from projekat1_puzzle.puzzle import PuzzleProblem
from projekat1_puzzle.searchMulti import ExpectimaxAgent, RandomAgent, MinimaxAgent
from time import sleep
from projekat1_puzzle.search import heuristicValue
from PySide2 import QtCore
from projekat1_puzzle.search import aStarSearch

class ProtivnikWorkThread(QtCore.QThread):
    signal = QtCore.Signal(dict)

    def __init__(self, puzzle_problem, startState = None, depth = 3, iterNum = 20, agent ="Minimax"):
        QtCore.QThread.__init__(self)
        self.puzzle_problem = puzzle_problem
        self.startState = startState
        self.depth = depth
        self.iterNum = iterNum
        self.agent = agent

    def run(self):
        myAgent = MinimaxAgent(self.depth)

        if self.agent == "Expectimax":
            myAgent = ExpectimaxAgent(self.depth)

        myProtivnik = RandomAgent()

        state = self.puzzle_problem.getStartState()
        myAgent.protivnik = myProtivnik

        agentIndex = 0


        startValue = heuristicValue(state)

        emitVal = {"me": [state.content, startValue]}
        self.signal.emit(emitVal)
        sleep(1)


        for i in range(self.iterNum):

            if not agentIndex:

                temp = myAgent.get_action(self.puzzle_problem, state)
                emitVal = {"me": [temp.content, heuristicValue(temp)]}

            else:
                temp = myProtivnik.get_action(self.puzzle_problem, state)
                emitVal = {"enemy": [temp.content, heuristicValue(temp)]}


            state = temp
            self.signal.emit(emitVal)
            sleep(0.3)

            agentIndex = (agentIndex + 1) % 2

            if self.puzzle_problem.isGoalState(state):
                break

        emitVal = {"done": [state.content, "FIGHTING DONE. FINDING SOLUTION..."]}
        self.signal.emit(emitVal)
        sleep(0.1)
        self.puzzle_problem = PuzzleProblem(state.content, self.puzzle_problem.goal.content)
        path = aStarSearch(self.puzzle_problem)
        for i in path:
            if path.index(i) == len(path) - 1:
                self.signal.emit({"PUZZLE SOLVED IN {} STEPS".format(len(path) - 1) : [i.content]})
            else:
                self.signal.emit({"SOLVING PUZZLE..." : [i.content]})
            sleep(0.1)





