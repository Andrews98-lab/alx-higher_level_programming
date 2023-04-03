#!/usr/bin/python3
"""
N Queens problem solver
"""

import sys


def is_valid(board, row, col):
    """
    Check if it's valid to place a queen at board[row][col]
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve(board, col, solutions):
    """
    Recursive function to solve the problem
    """
    if col >= N:
        # Found a solution
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for row in range(N):
        if is_valid(board, row, col):
            board[row][col] = 1
            solve(board, col + 1, solutions)
            board[row][col] = 0


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
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

    # Initialize the board
    board = [[0] * N for _ in range(N)]

    # Solve the problem
    solutions = []
    solve(board, 0, solutions)

    # Print solutions
    for solution in solutions:
        print(solution)

