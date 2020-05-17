from abc import ABC, abstractmethod
from random import choice
from projekat1_puzzle.search import heuristic_value

class MultiAgent(ABC):

    @abstractmethod
    def get_action(self, problem, state):
        pass

class RandomAgent(MultiAgent):

    def get_action(self, problem, state):
        return choice(list(problem.get_successors(state)))

class MyAgent(MultiAgent):

    def __init__(self, depth, evalution_function = heuristic_value):
        self.depth = depth
        self.evalution_function = evalution_function

class MinimaxAgent(MyAgent):

    def get_action(self, problem, state):

        def minimax_search(problem, state, index, depth, alfa, beta, root = False):

            if depth == self.depth or problem.is_goal_state(state):
                return self.evalution_function(state)

            next_index = index + 1
            if next_index == 2:
                next_index = 0
                depth += 1

            best_state = None

            for successor in problem.get_successors(state):

                value = minimax_search(problem, successor, next_index, depth, alfa, beta)

                if not index:

                    if value <= beta:
                        return value if not root else best_state

                    if value < alfa:
                        alfa = value
                        best_state = successor

                else:

                    if value >= alfa:
                        return value if not root else best_state

                    if value > beta:
                        beta = value
                        best_state = successor

            return best_state if root else alfa if not index else beta

        return minimax_search(problem, state, 0, 0, float('inf'), float('-inf'), True)

class ExpectimaxAgent(MyAgent):


    def get_action(self, problem, state):

        def expmax_search(problem, state, index, depth, root = False):

            if depth == self.depth or problem.is_goal_state(state):
                return self.evalution_function(state)

            next_index = index + 1
            if next_index == 2:
                next_index = 0
                depth += 1

            best_value = float('inf')
            best_state = None
            suma = 0.0
            counter = 0.0

            for successor in problem.get_successors(state):

                value = expmax_search(problem, successor, next_index, depth)

                if not index:
                    if value < best_value:
                        best_value = value
                        best_state = successor

                else:
                    suma += value
                    counter += 1
                    best_value = suma / counter

            return best_state if root else best_value

        return expmax_search(problem, state, 0, 0, True)
