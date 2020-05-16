from projekat1_puzzle.search import heuristicValue
from random import choice


class RandomAgent:

    def __init__(self, protivnik):
        self.protivnik = protivnik


    def getAction(self, problem, state):

        while True:
            temp = choice(list(problem.getSuccessors(state)))

            if temp != self.protivnik.lastState:
                return temp



class MultiAgent:

    def __init__(self, depth, agentsNum, evalutionFunction=heuristicValue):
        self.depth = depth
        self.evalutionFunction = evalutionFunction
        self.agentsNum = agentsNum
        self.lastState = None



class ExpectimaxAgent(MultiAgent):

    def __init__(self, depth, agentsNum, evalutionFunction=heuristicValue):
        super().__init__(depth, agentsNum, evalutionFunction)



    def getAction(self, problem, state):

        def expmaxSearch(problem, state, index, depth, root = False):

            if depth == self.depth or problem.isGoalState(state):
                return self.evalutionFunction(state)

            next_index = index + 1
            if next_index == self.agentsNum:
                next_index = 0
                depth += 1


            best_value = float('inf')

            best_action = None

            suma = 0.0
            counter = 0.0

            for successor in problem.getSuccessors(state):

                value = expmaxSearch(problem, state, next_index, depth)
                if index < self.agentsNum - 1:
                    if value < best_value:
                        best_action = successor
                        best_value = value


                else:
                    suma += value
                    counter += 1
                    best_value = suma / counter



            return best_value if not root else best_action

        temp = expmaxSearch(problem, state, 0, 0, True)
        self.lastState = temp
        return temp

class MinimaxAgent(MultiAgent):

    def __init__(self, depth, agentsNum, evalutionFunction=heuristicValue):
        super().__init__(depth, agentsNum, evalutionFunction)

    def getAction(self, problem, state):

        def minimaxSearch(problem, state, index, depth, alfa, beta, root = False):

            if depth == self.depth or problem.isGoalState(state):
                return self.evalutionFunction(state)

            next_index = index + 1
            if next_index == self.agentsNum:
                next_index = 0
                depth += 1




            best_action = None

            for successor in problem.getSuccessors(state):

                value = minimaxSearch(problem, state, next_index, depth, alfa, beta)
                if index < self.agentsNum - 1:

                    if value <= beta:

                        return value if not  root else best_action

                    if value < alfa:
                        best_action = successor
                        alfa = value

                else:

                    if value >= alfa:
                        return value if not root else best_action

                    if value > beta:
                        beta = value
                        best_action = successor


            return best_action if root else alfa if index < self.agentsNum - 1 else beta

        temp = minimaxSearch(problem, state, 0, 0, float('inf'), float('-inf'), True)
        self.lastState = temp
        return temp