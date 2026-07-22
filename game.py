import random
import time

# ==========================
# Colors
# ==========================
RESET = "\033[0m"
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"

# ==========================
# Display Board
# ==========================
def display_board(board):

    print(f"{CYAN}\nCurrent Board\t\tBoard Positions{RESET}")

    for i in range(3):
        left = f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]}"
        right = f" {i*3+1} | {i*3+2} | {i*3+3}"
        print(left + "\t\t" + right)

        if i != 2:
            print("---+---+---\t\t---+---+---")

    print()


# ==========================
# Winner Check
# ==========================
def check_winner(board, player):

    wins = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    return any(all(board[i] == player for i in win) for win in wins)


# ==========================
# Draw Check
# ==========================
def is_draw(board):
    return " " not in board


# ==========================
# Available Moves
# ==========================
def available_moves(board):
    return [i for i in range(9) if board[i] == " "]


# ==========================
# Smart AI
# ==========================
def ai_move(board):

    # 1. Win
    for move in available_moves(board):
        temp = board[:]
        temp[move] = "O"
        if check_winner(temp, "O"):
            return move

    # 2. Block
    for move in available_moves(board):
        temp = board[:]
        temp[move] = "X"
        if check_winner(temp, "X"):
            return move

    # 3. Center
    if board[4] == " ":
        return 4

    # 4. Opposite Corner
    opposite = {
        0:8,
        8:0,
        2:6,
        6:2
    }

    for corner in opposite:
        if board[corner] == "X" and board[opposite[corner]] == " ":
            return opposite[corner]

    # 5. Empty Corner
    corners = [0,2,6,8]
    empty = [c for c in corners if board[c] == " "]
    if empty:
        return random.choice(empty)

    # 6. Empty Side
    sides = [1,3,5,7]
    empty = [s for s in sides if board[s] == " "]
    if empty:
        return random.choice(empty)

    return random.choice(available_moves(board))


# ==========================
# Player Move
# ==========================
def player_move(board):

    while True:

        try:

            move = int(input(f"{GREEN}Enter your move (1-9): {RESET}")) - 1

            if move not in range(9):
                print(f"{RED}Choose number between 1-9.{RESET}")

            elif board[move] != " ":
                print(f"{RED}That position is already occupied.{RESET}")

            else:
                return move

        except ValueError:
            print(f"{RED}Invalid input! Enter numbers only.{RESET}")


# ==========================
# Toss
# ==========================
def toss():

    print(f"\n{YELLOW}Toss Time!{RESET}")

    while True:

        choice = input("Choose Heads(H) or Tails(T): ").upper()

        if choice in ["H","T"]:
            break

        print("Enter H or T only.")

    result = random.choice(["H","T"])

    print("Coin:", "Heads" if result=="H" else "Tails")

    return choice == result


# ==========================
# Play Game
# ==========================
def play_game():

    board = [" "]*9

    player_turn = toss()

    if player_turn:
        print(f"{GREEN}\nYou won the toss! You play first.{RESET}")
    else:
        print(f"{MAGENTA}\nAI won the toss! AI plays first.{RESET}")

    while True:

        display_board(board)

        if player_turn:

            move = player_move(board)
            board[move] = "X"

            if check_winner(board,"X"):
                display_board(board)
                print(f"{GREEN}🎉 Congratulations! You Win!{RESET}")
                return "Player"

        else:

            print(f"{MAGENTA}AI is thinking...{RESET}")
            time.sleep(1)

            move = ai_move(board)
            board[move] = "O"

            print(f"{BLUE}AI selected position {move+1}{RESET}")

            if check_winner(board,"O"):
                display_board(board)
                print(f"{RED}🤖 AI Wins!{RESET}")
                return "AI"

        if is_draw(board):
            display_board(board)
            print(f"{YELLOW}🤝 Match Draw!{RESET}")
            return "Draw"

        player_turn = not player_turn


# ==========================
# Main
# ==========================
player_score = 0
ai_score = 0
draw_score = 0
games = 0

print("="*50)
print("         TIC TAC TOE WITH SMART AI")
print("="*50)

while True:

    result = play_game()

    games += 1

    if result == "Player":
        player_score += 1

    elif result == "AI":
        ai_score += 1

    else:
        draw_score += 1

    print(f"\n{CYAN}========== SCOREBOARD =========={RESET}")

    print(f"Games Played : {games}")
    print(f"😊 Player Wins : {player_score}")
    print(f"🤖 AI Wins     : {ai_score}")
    print(f"🤝 Draws       : {draw_score}")

    print("="*32)

    again = input("\nPlay Again? (Y/N): ").upper()

    if again != "Y":
        print("\nThanks for playing!")
        break
