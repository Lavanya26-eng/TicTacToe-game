import random

# -------------------------------
# Display Board
# -------------------------------
def display_board(board):
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("---+---+---")
    print()


# -------------------------------
# Check Winner
# -------------------------------
def check_winner(board, player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pattern in wins:
        if all(board[i] == player for i in pattern):
            return True
    return False


# -------------------------------
# Draw
# -------------------------------
def is_draw(board):
    return " " not in board


# -------------------------------
# Available Moves
# -------------------------------
def available_moves(board):
    return [i for i in range(9) if board[i] == " "]


# -------------------------------
# AI Move
# -------------------------------
def ai_move(board):

    # Try to win
    for move in available_moves(board):
        temp = board[:]
        temp[move] = "O"
        if check_winner(temp, "O"):
            return move

    # Block player
    for move in available_moves(board):
        temp = board[:]
        temp[move] = "X"
        if check_winner(temp, "X"):
            return move

    # Take center
    if board[4] == " ":
        return 4

    # Take corners
    corners = [i for i in [0,2,6,8] if board[i] == " "]
    if corners:
        return random.choice(corners)

    # Random move
    return random.choice(available_moves(board))


# -------------------------------
# Player Move
# -------------------------------
def player_move(board):

    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move not in range(9):
                print("❌ Choose a number from 1-9.")
            elif board[move] != " ":
                print("❌ Position already occupied.")
            else:
                return move

        except ValueError:
            print("❌ Please enter a valid number.")


# -------------------------------
# Play Game
# -------------------------------
def play_game():

    board = [" "] * 9

    print("\nBoard Positions")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")

    while True:

        display_board(board)

        # Player
        move = player_move(board)
        board[move] = "X"

        if check_winner(board, "X"):
            display_board(board)
            print("🎉 Congratulations! You Win!")
            return "Player"

        if is_draw(board):
            display_board(board)
            print("🤝 Match Draw!")
            return "Draw"

        # AI
        ai = ai_move(board)
        board[ai] = "O"

        print(f"🤖 AI chose position {ai + 1}")

        if check_winner(board, "O"):
            display_board(board)
            print("🤖 AI Wins!")
            return "AI"

        if is_draw(board):
            display_board(board)
            print("🤝 Match Draw!")
            return "Draw"


# -------------------------------
# Main Program
# -------------------------------
player_score = 0
ai_score = 0
draw_score = 0

print("=" * 40)
print("      TIC-TAC-TOE WITH AI")
print("=" * 40)

while True:

    result = play_game()

    if result == "Player":
        player_score += 1
    elif result == "AI":
        ai_score += 1
    else:
        draw_score += 1

    print("\n📊 SCOREBOARD")
    print("-" * 25)
    print(f"😊 Player : {player_score}")
    print(f"🤖 AI     : {ai_score}")
    print(f"🤝 Draws  : {draw_score}")

    again = input("\nPlay Again? (y/n): ").lower()

    if again != "y":
        print("\n🎮 Thanks for Playing!")
        break
