import random

# Display the board
def display_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")
    print("\n")

# Check winner
def check_winner(board, player):
    win_patterns = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]

    for pattern in win_patterns:
        if all(board[pos] == player for pos in pattern):
            return True
    return False

# Check draw
def is_draw(board):
    return " " not in board

# AI move
def ai_move(board):
    available = [i for i in range(9) if board[i] == " "]
    return random.choice(available)

# Main game
board = [" "] * 9

print("=== Tic-Tac-Toe with AI ===")
print("Positions:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

while True:
    display_board(board)

    # Player move
    try:
        move = int(input("Enter your move (1-9): ")) - 1

        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move! Try again.")
            continue

        board[move] = "X"

        if check_winner(board, "X"):
            display_board(board)
            print("🎉 Congratulations! You win!")
            break

        if is_draw(board):
            display_board(board)
            print("Game Draw!")
            break

        # AI move
        ai = ai_move(board)
        board[ai] = "O"
        print(f"AI chose position {ai + 1}")

        if check_winner(board, "O"):
            display_board(board)
            print("🤖 AI Wins!")
            break

        if is_draw(board):
            display_board(board)
            print("Game Draw!")
            break

    except ValueError:
        print("Please enter a number between 1 and 9.")