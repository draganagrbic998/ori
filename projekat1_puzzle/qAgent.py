from time import sleep
from PySide2 import QtCore
from projekat1_puzzle.qlearning import QLearningAgent

class QLearningWorkThread(QtCore.QThread):

    signal = QtCore.Signal(dict)

    def __init__(self, puzzle_problem, iter_num = 20, alpha = 0.2, discount = 0.8):
        QtCore.QThread.__init__(self)
        self.puzzle_problem = puzzle_problem
        self.iter_num = iter_num
        self.alpha = alpha
        self.discount = discount

    def run(self):
        state = self.puzzle_problem.get_start_state()
        path = []

        emitVal = "TRAINING STARETED..."
        self.signal.emit(emitVal)
        sleep(0.1)

        agent = self.training()

        emitVal = "TRAINING FINISHED"
        self.signal.emit(emitVal)
        sleep(1)

        emitVal = "SOLVING PUZZLE..."
        self.signal.emit(emitVal)
        sleep(0.3)

        while not self.puzzle_problem.is_goal_state(state):
            state = agent.get_state(state)
            path.append(state)

        emitVal = "PUZZLE SOLVED IN {} STEPS".format(len(path))
        self.signal.emit(emitVal)

    def training(self):
        agent = QLearningAgent(self.puzzle_problem, self.alpha, self.discount)
        state = self.puzzle_problem.get_start_state()

        for i in range(5):
            self.signal.emit("ITERATION {} TRAINING".format(i + 1))
            while True:
                next_state = agent.get_state(state)
                if not next_state:
                    break
                agent.update(state, next_state)
                state = next_state
            state = self.puzzle_problem.get_start_state()
        return agent

