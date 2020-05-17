from projekat1_puzzle.util import PriorityQueue

def a_star_search(puzzle_problem):

        pr_queue = PriorityQueue()
        root = puzzle_problem.getStartState()
        heuristic_cost = heuristic_value(root)
        root.heuristic = heuristic_cost
        root.total_cost= heuristic_cost
        pr_queue.push(root, heuristic_cost)

        visited = set()
        k = 0
        kat1 = False
        kat2 = False

        while not pr_queue.isEmpty():

            k += 1
            parent = pr_queue.pop()

            if puzzle_problem.isGoalState(parent):

                path = []
                while parent != None:
                    path.append(parent)
                    parent = parent.parent
                path.reverse()
                return path

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
                heuristic_cost = heuristic_value(child)
                total_cost = path_cost + heuristic_cost
                if not child in visited :
                    child.total_cost = total_cost
                    child.heuristic = heuristic_cost
                    pr_queue.push(child, child.total_cost)

def manhattan_heuristic(content):

    puzzle_size = int(len(content) ** 0.5)
    heuristic = 0
    row = 0
    column = -1

    for i in range(len(content)):

        column += 1
        if column > puzzle_size - 1:
            column -= puzzle_size
            row += 1

        if content[i] == 0:
            continue

        heuristic += abs(row - (content[i] - 1) / puzzle_size) + abs(column - (content[i] - 1) % puzzle_size)

    return heuristic


def linear_conflict(content):

    puzzle_size = int(len(content) ** 0.5)
    heuristic = 0
    column = -1
    row = 0
    max_row = [-1,-1,-1,-1]
    max_column = [-1,-1,-1,-1]

    for i in range(len(content)):
        column += 1
        if column > puzzle_size - 1:
            row += 1
            column -= puzzle_size
        num = content[i]
        usefull_num = num - 1
        if num == 0:
            continue
        if usefull_num / puzzle_size == row and usefull_num % puzzle_size == column:
            continue
        if usefull_num / puzzle_size == row:
            if usefull_num > max_row[row]:
                max_row[row] = usefull_num
            else:
                heuristic += 2
        if usefull_num % puzzle_size == column:
            if usefull_num > max_column[column]:
                max_column[column] = usefull_num
            else:
                heuristic += 2

    return heuristic

def heuristic_value(puzzle):
    return manhattan_heuristic(puzzle.content) + linear_conflict(puzzle.content)