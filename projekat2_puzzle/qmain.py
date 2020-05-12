from projekat2_puzzle.puzzle import PuzzleProblem
from projekat2_puzzle.search import aStarSearch
from projekat2_puzzle.qlearning import QLearningAgent

def reward(problem, state):
    if problem.isGoalState(state):
        return 500.0  #ako smo pobedili, nagradimo agenta
    return 0.0

def main():
    #samo da obicno resim 3x3 slagalicu
    problem = PuzzleProblem([1, 0, 4, 2, 5, 3, 8, 7, 6], [1, 2, 3, 4, 5, 6, 7, 8, 0])
    aStarSearch(problem)

def obucavanje(iter_num):
    #iter_num => koliko iteracija obucavamo agenta
    problem = PuzzleProblem([1, 0, 4, 2, 5, 3, 8, 7, 6], [1, 2, 3, 4, 5, 6, 7, 8, 0])
    agent = QLearningAgent(problem, 0.2, 0.8)
    state = problem.getStartState()
    for i in range(iter_num):
        nextState = agent.computeStateFromQValue(state)
        agent.update(state, nextState, reward(problem, nextState))
        state= nextState
    return agent


if __name__ == '__main__':
    agent = obucavanje(100000)
    print ("ZAVRSENO OBUCAVANJE")
    problem = PuzzleProblem([1, 0, 4, 2, 5, 3, 8, 7, 6], [1, 2, 3, 4, 5, 6, 7, 8, 0])
    state= problem.getStartState()
    path = []
    while not problem.isGoalState(state):
        state = agent.getState(state)
        path.append(state)
    print ("RESILA!")   #za sada sam testirala na slagalici na kojoj sam obucavala agenta, nju resi poprilicno brzo, kasnije cu
                        #videti kako radi za slagalice koje nisu iz obucavajuceg skupa, sad mi se sklapaju oci :D
    for i in path:
        print (i)