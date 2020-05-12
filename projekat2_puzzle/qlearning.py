#evo, i ovde se trudim da bude ko na vezbama, stvari koje sam radila drugacije
#cu komentaristati


#agent koji ce resiti slagalicu q-ucenjem
#prvo cemo da ga istreniramo (obucimo) => napunicemo tabelu koja cuva q vrednosti
#e kada ga obucimo, odnosno napunimo tu tabelu, onda cemo da je iskoritstimo
#i da vidimo kako ce agent resiti slagalicu kada je bude koristio

import random

class QLearningAgent:



    def __init__(self, puzzle_problem, alpha, discount):
        self.q_values = {}
        self.alpha = alpha
        self.discount = discount
        #discount cu staviti da je 0.8
        #alpha cu uzeti da je 0.2 za pocetak
        #velika nepomena: ucili smo da su q-vrednosti vrednosti za stanje-akcije
        #=> Q(S, A), e sad mogu i ja tako da radim, al msm da nije potrebno
        #za slagalicu to raditi, ja cu cuvati vrednosti za Q(S1, S2), gde je S1
        #prvo stanje, a S2 drugo stanje, jer svaka akcija je jednoznacna odnosno vodi
        #u jedno i samo jedno stanje
        #dakle, kljucevi recnika bice par (S1, S2), a vrednost ce biti q-vrednost
        #za prelazak iz stanja S1 u stanje S2
        self.puzzle_problem = puzzle_problem    #posto u klasi PuzzleProblem
        #vec imamo fine metode (tipa getSuccessors i sl) koristicemo ih ovde, da ne
        #pravim ponovo iste metode

    def getQValue(self, state1, state2):
        #ovo cu zvati iz fja, ne sama direktno
        if (state1, state2) not in self.q_values:
            self.q_values[(state1, state2)] = 0.0
        return self.q_values[(state1, state2)]
    #vracamo Q-vrednost za stanje1 i akciju koja ga vodi u stanje2

    def computeValueFromQValues(self, state):
        #ovo cu zvati iz fja, ne sama direktno
        q_values = [self.getQValue(state, successor) for successor in self.puzzle_problem.getSuccessors(state)]
        return max(q_values) if q_values else 0.0
    #ako je stanje terminalno (pobednicko), vracamo nulu
    #DODAJ DA SE NE PRAVE DECA OD POBEDNICKOG STANJA

    def computeStateFromQValue(self, state):
        #ako bih vracala akciju, vracala bih GORE, DOLE, LEVO, DESNO
        #al te akcije jednoznacno odredjuju sledece stanje, pa cu vracati
        #stanje koje te ackije prozivde

        successors = self.puzzle_problem.getSuccessors(state)
        successors = list(successors)
        if not successors:
            return None #dosli smo u pobednicko stanje!!

        q_values = [self.getQValue(state, successor) for successor in successors]
        results = []
        max_q = max(q_values)
        for i in range(len(q_values)):
            if q_values[i] == max_q:
                results.append(i)

        return successors[random.choice(results)]   #ako imamo npr dva stanja sa istom q-vrednoscu, radnom biramo od njih dva

    def getState(self, state):

        #dodaj greedy search ovde
        return self.computeStateFromQValue(state)


    def getPolicy(self, state):
        return self.computeStateFromQValue(state)   #ovo msm da necu nigde koristiti
                            #al neka ga ovde, mozda zatreba

    def getValue(self, state):
        return self.computeValueFromQValues(state)  #ovo msm da necu koristiti,
                    #al neka ga ovde, mozda zatreba


    def update(self, state, nextState, reward):
        difference = reward + self.discount * self.computeValueFromQValues(nextState)   #koliko smo osvojili ukupno
        self.q_values[(state, nextState)] = self.alpha * difference + (1 - self.alpha) * self.getQValue(state, nextState)






