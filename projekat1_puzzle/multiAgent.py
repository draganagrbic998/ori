from projekat1_puzzle.puzzle import PuzzleProblem
from projekat1_puzzle.searchMulti import ExpectimaxAgent, RandomAgent, MinimaxAgent
from time import sleep
from projekat1_puzzle.search import heuristic_value
from PySide2 import QtCore
from projekat1_puzzle.search import a_star_search

class ProtivnikWorkThread(QtCore.QThread):
    signal = QtCore.Signal(dict)

    def __init__(self, puzzle_problem, depth = 3, iter_num = 100, agent ="Expectimax"):
        QtCore.QThread.__init__(self)
        self.puzzle_problem = puzzle_problem
        self.depth = depth
        self.iter_num = iter_num
        self.agent = agent

    def run(self):

        if self.agent == "Expectimax":
            my_agent = ExpectimaxAgent(self.depth)
        else:
            my_agent = MinimaxAgent(self.depth)

        my_enemy = RandomAgent()

        state = self.puzzle_problem.getStartState()
        agentIndex = 0

        for i in range(self.iter_num):

            if not agentIndex:

                state = my_agent.get_action(self.puzzle_problem, state)
                emitVal = {"me": [state.content, heuristic_value(state)]}

            else:
                state = my_enemy.get_action(self.puzzle_problem, state)
                emitVal = {"enemy": [state.content, heuristic_value(state)]}


            self.signal.emit(emitVal)
            sleep(0.3)
            agentIndex = (agentIndex + 1) % 2

            if self.puzzle_problem.isGoalState(state):
                break

        emitVal = {"done": [state.content, "FIGHTING DONE. FINDING SOLUTION..."]}
        self.signal.emit(emitVal)
        sleep(0.1)
        self.puzzle_problem = PuzzleProblem(state.content, self.puzzle_problem.goal.content)
        path = a_star_search(self.puzzle_problem)
        for i in range(len(path)):
            state = path[i]
            if i == len(path) - 1:
                self.signal.emit({"PUZZLE SOLVED IN {} STEPS".format(len(path) - 1) : [state.content]})
            else:
                self.signal.emit({"SOLVING PUZZLE..." : [state.content]})
            sleep(0.1)





