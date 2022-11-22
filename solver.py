# code from https://stackoverflow.com/questions/70789686/python-sudoku-solver-with-multiple-solutions,
# which was taken from Tech with Tim: https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/


# example input:
# [
# [7, 5, 4, 8, 3, 9, 1, 6, 2],
# [6, 9, 1, 5, 2, 4, 8, 3, 7],
# [3, 2, 8, 6, 7, 1, 4, 5, 9],
# [4, 1, 9, 2, 6, 3, 5, 7, 8],
# [8, 3, 6, 7, 9, 5, 2, 1, 4],
# [5, 7, 2, 1, 4, 8, 6, 9, 3],
# [1, 6, 3, 4, 8, 7, 9, 2, 5],
# [2, 8, 7, 9, 5, 6, 3, 4, 1],
# [9, 4, 5, 3, 1, 2, 7, 8, 6]
# ]


board = [
    [0, 8, 4, 9, 0, 5, 7, 0, 0],
    [0, 0, 7, 8, 3, 4, 9, 5, 2],
    [0, 9, 0, 2, 0, 7, 0, 0, 8],
    [0, 7, 9, 5, 2, 3, 4, 0, 6],
    [3, 0, 5, 4, 8, 9, 2, 7, 0],
    [4, 0, 8, 0, 7, 0, 0, 9, 0],
    [7, 0, 0, 3, 5, 2, 8, 0, 9],
    [8, 3, 0, 7, 9, 0, 5, 2, 4],
    [0, 0, 2, 0, 4, 8, 0, 3, 0],
]


def check(puzzle, i, row, col):
    rows = puzzle[int(row)]
    column = [puzzle[r][col] for r in range(9)]
    if i in rows:
        return False
    if i in column:
        return False
    SquareRow = (row // 3) * 3
    squareColumn = (col // 3) * 3
    Square = [puzzle[y][z] for y in range(
        SquareRow, SquareRow + 3) for z in range(squareColumn, squareColumn + 3)]
    if i in Square:
        return False
    return True


def find(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return None


def solve(board):
    finds = find(board)
    if not finds:
        return True
    else:
        row, col = finds

    for i in range(1, 10):
        if check(board, i, row, col):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


print(solve(board))
print(board)
