from enum import Enum


class Action(Enum):  #ovo necu koristiti kod obicne pretrage, samo cemo usporiti proces ako budemo vraacali akcije a ne stanja
                    #(jer cmeo vrv na guiju samo da stanja prikazujemo jedno po jedno kad nadjemo resenje)
                    #vrv cu koristit kod pretrage sa protivnicima

    LEFT = 1
    UP = 2
    RIGHT = 2
    DOWN = 3  # gde mozemo da pomerimo prazno mesto
    STOP = 4  # ne pomeramo se


class Puzzle:

    def __init__(self, content, parent=None, action = Action.STOP):
        self.content = content[:]
        self.parent = parent
        self.heuristic = 0
        self.total_cost = 0
        self.hash = None
        self.action=action

    def __eq__(self, other):
        if other == None:
            return False
        return self.content == other.content

    def __hash__(self):
        if self.hash == None:   #ovo je bitno, pomocu hasha mnogooo brze pretrazujemo visited
            self.hash = hash(tuple(self.content))
        return self.hash

    def __str__(self):
        puzzle_size = int(len(self.content) ** 0.5)
        indeks = 0
        suma = ""
        for i in range(puzzle_size):
            for j in range(puzzle_size):
                suma += str(self.content[indeks]).ljust(5)
                indeks += 1
            suma += "\n"
        return suma


class PuzzleProblem:

    def __init__(self, goal):
        self.goal = goal    #ovo je lista koja treb da se dobije ([1, 2, 3, ...., 15, 0])

    def getStartState(self):
        return Puzzle([0,12,9,13,15,11,10,14,8,3,6,2,4,7,5,1])
        #za pocetak nek vraca ovu slagalicu, kasnije dodamo
        #da vraca radnom slagalicu iz nekog skupa ili slicno
        #samo da znas, ovo je TESKA SLAGALICA, i resi mi je za 96 koraka i pola sekunde (PONOSNA SAM :D)

    def isGoalState(self, state):
        return state.content == self.goal

    def getSuccessors(self, parent):

        successors = set()
        state = parent.content
        puzzle_size = int(len(state) ** 0.5)    #da li je slagalica 3x3 ili 4x4
        empty_space = state.index(0)        #trazimo prazno mesto koje cemo pomerati

        if empty_space - puzzle_size >= 0:  #mozemo gore da pomerimo
            successor = state[:]
            successor[empty_space], successor[empty_space - puzzle_size] = successor[empty_space - puzzle_size], successor[empty_space]
            successors.add((Puzzle(successor, parent, Action.UP)))  #stavljala sam da se cuvaju akcije, mada ih ne koristim, al neka ih ovde
                                                                    #mozda budu zatrebale
        if empty_space + puzzle_size < len(state):  #mozemo da pomerimo dole
            successor = state[:]
            successor[empty_space], successor[empty_space + puzzle_size] = successor[empty_space + puzzle_size], successor[empty_space]
            successors.add((Puzzle(successor, parent, Action.DOWN)))
        if empty_space % puzzle_size > 0:   #mozemo da pomerimo levo
            successor = state[:]
            successor[empty_space], successor[empty_space - 1] = successor[empty_space - 1], successor[empty_space]
            successors.add((Puzzle(successor, parent, Action.LEFT)))
        if empty_space % puzzle_size < puzzle_size - 1:  #mozemo da pomerimo desno
            successor = state[:]
            successor[empty_space], successor[empty_space + 1] = successor[empty_space + 1], successor[empty_space]
            successors.add((Puzzle(successor, parent, Action.RIGHT)))

        return successors