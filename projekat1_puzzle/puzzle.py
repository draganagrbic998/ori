class Puzzle:

    def __init__(self, content, parent = None):
        self.content = content[:]
        self.parent = parent
        self.heuristic_cost = 0.0
        self.total_cost = 0.0
        self.hash = None

    def __eq__(self, other):
        if other == None:
            return False
        return self.content == other.content

    def __hash__(self):
        if self.hash == None:
            self.hash = hash(tuple(self.content))
        return self.hash

class PuzzleProblem:

    def __init__(self, start, goal):
        self.start = Puzzle(start)
        self.goal = Puzzle(goal)

    def get_start_state(self):
        return self.start

    def is_goal_state(self, state):
        return state == self.goal

    def get_successors(self, parent):

        if self.is_goal_state(parent):
            return set()

        state = parent.content
        successors = set()
        puzzle_size = int(len(state) ** 0.5)
        empty_space = state.index(0)

        if empty_space - puzzle_size >= 0:
            successor = state[:]
            successor[empty_space], successor[empty_space - puzzle_size] = successor[empty_space - puzzle_size], successor[empty_space]
            successors.add((Puzzle(successor, parent)))

        if empty_space + puzzle_size < len(state):
            successor = state[:]
            successor[empty_space], successor[empty_space + puzzle_size] = successor[empty_space + puzzle_size], successor[empty_space]
            successors.add((Puzzle(successor, parent)))

        if empty_space % puzzle_size > 0:
            successor = state[:]
            successor[empty_space], successor[empty_space - 1] = successor[empty_space - 1], successor[empty_space]
            successors.add((Puzzle(successor, parent)))

        if empty_space % puzzle_size < puzzle_size - 1:
            successor = state[:]
            successor[empty_space], successor[empty_space + 1] = successor[empty_space + 1], successor[empty_space]
            successors.add((Puzzle(successor, parent)))

        return successors