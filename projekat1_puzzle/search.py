from projekat1_puzzle.util import PriorityQueue

def aStarSearch(puzzle_problem):


        prQueue = PriorityQueue()
        root = puzzle_problem.getStartState()

        heuristic_cost = heuristicValue(root)
        root.total_cost= heuristic_cost
        root.heuristic = heuristic_cost

        prQueue.push(root, heuristic_cost)

        visited = set()

        result = None

        k = 0
        kat1 = False
        kat2 = False

        while not prQueue.isEmpty():
            k += 1
            parent = prQueue.pop()

            if puzzle_problem.isGoalState(parent):
                result = parent
                break
            if parent in visited:
                continue

            visited.add(parent)

            if k == 5000:
                kat1 = True
            if k == 10000:
                kat2 = True
            if kat2:
                path_cost = parent.total_cost - parent.heuristic + 0.4
            elif kat1:
                path_cost = parent.total_cost - parent.heuristic + 0.5
            else:
                path_cost = parent.total_cost - parent.heuristic + 1

            for child in puzzle_problem.getSuccessors(parent):
                heuristic_cost = heuristicValue(child)
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
        return path


def manhattanHeuristic(state):
    puzzle_size = int(len(state) ** 0.5)
    heuristic = 0
    row = 0
    column = -1

    for i in range(len(state)):
        column += 1
        if column > puzzle_size - 1:
            column -= puzzle_size
            row += 1

        if state[i] == 0:
            continue

        heuristic += abs(row - (state[i] - 1) / puzzle_size) + abs(column - (state[i] - 1) % puzzle_size)

    return heuristic


def linearConflict(lista):
    puzzle_size = int(len(lista) ** 0.5)
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

def heuristicValue(puzzle):
    heuristika1 = manhattanHeuristic(puzzle.content)
    heuristika2 = linearConflict(puzzle.content)
    return heuristika1 + heuristika2