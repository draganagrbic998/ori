import time
from PySide2 import QtCore
from projekat1_puzzle.qlearning import QLearningAgent


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
            return 500.0
        return 0.0

    def obucavanje(self):
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


        for i in path:
            emitVal = {"reseno": i.content}
            self.signal.emit(emitVal)
            time.sleep(0.05)
