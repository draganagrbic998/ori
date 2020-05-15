#e bas da vidim da li mi radi ovo :D

from projekat2_puzzle.searchMulti import ExpectimaxAgent, RandomAgent, MinimaxAgent
from time import sleep
from projekat2_puzzle.search import aStartValue
from PySide2 import QtCore


class ProtivnikWorkThread(QtCore.QThread):
    signal = QtCore.Signal(dict)

    def __init__(self, puzzle_problem, startState = None, numAgents = 2, depth = 7, iterNum = 20, agent = "Minimax"):
        QtCore.QThread.__init__(self)
        self.puzzle_problem = puzzle_problem
        self.startState = startState
        self.numAgents = numAgents
        self.depth = depth
        self.iterNum = iterNum
        self.agent = agent

    def run(self):
        self.protivnikSearch()

    def protivnikSearch(self):
        #numAgents = 2  #na svaki peti potez nam protivnik pomeri prazno mesto
        #depth = 7  #do koje dubine pretrazujemo minimax stablo
        myAgent = MinimaxAgent(self.depth, self.numAgents)

        if self.agent == "Expectimax":
            myAgent = ExpectimaxAgent(self.depth, self.numAgents)

        myProtivnik = RandomAgent(myAgent)
        state = self.puzzle_problem.getStartState()

        agentIndex = 0

        #iterNum = 20    #koliko iteracija dajemo da se borimo mi i protivnik
                        #onaj ko vise osvoji poena, taj pobeduje (mi smo pobedili ako smo se vise pomerili u odnosu na
                        #pocetno stanje, u suptrotnom je protivnik pobedio)
                        #ako smo mi pobedili, zovemo obicnu pretragu i slagalica se slozi
                        #ako smo mi izgubili onda kazemo da smo izgubili :D

        startValue = aStartValue(state)     #zapamptimo koliko smo na pocetku bili daleko od resenja, pa uporedimo sa kranjim resenjem

        emitVal = {"me": [state.content, startValue]}
        self.signal.emit(emitVal)
        sleep(1)

        for i in range(self.iterNum):
            print ("IGRA AGENT: {}".format(agentIndex))

            if agentIndex < self.numAgents - 1:

                temp = myAgent.getAction(self.puzzle_problem, state)
            else:
                temp = myProtivnik.getAction(self.puzzle_problem, state)

            if not temp:
                print("NE MOZE DA ODIGRA  AGENT :( {}".format(agentIndex))
            else:
                if agentIndex < self.numAgents - 1:
                    emitVal = {"me": [temp.content, aStartValue(temp)]}
                else:
                    emitVal = {"enemy": [temp.content, aStartValue(temp)]}

                state = temp
                self.signal.emit(emitVal)
                sleep(0.3)

            agentIndex = (agentIndex + 1) % self.numAgents

            if self.puzzle_problem.isGoalState(state):
                print ("RESILI")
                break

        if aStartValue(state) <= startValue:
            print ("POBEDILI")
            emitVal = {"pobedili": [state.content, aStartValue(state)]}
            self.signal.emit(emitVal)
            #aStarSearch(self.puzzle_roblem, state)
        else:
            emitVal = {"izgubili": [state.content, aStartValue(state)]}
            self.signal.emit(emitVal)
            print ("IZGUBILI")

