import random
def draw_board(board):
    print(the_board[7] + "|" + the_board[8] + "|" + the_board[9])
    print("-+-+-")
    print(the_board[4] + "|" + the_board[5] + "|" + the_board[6])
    print("-+-+-")
    print(the_board[1] + "|" + the_board[2] + "|" + the_board[3])
    print("\n\n")

def player_turn(the_board, PLAYER_CHOICE, COMPUTER_CHOICE):
    x = int(input("Choose a place "))
    if the_board[x] == " ":
        the_board[x] = PLAYER_CHOICE
    else:
        print("That space is already taken")
        player_turn(the_board, PLAYER_CHOICE, COMPUTER_CHOICE)


def computer_turn(the_board, PLAYER_CHOICE, COMPUTER_CHOICE):
    x = random.randint(1, 9)
    if the_board[x] == " ":
        the_board[x] = COMPUTER_CHOICE
        draw_board(the_board)
    elif the_board[1] and the_board[2] and the_board[3] and the_board[4] and the_board[5] and the_board[6] and the_board[7] and the_board[8] and the_board[9] != " ":
        print("Draw")
        terminate()
    else:
        computer_turn(the_board, PLAYER_CHOICE, COMPUTER_CHOICE)

def check_for_win(the_board):

    if the_board[1] == "X" and the_board[2] == "X" and the_board[3] == "X":
        print("X wins")
        terminate()
    elif the_board[4] == "X" and the_board[5] == "X" and the_board[6] == "X":
        print("X wins")
        terminate()
    elif the_board[7] == "X" and the_board[8] == "X" and the_board[9] == "X":
        print("X wins")
        terminate()
    elif the_board[7] == "X" and the_board[4] == "X" and the_board[1] == "X":
        print("X wins")
        terminate()
    elif the_board[8] == "X" and the_board[5] == "X" and the_board[2] == "X":
        print("X wins")
        terminate()
    elif the_board[9] == "X" and the_board[6] == "X" and the_board[3] == "X":
        print("X wins")
        terminate()
    elif the_board[7] == "X" and the_board[5] == "X" and the_board[3] == "X":
        print("X wins")
        terminate()
    elif the_board[1] == "X" and the_board[5] == "X" and the_board[9] == "X":
        print("X wins")
        terminate()

    elif the_board[1] == "O" and the_board[2] == "O" and the_board[3] == "O":
        print("O wins")
        terminate()
    elif the_board[4] == "O" and the_board[5] == "O" and the_board[6] == "O":
        print("O wins")
        terminate()
    elif the_board[7] == "O" and the_board[8] == "O" and the_board[9] == "O":
        print("O wins")
        terminate()
    elif the_board[7] == "O" and the_board[4] == "O" and the_board[1] == "O":
        print("O wins")
        terminate()
    elif the_board[8] == "O" and the_board[5] == "O" and the_board[2] == "O":
        print("O wins")
        terminate()
    elif the_board[9] == "O" and the_board[6] == "O" and the_board[3] == "O":
        print("O wins")
        terminate()
    elif the_board[7] == "O" and the_board[5] == "O" and the_board[3] == "O":
        print("O wins")
        terminate()
    elif the_board[1] == "O" and the_board[5] == "O" and the_board[9] == "O":
        print("O wins")
        terminate()

the_board = [' '] * 10
global COMPUTER_CHOICE
global PLAYER_CHOICE

def choose_x_or_o():
    PLAYER_CHOICE = input("Do you want to be X or O\n")
    PLAYER_CHOICE = PLAYER_CHOICE.upper()
    while PLAYER_CHOICE != "X" or PLAYER_CHOICE != "O":
        if PLAYER_CHOICE == "X":
            COMPUTER_CHOICE = "O"
            game(PLAYER_CHOICE, COMPUTER_CHOICE)
        elif PLAYER_CHOICE == "O":
            COMPUTER_CHOICE = "X"
            game(PLAYER_CHOICE, COMPUTER_CHOICE)
        else:
            print("Invalid Selection")
            choose_x_or_o()

def game(PLAYER_CHOICE, COMPUTER_CHOICE):
    while True:
        if PLAYER_CHOICE == "X":
            player_turn(the_board, PLAYER_CHOICE, COMPUTER_CHOICE)
            check_for_win(the_board)
            computer_turn(the_board, PLAYER_CHOICE, COMPUTER_CHOICE)
            check_for_win(the_board)
        else:
            computer_turn(the_board, PLAYER_CHOICE, COMPUTER_CHOICE)
            check_for_win(the_board)
            player_turn(the_board, PLAYER_CHOICE, COMPUTER_CHOICE)
            check_for_win(the_board)

def terminate():
    print("Thanks for playing")
    quit()

choose_x_or_o()
