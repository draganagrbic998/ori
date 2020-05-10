#i ovde cu se voditi da radim slicno ko na vezbama, koliko budem mogla
#e stvari sa kojima cemo se igrati (parametre koje cemo cackati:)

#1. DUBINA (dokle se spustamo u stblu sa protivnicima)
#2. POSLE KOLIKO KORAKA PROTIVNIK NAM POMERI MESTO (tj. da li na svaki
#drugi, treci, cetvrti... korak nam protivnik random pomeri prazno mesto
#3. sto se tice evalucione fje, pitacu asistenta da li moze heustika da se koristi
#(jer je meni logicno da moze, stavicu za sad heurstiku pa cemo se cuti sa njim jos)

#e za ovaj nas problem je ispravno koristiti Expectimax, ali uradicu i minimax cisto da mozemo da uporedimo

from projekat2_puzzle.search import aStartValue
from random import choice


class RandomAgent:

    def __init__(self, protivnik):
        self.protivnik = protivnik


    def getAction(self, problem, state):

        return choice(list(problem.getSuccessors(state)))



class MultiAgent:

    def __init__(self, depth, agentsNum, evalutionFunction=aStartValue):    #za sada neka evaluciona fja bude heuristika
        self.depth = depth  #sa ovim cemo se igrati i zato je u kontruktoru
        self.evalutionFunction = evalutionFunction
        self.agentsNum = agentsNum  #e ovo oznacava na koji korak ce da nam protivnik
                            #random pomeri mesto
                    #npr ako je agentsNum=5, onda ce na svaki peti korak da to uradi (zato sto
            #imamo samo dva igraca - nas agent i taj random protivnik, a nas agent ce igrati prva cetiri puta
        #, a protivnik samo peti put)
        #ja msm da evaluciona fja moze biti heuristika
        #pitacemo jos asistenta

        #sa agentsNum cemo se igrati i zato stoji u konsturktoru

class ExpectimaxAgent(MultiAgent):

    def __init__(self, depth, agentsNum, evalutionFunction=aStartValue):
        super().__init__(depth, agentsNum, evalutionFunction)



    def getAction(self, problem, state):

        def expmaxSearch(problem, state, index, depth, root = False):

            #root => prvi put kad pozove fju, vracamo akciju (GORE, DOLE, LEVO, DESNO)
            #u ostlaim slucajevima vracamo vrednost stanja

            if depth == self.depth or problem.isGoalState(state):    #ne moze da bude izgubljeno :)
                return self.evalutionFunction(state)

            next_index = index + 1
            if next_index == self.agentsNum:    #kod nas nema umiranja igraca, pa ce broj igraca uvek ostati konstantan
                next_index = 0                                 #zato ovde cuvamo agentsNum
                depth += 1

            #nas agent ima indekse 0, 1, ..., self.agentsNum - 2
            #a protivnik ima indeks self.agentsNum-1

            best_value = float('inf') #if index < self.agentsNum - 1 else float('inf')
            #ako je indeks agenta manji od poslednjeg indeksa, onda su to potezi koje nas igrac ima
            #i on radi maksimizaciju
            #a ako je indeks poslednji (self.agentsNum-1) onda je to potez naseg protivnika i on radi minimizaciju

            best_action = None  #ako smo prvi put pozvali ovu fju, onda vracamo akciju, a ne vrednost

            suma = 0.0
            counter = 0.0

            for successor in problem.getSuccessors(state):

                value = expmaxSearch(problem, state, next_index, depth)
                if index < self.agentsNum - 1:  #ovo je potez naseg igraca
                    if value < best_value:    #max je za nas ovde min jer heuristika je bolja sto je manja
                        best_action = successor
                        best_value = value


                else:   #ovo je potez naseg protivnika

                    suma += value
                    counter += 1
                    best_value = suma / counter
                    best_action = best_action



            return best_value if not root else best_action  #ako smo prvi put pozvali, ocemo akciju

        return expmaxSearch(problem, state, 0, 0, True)    #necu da pamptim indeks u klasi jer je uvek nula na pocetku


class MinimaxAgent(MultiAgent):

    def __init__(self, depth, agentsNum, evalutionFunction=aStartValue):
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

                    if value <= beta:    #ne secam se dal na predavanjima ovde bilo jednako

                        return value if not  root else best_action

                    if value < alfa:
                        best_action = successor
                        alfa = value

                else:

                    if value >= alfa:    #ne secam se dal na predavanjima ovde bilo jednako
                        return value if not root else best_action

                    if value > beta:
                        beta = value
                        best_action = successor



            return best_action if root else alfa if index < self.agentsNum - 1 else beta

        return minimaxSearch(problem, state, 0, 0, float('inf'), float('-inf'), True)
