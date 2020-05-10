#e bas da vidim da li mi radi ovo :D

from projekat2_puzzle.searchMulti import ExpectimaxAgent, RandomAgent, MinimaxAgent
from projekat2_puzzle.puzzle import PuzzleProblem
from time import sleep
from projekat2_puzzle.search import aStartValue
from projekat2_puzzle.search import aStarSearch

def main():
    numAgents = 2  #na svaki peti potez nam protivnik pomeri prazno mesto
    depth = 7  #do koje dubine pretrazujemo minimax stablo
    myAgent = MinimaxAgent(depth, numAgents)
    myProtivnik = RandomAgent(myAgent)
    puzzleProblem = PuzzleProblem([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0])
    state = puzzleProblem.getStartState()

    agentIndex = 0

    iterNum = 20    #koliko iteracija dajemo da se borimo mi i protivnik
                    #onaj ko vise osvoji poena, taj pobeduje (mi smo pobedili ako smo se vise pomerili u odnosu na
                    #pocetno stanje, u suptrotnom je protivnik pobedio)
                    #ako smo mi pobedili, zovemo obicnu pretragu i slagalica se slozi
                    #ako smo mi izgubili onda kazemo da smo izgubili :D

    startValue = aStartValue(state)     #zapamptimo koliko smo na pocetku bili daleko od resenja, pa uporedimo sa kranjim resenjem


    for i in range(iterNum):
        print ("IGRA AGENT: {}".format(agentIndex))
        if agentIndex < numAgents - 1:

            temp = myAgent.getAction(puzzleProblem, state)
        else:
            temp = myProtivnik.getAction(puzzleProblem, state)

        if not temp:
            print("NE MOZE DA ODIGRA  AGENT :( {}".format(agentIndex))
        else:
            state = temp


        agentIndex = (agentIndex + 1) % numAgents


        if puzzleProblem.isGoalState(state):
            print ("RESILI")
            break



    if aStartValue(state) <= startValue:
        print ("POBEDILI")
        aStarSearch(puzzleProblem, state)
    else:
        print ("IZGUBILI")

if __name__ == '__main__':

    main()