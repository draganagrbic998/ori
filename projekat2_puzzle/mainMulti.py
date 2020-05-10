#e bas da vidim da li mi radi ovo :D

from projekat2_puzzle.searchMulti import ExpectimaxAgent, RandomAgent
from projekat2_puzzle.puzzle import PuzzleProblem
from time import sleep

def main():
    numAgents = 2   #na svaki peti potez nam protivnik pomeri prazno mesto
    depth = 5   #do koje dubine pretrazujemo minimax stablo
    myAgent = ExpectimaxAgent(depth, numAgents)
    myProtivnik = RandomAgent(myAgent)
    puzzleProblem = PuzzleProblem([1, 2, 3, 4, 5, 6, 7, 8, 0])
    state = puzzleProblem.getStartState()

    agentIndex = 0


    while True:
        print ("IGRA AGENT: {}".format(agentIndex))
        if agentIndex < numAgents - 1:

            temp = myAgent.getAction(puzzleProblem, state)
        else:
            temp = myProtivnik.getAction(puzzleProblem, state)

        if not temp:
            print("NE MOZE DA ODIGRA  AGENT :( {}".format(agentIndex))
        else:
            state = temp

        print (state)
        agentIndex = (agentIndex + 1) % numAgents
        if puzzleProblem.isGoalState(state):
            print ("RESILI")
            break

        if myAgent.blocked or myProtivnik.blocked:
            print ("NEMA DALJE")
            #dodam da se ovde restartuje il nesto slicno
            break


if __name__ == '__main__':

    main()