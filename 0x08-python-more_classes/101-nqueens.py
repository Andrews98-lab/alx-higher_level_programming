#!/usr/bin/python3
"""
N Queens Puzzle
"""
import sys


def print_board(board):
    """Print the board"""
    result = []
    for i in range(len(board)):
        row = []
        for j in range(len(board)):
            if board[i] == j:
                row.append([i, j])
        result.append(row)
    print(result)


def is_safe(board, row, col):
    """Check if the cell is under attack"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve(board, row):
    """Solve N Queen problem"""
    if row == len(board):
        print_board(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1)


if __name__ == "__main__":
    # Validate the input
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0] * N
    solve(board, 0)

