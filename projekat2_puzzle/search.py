import time
from PySide2 import QtCore
from projekat2_puzzle.util import PriorityQueue


class AStarWorkThread(QtCore.QThread):
    signal = QtCore.Signal(list)

    def __init__(self, puzzle_problem, startState = None):
        QtCore.QThread.__init__(self)
        self.puzzle_problem = puzzle_problem
        self.startState = startState

    def run(self):
        self.aStarSearch()

    def aStarSearch(self):
        prQueue = PriorityQueue()

        root = self.puzzle_problem.getStartState() if not self.startState else self.startState
        heuristic_cost = self.aStartValue(root)
        root.total_cost= heuristic_cost    #necemo kada kreiramo Puzzle da prosledjujemo vrednost heurstike jer gubimo na vremenu =>
                                #moze se desiti da generisemo potomke koje necemo obici
                                #zato heuristiku i total_cost setujemo rucno, kada obilazimo potomka
        root.heuristic = heuristic_cost

        prQueue.push(root, heuristic_cost)

        visited = set() #da se vrsi pretraga po hashu, bice mnogoooo brze tako nego da koristimo listu

        result = None

        k = 0
        kat1 = False
        kat2 = False

        while not prQueue.isEmpty():
            k += 1
            parent = prQueue.pop()

            if self.puzzle_problem.isGoalState(parent):
                result = parent
                break
            if parent in visited:
                continue

            visited.add(parent)

            if k == 5000:   #za teske slagalice, posle ove dubine performanse jako opadaju, zato smanjujemo korak za pola
                kat1 = True
            if k == 10000:
                kat2 = True
            if kat2:
                path_cost = parent.total_cost - parent.heuristic + 0.4
            elif kat1:
                path_cost = parent.total_cost - parent.heuristic + 0.5 #ovo sam eksperimentalno utvrdila da SAMO ZA TESKE slagalice ce resenje
                                                                                #biti mnogo brze ak ose korak malo smanji
                                                                    #za lake i srednje slagalice ovo nije potrebno
            else:
                path_cost = parent.total_cost - parent.heuristic + 1

            for child in self.puzzle_problem.getSuccessors(parent):
                heuristic_cost = self.aStartValue(child)
                total_cost = path_cost + heuristic_cost

                if not child in visited :
                    child.total_cost = total_cost
                    child.heuristic = heuristic_cost
                    prQueue.push(child, child.total_cost)

        path = []

        while result != None:
            path.append(result)
            result = result.parent

        path.reverse()
        print ("Broj predjenih koraka je " + str(len(path)  - 1) + ".")     #ne koliko je koraka u pretrazi,
                                                                            #nego nase resenje koliko ima koraka
                                                                            #ovaj broj mi je poprilicno dobar, za teske slagalice ne prelazi 100
        for i in path:
            if path.index(i) == len(path) - 1:
                self.signal.emit({"RESENO!" : i.content})
            else:
                self.signal.emit({"RESAVA SE!" : i.content})
            time.sleep(0.3)
            #print (i)           #samo u konzoli da vidimo jel radi, kada dodamo gui prikazacemo svako stanje na svakuh sekund tako nesto

    def manhattanHeuristic(self, state):
        puzzle_size = int(len(state) ** 0.5)    #da li je 3x3 ili 4x4 slagalica
        heuristic = 0
        row = 0
        column = -1

        for i in range(len(state)):
            column += 1

            if column > puzzle_size - 1:
                column -= puzzle_size
                row += 1

            if state[i] == 0:
                continue    #smatracemo da ne gledamo da li je nula na svom mestu

            heuristic += abs(row - (state[i] - 1) / puzzle_size) + abs(column - (state[i] - 1) % puzzle_size)

        return heuristic

    def linearConflict(self, lista):  #ovo kad se doda na menheten, mnogo je bolja heuristika
        puzzle_size = int(len(lista) ** 0.5)    #da li je 3x3 ili 4x4 slagalica
        heuristic = 0
        column = -1
        row = 0
        max_row = [-1,-1,-1,-1]
        max_column = [-1,-1,-1,-1]

        for i in range(len(lista)):
            column += 1

            if column > puzzle_size - 1:
                row += 1
                column -= puzzle_size

            num = lista[i]
            koristan_broj = num - 1

            if num == 0:
                continue
            if koristan_broj / puzzle_size == row and koristan_broj % puzzle_size == column:
                continue
            if koristan_broj / puzzle_size == row:
                if koristan_broj > max_row[row]:
                    max_row[row] = koristan_broj
                else:
                    heuristic += 2
            if koristan_broj % puzzle_size == column:
                if koristan_broj > max_column[column]:
                    max_column[column] = koristan_broj
                else:
                    heuristic += 2

        return heuristic

    def aStartValue(self, puzzle):
        heuristika1 = self.manhattanHeuristic(puzzle.content)
        heuristika2 = self.linearConflict(puzzle.content)
        return heuristika1 + heuristika2


def manhattanHeuristic(state):
    puzzle_size = int(len(state) ** 0.5)    #da li je 3x3 ili 4x4 slagalica
    heuristic = 0
    row = 0
    column = -1

    for i in range(len(state)):
        column += 1
        if column > puzzle_size - 1:
            column -= puzzle_size
            row += 1

        if state[i] == 0:
            continue    #smatracemo da ne gledamo da li je nula na svom mestu

        heuristic += abs(row - (state[i] - 1) / puzzle_size) + abs(column - (state[i] - 1) % puzzle_size)

    return heuristic


def linearConflict(lista):  #ovo kad se doda na menheten, mnogo je bolja heuristika
    puzzle_size = int(len(lista) ** 0.5)    #da li je 3x3 ili 4x4 slagalica
    heuristic = 0
    column = -1
    row = 0
    max_row = [-1,-1,-1,-1]
    max_column = [-1,-1,-1,-1]

    for i in range(len(lista)):
        column += 1
        if column > puzzle_size - 1:
            row += 1
            column -= puzzle_size
        num = lista[i]
        koristan_broj = num - 1
        if num == 0:
            continue
        if koristan_broj / puzzle_size == row and koristan_broj % puzzle_size == column:
            continue
        if koristan_broj / puzzle_size == row:
            if koristan_broj > max_row[row]:
                max_row[row] = koristan_broj
            else:
                heuristic += 2
        if koristan_broj % puzzle_size == column:
            if koristan_broj > max_column[column]:
                max_column[column] = koristan_broj
            else:
                heuristic += 2

    return heuristic

def aStartValue(puzzle):
    heuristika1 = manhattanHeuristic(puzzle.content)
    heuristika2 = linearConflict(puzzle.content)
    return heuristika1 + heuristika2