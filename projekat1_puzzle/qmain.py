import time
from PySide2 import QtCore
from projekat1_puzzle.qlearning import QLearningAgent


class QLearningWorkThread(QtCore.QThread):
    signal = QtCore.Signal(dict)

    def __init__(self, puzzle_problem, iterNum = 20, alpha = 0.2, discount = 0.8):
        QtCore.QThread.__init__(self)
        self.puzzle_problem = puzzle_problem
        self.iterNum = iterNum
        self.alpha = alpha
        self.discount = discount

    def run(self):
        self.qLearning()

    def reward(self, problem, state):
        if problem.isGoalState(state):
            return 500.0
        return 0.0

    def obucavanje(self):
        agent = QLearningAgent(self.puzzle_problem, self.alpha, self.discount)
        state = self.puzzle_problem.getStartState()

        for i in range(self.iterNum):
            nextState = agent.computeStateFromQValue(state)
            agent.update(state, nextState, self.reward(self.puzzle_problem, nextState))
            state= nextState
            if i % 50000 == 0:
                self.signal.emit("TRAINING ITERATION: {}...".format(i))
        return agent

    def qLearning(self):
        state = self.puzzle_problem.getStartState()
        path = []

        emitVal = "TRAINING STARETED..."
        self.signal.emit(emitVal)
        time.sleep(0.1)

        agent = self.obucavanje()

        emitVal = "TRAINING FINISHED"
        self.signal.emit(emitVal)
        time.sleep(1)

        emitVal = "SOLVING PUZZLE..."
        self.signal.emit(emitVal)
        time.sleep(0.3)

        while not self.puzzle_problem.isGoalState(state):
            state = agent.computeStateFromQValue(state)
            path.append(state)


        emitVal = "PUZZLE SOLVED IN {} STEPS".format(len(path))
        self.signal.emit(emitVal)

