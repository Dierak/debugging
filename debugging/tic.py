def print_board(board):
    """
    Function Description:
    Prints the current state of the tic-tac-toe board.

    Parameters:
    - board (list of lists): The tic-tac-toe board represented as a 2D list.

    Returns:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Function Description:
    Checks if a player has won the game.

    Parameters:
    - board (list of lists): The tic-tac-toe board represented as a 2D list.

    Returns:
    - bool: True if a player has won, False otherwise.
    """
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Function Description:
    Plays a game of tic-tac-toe.

    Parameters:
    None

    Returns:
    None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                raise ValueError("Row and column values must be 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for row and column.")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    print("Player " + player + " wins!")

tic_tac_toe()

