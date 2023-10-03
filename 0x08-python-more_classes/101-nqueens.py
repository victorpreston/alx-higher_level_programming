#!/usr/bin/python3
"""Solving the nqueen puzzle"""
import sys


def init_board(n):
    """Initializing `n`x`n` size chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """chessboard deepcopy"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """List represenation of solved chessboard"""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """spots on chessboard
    Args:
        board (list): Working chessboard.
        row (int): Last queen played row.
        col (int): Last queen played column.
    """
    # forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # down and right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # all spots
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # Right diagonal
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # left diagonal
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Solving nquuen puzzle recursively.

    Args:
        board (list): Working chessboard.
        row (int): Working row.
        queens (int): Number of currently placed queens.
        solutions (list): Lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
