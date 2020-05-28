from abc import ABC
from random import random, choice
from projekat1_puzzle.search import heuristic_value

class QLearningAgent(ABC):

    def __init__(self, puzzle_problem, alpha, discount, epsilon = 0.05):
        self.puzzle_problem = puzzle_problem
        self.alpha = alpha
        self.discount = discount
        self.epsilon = epsilon
        self.qvalues = {}
        self.weights = {}
        self.features = {}

class AproximativeQLearningAgent(QLearningAgent):

    def __init__(self, puzzle_problem, alpha, discount, epsilon = 0.05):
        super().__init__(puzzle_problem, alpha, discount, epsilon)
        self.discount = 1
        self.alpha = 0.1

    def reward(self, state):
        if self.puzzle_problem.is_goal_state(state):
            return 100000000.0
        return -0.000001 * heuristic_value(state)

    def get_state(self, state):
        successors = list(self.puzzle_problem.get_successors(state))
        qvalues = [self.get_qvalue(state, successor) for successor in successors]
        maxq = max(qvalues)

        if random() < self.epsilon:
            return choice(successors)

        results = []
        for i in range(len(qvalues)):
            if qvalues[i] == maxq:
                results.append(i)
        return successors[choice(results)]

    def get_qvalue(self, state, next_state):

        suma = 0.0
        if (state, next_state) not in self.features:
            self.features[(state, next_state)] = heuristic_value(state) - heuristic_value(next_state)

        if (state, next_state) not in self.weights:
            self.weights[(state, next_state)] = 0.01

        suma += self.weights[(state, next_state)] * self.features[(state, next_state)]
        return suma

    def get_value(self, state):
        qvalues = [self.get_qvalue(state, successor) for successor in self.puzzle_problem.get_successors(state)]
        return max(qvalues) if qvalues else 0.0

    def update(self, state, next_state):
        difference = self.reward(next_state) + self.discount * self.get_value(next_state) - self.get_qvalue(state, next_state)
        self.weights[(state, next_state)] += self.alpha * difference * self.features[(state, next_state)]


class TabelarQLearningAgent(QLearningAgent):

    def reward(self, state):
        if self.puzzle_problem.is_goal_state(state):
            return 100.0
        return -1.0


    def get_value(self, state):
        qvalues = [self.get_qvalue(state, successor) for successor in self.puzzle_problem.get_successors(state)]
        return max(qvalues) if qvalues else 0.0

    def get_qvalue(self, state, next_state):
        if (state, next_state) not in self.qvalues:
            self.qvalues[(state, next_state)] = 0.0
        return self.qvalues[(state, next_state)]

    def get_state(self, state):

        if self.puzzle_problem.is_goal_state(state):
            return None
        successors = list(self.puzzle_problem.get_successors(state))

        if random() < self.epsilon:
            return choice(successors)

        qvalues = [self.get_qvalue(state, successor) for successor in successors]
        maxq = max(qvalues)
        results = []

        for i in range(len(qvalues)):
            if qvalues[i] == maxq:
                results.append(i)

        return successors[choice(results)]

    def update(self, state, next_state):
        difference = self.reward(next_state) + self.discount * self.get_value(next_state)
        self.qvalues[(state, next_state)] = self.alpha * difference + (1 - self.alpha) * self.get_qvalue(state, next_state)