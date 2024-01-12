import sys

def is_attacked(board, row, col):
    """Checks if a queen placed at (row, col) is attacked by any other queen."""
    for i in range(row):
        if board[i] == col or abs(row - i) == abs(col - board[i]):
            return True
    return False

def solve_n_queens(n, board, row):
    """Recursively solves the N queens problem for a given board state."""
    if row == n:
        print(" ".join(str(x) for x in board))  # Print the solution in required format
        return

    for col in range(n):
        if not is_attacked(board, row, col):
            board[row] = col
            solve_n_queens(n, board, row + 1)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    if n < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    board = [-1] * n
    solve_n_queens(n, board, 0)

if __name__ == "__main__":
    main()
