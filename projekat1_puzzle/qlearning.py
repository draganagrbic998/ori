
import random

class QLearningAgent:

    def __init__(self, puzzle_problem, alpha, discount):
        self.q_values = {}
        self.alpha = alpha
        self.discount = discount
        #discount cu staviti da je 0.8
        #alpha cu uzeti da je 0.2 za pocetak
        self.puzzle_problem = puzzle_problem

    def getQValue(self, state1, state2):
        #ovo cu zvati iz fja, ne sama direktno
        if (state1, state2) not in self.q_values:
            self.q_values[(state1, state2)] = 0.0
        return self.q_values[(state1, state2)]

    def computeValueFromQValues(self, state):
        #ovo cu zvati iz fja, ne sama direktno
        q_values = [self.getQValue(state, successor) for successor in self.puzzle_problem.getSuccessors(state)]
        return max(q_values) if q_values else 0.0
    #DODAJ DA SE NE PRAVE DECA OD POBEDNICKOG STANJA

    def computeStateFromQValue(self, state):

        successors = self.puzzle_problem.getSuccessors(state)
        successors = list(successors)
        if not successors:
            return None

        q_values = [self.getQValue(state, successor) for successor in successors]
        results = []
        max_q = max(q_values)
        for i in range(len(q_values)):
            if q_values[i] == max_q:
                results.append(i)

        return successors[random.choice(results)]

    def getState(self, state):
        #dodaj greedy search ovde
        return self.computeStateFromQValue(state)


    def update(self, state, nextState, reward):
        difference = reward + self.discount * self.computeValueFromQValues(nextState)
        self.q_values[(state, nextState)] = self.alpha * difference + (1 - self.alpha) * self.getQValue(state, nextState)