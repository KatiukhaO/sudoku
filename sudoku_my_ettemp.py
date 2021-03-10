from random import randint
import numpy as nm


def show_board(board):
    for row in board:
        print('   '.join(map(str, row)))

def create_rand_num_board(a=1, c=9):
    """Create board sudoku with random integer number in range from a to b """
    board = [[0]*9 for i in range(9)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            b = 0
            while b in board[i]:
                b = randint(a, c)
            board[i][j] = b
    return board

def find_0_change(board):
    board = nm.array(board)
    for i in range(9):
        column = board[:, i]
        for k, el in enumerate(column):
            s = column[k + 1:]
            if el in s:
                b = randint(1, 9)
                while b in column:
                    b = randint(1, 9)
                column[k] = b
    return board


show_board(find_0_change(create_rand_num_board()))

