#!/usr/bin/env python3
import sys

def is_safe(board, row, col, n):
    # Check if the same column has a queen
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper diagonal on right side
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def nqueens(board, row, n):
    # If all queens are placed, print the board
    if row == n:
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    print("[{}, {}]".format(i, j), end=" ")
        print()
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            nqueens(board, row+1, n)
            board[row][col] = 0

if __name__ == '__main__':
    # Check number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get value of N from command line argument
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [[0 for i in range(n)] for j in range(n)]

    # Call the nqueens function to solve the problem
    nqueens(board, 0, n)

