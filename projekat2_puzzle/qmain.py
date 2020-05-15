import time

from PySide2 import QtCore

from projekat2_puzzle.puzzle import PuzzleProblem
from projekat2_puzzle.qlearning import QLearningAgent


class QLearningWorkThread(QtCore.QThread):
    signal = QtCore.Signal(dict)

    def __init__(self, puzzle_problem, iterNum = 20):
        QtCore.QThread.__init__(self)
        self.puzzle_problem = puzzle_problem
        self.iterNum = iterNum

    def run(self):
        self.qLearning()

    def reward(self, problem, state):
        if problem.isGoalState(state):
            return 500.0  #ako smo pobedili, nagradimo agenta
        return 0.0

    def obucavanje(self):
        #iter_num => koliko iteracija obucavamo agenta
        #problem = PuzzleProblem([1, 0, 4, 2, 5, 3, 8, 7, 6], [1, 2, 3, 4, 5, 6, 7, 8, 0])
        agent = QLearningAgent(self.puzzle_problem, 0.2, 0.8)
        state = self.puzzle_problem.getStartState()

        for i in range(self.iterNum):
            nextState = agent.computeStateFromQValue(state)
            agent.update(state, nextState, self.reward(self.puzzle_problem, nextState))
            state= nextState

        return agent

    def qLearning(self):
        state = self.puzzle_problem.getStartState()
        path = []

        emitVal = {"OBUCAVANJE ZAPOCETO!" : state.content}
        self.signal.emit(emitVal)
        time.sleep(0.1)

        agent = self.obucavanje()
        print ("ZAVRSENO OBUCAVANJE!")

        emitVal = {"ZAVRSENO OBUCAVANJE!" : state.content}
        self.signal.emit(emitVal)
        time.sleep(1)

        emitVal = {"TRAZI SE RESENJE!" : state.content}
        self.signal.emit(emitVal)
        time.sleep(0.3)

        while not self.puzzle_problem.isGoalState(state):
            state = agent.computeStateFromQValue(state)
            path.append(state)

        print ("RESENO!")   #za sada sam testirala na slagalici na kojoj sam obucavala agenta, nju resi poprilicno brzo, kasnije cu
                            #videti kako radi za slagalice koje nisu iz obucavajuceg skupa, sad mi se sklapaju oci :D
        print(len(path))
        for i in path:
            emitVal = {"reseno": i.content}
            self.signal.emit(emitVal)
            time.sleep(0.05)
            #print (i)