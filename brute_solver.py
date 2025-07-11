def print_board(board):
    """Print the Sudoku board in a readable format."""
    for i in range(9):
        row = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += "| "
            row += str(board[i][j]) if board[i][j] != 0 else "."
            row += " "
        print(row)
        if (i + 1) % 3 == 0 and i != 8:
            print("-" * 21)

def find_empty_cell(board):
    """Find the first empty cell on the board. Return (row, col) or None if full."""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def is_valid(board, num, row, col):
    """Check if placing num at (row, col) is valid."""
    # Check row
    for j in range(9):
        if board[row][j] == num:
            return False
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    """Solve the Sudoku puzzle using backtracking."""
    empty = find_empty_cell(board)
    if not empty:
        return True  # Solved!
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0  # Backtrack
    return False

if __name__ == "__main__":
    # Example Sudoku puzzle (0 for empty)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original board:")
    print_board(board)

    if solve(board):
        print("\nSolved board:")
        print_board(board)
    else:
        print("No solution exists.")
