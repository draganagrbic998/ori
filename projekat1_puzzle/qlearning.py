from random import choice

class QLearningAgent:

    def __init__(self, puzzle_problem, alpha, discount):
        self.puzzle_problem = puzzle_problem
        self.alpha = alpha
        self.discount = discount
        self.qvalues = {}

    def reward(self, state):
        if self.puzzle_problem.is_goal_state(state):
            return 500.0
        return 0.0

    def get_value(self, state):
        qvalues = [self.get_qvalue(state, successor) for successor in self.puzzle_problem.get_successors(state)]
        return max(qvalues) if qvalues else 0.0

    def get_qvalue(self, state, next_state):
        if (state, next_state) not in self.qvalues:
            self.qvalues[(state, next_state)] = 0.0
        return self.qvalues[(state, next_state)]

    def get_state(self, state):

        successors = list(self.puzzle_problem.get_successors(state))
        if not successors:
            return None

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