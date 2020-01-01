def solve(board):
    """ Attempts to place candidates 1-9 in unprocessed squares by
    recursively backtracking to fill the board and returning True once there
    no more unprocessed squares hence the Sudoku has been solved.

    Args:
        board (list):

    Returns:
        bool: Returns true if every square in the board is processed
    """
    square = find_unprocessed_square(board)
    if not square:  # Terminates if there are no more unprocessed squares
        return True
    else:
        row, col = square
    for candidate in range(1, 10, 1):
        if should_prune(board, candidate, (row, col)) is False:
            board[row][col] = candidate
            if solve(board):
                return True
            board[row][col] = 0
    return False


def should_prune(board, candidate, pos):
    """ Takes a candidate and returns true if it can be determined that they
    cannot lead to a solution.

    Args:
        board (list):
        candidate (int):
        pos (tuple):

    Returns:
        bool: Returns
    """
    row, col = pos[0], pos[1]  # pos is the tuple from find_empty_square
    # Check row
    for i in range(9):
        if board[row][i] == candidate and col != i:
            return True
    # Check column
    for i in range(9):
        if board[i][col] == candidate and row != i:
            return True
    # Check box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == candidate and (i, j) != pos:
                return True
    return False


def find_unprocessed_square(board):
    """ Finds an unprocessed square on the board and returns the position as
    a tuple representing its row and column

    Args:
        board (list):

    Returns: object: Returns the position of an unprocessed square as a tuple if
        it can find one. Otherwise returns None
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # 0 is denoted for unprocessed squares
                return i, j
    return None


def print_board(board):
    """ Returns string representation of board.

    Args:
        board (list):

    Returns:
        object (str):
    """
    board_str = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if j == 3 or j == 6:
                board_str.append("| ")
            board_str.append(str(board[i][j]))
            board_str.append(" ")
        board_str.append("\n")
        if i == 2 or i == 5:
            board_str.append("- - - - - - - - - - -")
            board_str.append("\n")
    return "".join(board_str)


sudoku_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],

    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],

    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

# print("Initial board")
# print(print_board(sudoku_board))
# solve(sudoku_board)
# print("Solved board")
# print(print_board(sudoku_board))
