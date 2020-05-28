from time import sleep
from PySide2 import QtCore
from projekat1_puzzle.qlearning import TabelarQLearningAgent, AproximativeQLearningAgent

class QLearningWorkThread(QtCore.QThread):

    signal = QtCore.Signal(dict)

    def __init__(self, puzzle_problem, iter_num = 5, alpha = 0.2, discount = 0.8, agent = "Tabelarni"):
        QtCore.QThread.__init__(self)
        self.puzzle_problem = puzzle_problem
        self.iter_num = iter_num
        self.alpha = alpha
        self.discount = discount
        self.agent = agent

    def run(self):

        emit_val = "TRAINING STARTED"
        self.signal.emit(emit_val)
        sleep(0.1)

        agent = self.training()
        emit_val = "TRAINING FINISHED"
        self.signal.emit(emit_val)
        sleep(1)

        emit_val = "SOLVING PUZZLE..."
        self.signal.emit(emit_val)
        sleep(0.1)

        state = self.puzzle_problem.get_start_state()
        path = []

        while not self.puzzle_problem.is_goal_state(state):
            state = agent.get_state(state)
            path.append(state)

        emit_val = "PUZZLE SOLVED IN {} STEPS".format(len(path) - 1)
        self.signal.emit(emit_val)

    def training(self):

        if self.agent == "Tabelarni":
            agent = TabelarQLearningAgent(self.puzzle_problem, self.alpha, self.discount)
        else:
            agent = AproximativeQLearningAgent(self.puzzle_problem, self.alpha, self.discount)

        state = self.puzzle_problem.get_start_state()

        if self.agent == "Tabelarni":
            for i in range(self.iter_num):
                self.signal.emit("ITERATION {} TRAINING...".format(i + 1))
                while True:
                    next_state = agent.get_state(state)
                    if not next_state:
                        break
                    agent.update(state, next_state)
                    state = next_state
                state = self.puzzle_problem.get_start_state()

            return agent

        else:
            self.signal.emit("TRAINING...")
            for i in range(100000):     #cackaj broj iteracija
                next_state = agent.get_state(state)
                agent.update(state, next_state)
                state = next_state
            return agent
