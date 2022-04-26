
import pprint

# solver.py
def solve(to):
    # solves a sudoku board using backtracking
    find = find_empty(to)
    if find:
        row, col = find
    else:
        return True

    for i in range(1, 10):
        if valid(to, (row, col), i):
            to[row][col] = i

            if solve(to):
                return True

            to[row][col] = 0

        return False

def valid(to, pos, num):
    # returns if the attempted move is valid

    # check now
    for i in range(0, len(to)):
        if to[pos[0]][i] == num and pos[1] != i:
            return False

        # Check col
    for i in range(0, len(to)):
        if to[i][pos[1]] == num and pos[1] != i:
            return False

    # check box
    box_x = pos[1]//3
    box_y = pos[0]//3


    for i in range(box_y * 3, box_x * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if to[i][j] == num and (i,j) != pos:
                return False

        return True


def find_empty(to):


    for i in range(len(to)):
        for j in range(len(to[0])):
            if to[i][j] == 0:
                return (i, j)


def print_board(to):



    for i in range(len(to)):
        if 1 % 3 ==  0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(to[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(to[i][j], end="\n")
            else:
                print(str(to[1][j]) + " ", end="")


board = [
        [7, 8, 0, 4, 0, 0, 1, 3, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

pp = pprint.PrettyPrinter(width=41, compact=True)
solve(board)
pp.pprint(board)

