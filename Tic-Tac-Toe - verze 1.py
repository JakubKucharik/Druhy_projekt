"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Jakub Kuchařík
email: jakub.kucharik@gmail.com
discord: Jakub Kuchařík#8660
"""
import random

print('''
Welcome to Tic Tac Toe
============================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
============================================
Let's start the game
--------------------------------------------
''')

board_size = 3
board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9,
         ]
players = []
#volba symbolů pro hráče a pro počítač

while True:
    user_symbol = input("Enter symbol, you will play with, symbol can´t be number: ")
    if user_symbol.isnumeric():
        continue
    else:
        break
while True:
    pc_symbol = input("Enter symbol, computer will play with, symbol can´t be number: ")
    if pc_symbol.isnumeric():
        continue
    else:
        break
players.append(user_symbol)
players.append(pc_symbol)
player = players[0]
game_running = True
winner = None
choice = ""


def show_board(board):
    print("_" * 8 * board_size)
    for i in range(board_size):
        print(("--" * 3 + "| ")*3)
        print(" ", board[i*3], "  |  ", board[1+i*3], "  |  ", board[2+i*3], "  | ")
def player_input():
    global choice
    valid = False
    while not valid:
        print("============================================")
        choice = input(f"Player {players[0]} | Please enter your move number: ")
        print("============================================")
        if choice.isnumeric() and choice not in \
          ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            print("Number must be integer between 1 and 9")
            valid = False
        elif not choice.isnumeric():
            print("You have to enter a number")
            valid = False
        elif choice == "q":
            quit()
        elif board[int(choice)-1] == players[0] or board[int(choice)-1] == players[1]:
            print("This spot is occupied, choose different spot number")
            valid = False
        elif choice in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            valid = True
    board[int(choice) - 1] = player

def computer_turn(board):
    # výběr pole počítače
    # najít místo, na které je možné dát znak počítače O
    while player == players[0]:
        computer_choice = random.randint(0, 8)
        if board[computer_choice] != players[0] and board[computer_choice] != players[1]:
            board[computer_choice] = players[1]
            switch_player()

def check_horizontal(board):
    global winner
    # horizontálně
    if board[0] == board[1] == board[2]:
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5]:
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8]:
        winner = board[6]
        return True
def check_vertical(board):
    global winner
    # vertikálně
    if board[0] == board[3] == board[6]:
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7]:
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8]:
        winner = board[2]
        return True
def check_diagonal(board):
    global winner
    # diagonálně
    if board[0] == board[4] == board[8]:
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6]:
        winner = board[2]
        return True
def check_winner():
    global game_running
    if check_horizontal(board) or check_vertical(board) or check_diagonal(board):

        game_running = False
        return True
    else:
        return False

def switch_player():
    global player
    if player == players[0]:
        player = players[1]
    elif player == players[1]:
        player = players[0]
def check_tie(board):
    global game_running
    if 1 not in board and 2 not in board and 3 not in board and 4 not in board \
            and 5 not in board and 6 not in board and 7 not in board \
            and 8 not in board and 9 not in board and check_winner() == False:

        game_running = False
        return True
    else:
        return False

while game_running:
    show_board(board)
    player_input()
    if check_winner():
        check_winner()
        show_board(board)
        print(f'''
============================================
Congratulations, the player {winner} WON!
============================================''')
        break

    if check_tie(board):
        check_tie(board)
        show_board(board)
        print(f'''
============================================
It´s a TIE!
============================================''')
        break
#--------------------------------------------------------------------
    computer_turn(board)
#--------------------------------------------------------------------
    if check_winner():
        check_winner()
        show_board(board)
        print(f'''
============================================
Congratulations, the player {winner} WON!
============================================''')
        break

    if check_tie(board):
        check_tie(board)
        show_board(board)
        print(f'''
============================================
It´s a TIE!
============================================''')
        break
    switch_player()





