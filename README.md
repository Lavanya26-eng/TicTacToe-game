# 🎮 Tic Tac Toe with Smart AI

A console-based **Tic Tac Toe** game developed in **Python** where a human player competes against an intelligent computer opponent. The game features a **Smart AI strategy**, a **coin toss** to decide the first player, a **live scoreboard**, colorful console output, and robust input validation to provide an engaging and user-friendly gaming experience.

---

# 📖 Project Overview

**Tic Tac Toe with Smart AI** is a Python-based console application designed to simulate the classic Tic Tac Toe game with an intelligent computer opponent. Unlike a traditional random-move AI, the Smart AI follows strategic decision-making rules such as winning whenever possible, blocking the player's winning moves, occupying the center, choosing corners strategically, and selecting the best available position.

The project demonstrates fundamental Python programming concepts while introducing beginners to simple Artificial Intelligence (AI) techniques used in game development.

---

# 🎯 Project Objectives

- Develop a fully functional console-based Tic Tac Toe game.
- Implement an intelligent AI opponent using rule-based decision making.
- Strengthen logical thinking and problem-solving skills.
- Demonstrate the practical use of Python programming concepts.
- Provide an interactive and enjoyable gaming experience.

---

# ✨ Key Features

- 🎮 Single Player vs Smart AI
- 🪙 Coin Toss to decide who plays first
- 🧠 Intelligent AI with strategic gameplay
- 📊 Live Scoreboard after every match
- 🔄 Play Multiple Rounds
- ❌ Input Validation and Error Handling
- 🤝 Automatic Draw Detection
- 🏆 Winner Announcement
- 🎨 Colored Console Interface
- ⚡ Fast and Lightweight
- 💻 Beginner-Friendly Python Project

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.x | Core Programming Language |
| Random Module | Coin Toss & Random Choices |
| Time Module | Delays and Better User Experience |
| ANSI Escape Codes | Colored Console Output |

---

# 📂 Project Structure

```
TicTacToe/
│
├── tic_tac_toe.py      # Main Python Program
├── README.md           # Project Documentation
```

---

# 🚀 Installation & Execution

## Step 1

Install **Python 3.x**

Download Python from:

https://www.python.org/downloads/

---

## Step 2

Download or Clone the Project

```bash
git clone https://github.com/your-username/TicTacToe.git
```

Or simply download the ZIP file and extract it.

---

## Step 3

Open **Command Prompt** or **Terminal**.

Navigate to the project directory.

```bash
cd TicTacToe
```

---

## Step 4

Run the application.

```bash
python tic_tac_toe.py
```

---

# 🎮 Game Rules

- The game is played between **one player** and the **Smart AI**.
- The player uses **X**.
- The AI uses **O**.
- A coin toss decides who plays first.
- Players take turns placing their symbols on the board.
- The first player to make **three consecutive symbols** horizontally, vertically, or diagonally wins.
- If all positions are filled without a winner, the game ends in a draw.

---

# 🕹️ How to Play

1. Launch the program.
2. Choose **Heads (H)** or **Tails (T)** for the toss.
3. The toss winner starts the game.
4. Enter a board position between **1 and 9**.
5. The Smart AI automatically makes its move.
6. Continue playing until someone wins or the game ends in a draw.
7. Select **Y** to play another game or **N** to exit.

---

# 📍 Board Positions

```
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

Players choose numbers according to the above board positions.

---

# 🤖 Smart AI Strategy

The AI follows a rule-based strategy instead of selecting random moves.

Its decision-making process is:

1. ✅ Check if it can win immediately.
2. 🛡️ Block the player's winning move.
3. ⭐ Occupy the center position if available.
4. 🔄 Take the opposite corner when advantageous.
5. 📐 Select any available corner.
6. ➡️ Choose any remaining side position.

This strategy makes the AI more challenging and improves gameplay.

---

# 📊 Live Scoreboard

After every match, the program automatically updates the scoreboard.

The scoreboard displays:

- 🎮 Games Played
- 😊 Player Wins
- 🤖 AI Wins
- 🤝 Draw Matches

### Example

```
======================================
           SCOREBOARD
======================================

Games Played : 5
Player Wins  : 3
AI Wins      : 1
Draws        : 1
======================================
```

---

# 💻 Python Concepts Used

This project demonstrates several important Python concepts:

- Variables
- Data Types
- Lists
- Functions
- Loops
- Conditional Statements
- Exception Handling
- User Input Validation
- Random Module
- Time Module
- ANSI Color Codes
- Game Logic
- Rule-Based Artificial Intelligence

---

# 📸 Sample Gameplay

```
==================================================
          TIC TAC TOE WITH SMART AI
==================================================

Toss Time!
Choose Heads(H) or Tails(T): H

Coin: Heads

You won the toss!
You will play first.

Current Board              Board Positions

   |   |                  1 | 2 | 3
---+---+---              ---+---+---
   |   |                  4 | 5 | 6
---+---+---              ---+---+---
   |   |                  7 | 8 | 9

Enter your move (1-9): 5

AI selected position 1

 X |   | O
---+---+---
   | X |
---+---+---
   |   |

Game continues...
```

---

# 🎯 Advantages

- ✅ Simple and easy to understand
- ✅ Beginner-friendly Python project
- ✅ Interactive console interface
- ✅ Smart AI provides challenging gameplay
- ✅ Demonstrates Artificial Intelligence concepts
- ✅ Enhances logical thinking and problem-solving skills
- ✅ Well-structured and modular code
- ✅ Lightweight with no external libraries required

---

# 📈 Future Enhancements

The project can be extended with:

- 🖥️ Tkinter GUI Version
- 🌐 Flask Web Application
- 🌍 Online Multiplayer
- 👥 Two Player Mode
- 🤖 Minimax AI (Unbeatable AI)
- 🎚️ Multiple Difficulty Levels
- 💾 Save Scoreboard to File
- 🔊 Sound Effects
- 🏅 Player Profiles
- 📈 Game Statistics Dashboard
- ☁️ Cloud Database Integration
- 📱 Mobile Version

---

# 🎓 Learning Outcomes

By completing this project, learners will gain knowledge of:

- Python Programming Fundamentals
- Modular Programming
- Function-Based Programming
- Game Development Basics
- Artificial Intelligence Concepts
- Input Validation Techniques
- Exception Handling
- Console Application Development
- Decision-Making Algorithms
- Logical Thinking and Problem Solving

---

# 👨‍💻 Project Information

| Property | Details |
|----------|---------|
| **Project Name** | Tic Tac Toe with Smart AI |
| **Language** | Python 3 |
| **Application Type** | Console-Based Game |
| **Programming Paradigm** | Procedural Programming |
| **AI Technique** | Rule-Based Smart AI |

---

# 📄 License

This project is developed **for educational and learning purposes**.

You are free to **use, modify, and distribute** this project for academic, personal, and non-commercial purposes.

---

# ⭐ Author

**K B Lavanya**

*Python Developer | Student | AI & Game Development Enthusiast*
