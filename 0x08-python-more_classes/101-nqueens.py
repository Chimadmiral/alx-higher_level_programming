#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def solve_n_queens(n):
    def can_place(row, col):
        # check if there is a queen placed in the same column
        for i in range(row):
            if board[i] == col:
                return False
        # check if there is a queen placed in the same diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i] == j:
                return False
        for i, j in zip(range(row, -1, -1), range(col, n, 1)):
            if board[i] == j:
                return False
        return True

    def place_queen(row, n):
        if row == n:
            # all queens are placed
            result.append(board.copy())
            return
        for col in range(n):
            if can_place(row, col):
                board[row] = col
                place_queen(row + 1, n)

    result = []
    board = [-1] * n
    place_queen(0, n)
    return result
