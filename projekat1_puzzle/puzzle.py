
class PuzzleState:

    def __init__(self, content, parent=None):
        self.content = content[:]
        self.parent = parent
        self.heuristic = 0
        self.total_cost = 0
        self.hash = None

    def __eq__(self, other):
        if other == None:
            return False
        return self.content == other.content

    def __hash__(self):
        if self.hash == None:
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

    def __init__(self, start, goal):
        self.start = PuzzleState(start)
        self.goal = goal

    def getStartState(self):
        return self.start

    def isGoalState(self, state):
        return state.content == self.goal

    def getSuccessors(self, parent):
        successors = set()
        state = parent.content
        puzzle_size = int(len(state) ** 0.5)
        empty_space = state.index(0)

        if empty_space - puzzle_size >= 0:
            successor = state[:]
            successor[empty_space], successor[empty_space - puzzle_size] = successor[empty_space - puzzle_size], successor[empty_space]
            successors.add((PuzzleState(successor, parent)))
        if empty_space + puzzle_size < len(state):
            successor = state[:]
            successor[empty_space], successor[empty_space + puzzle_size] = successor[empty_space + puzzle_size], successor[empty_space]
            successors.add((PuzzleState(successor, parent)))
        if empty_space % puzzle_size > 0:
            successor = state[:]
            successor[empty_space], successor[empty_space - 1] = successor[empty_space - 1], successor[empty_space]
            successors.add((PuzzleState(successor, parent)))
        if empty_space % puzzle_size < puzzle_size - 1:
            successor = state[:]
            successor[empty_space], successor[empty_space + 1] = successor[empty_space + 1], successor[empty_space]
            successors.add((PuzzleState(successor, parent)))

        return successors