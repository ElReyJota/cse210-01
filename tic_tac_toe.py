#CSE210 Week 2
#Assignment: Tic-tac-toe game made with python.
#Author: Julian Hernandez

from pickle import TRUE


def main():
    print("\n----------------------------------------Tic Tac Toe----------------------------------------\n")
    x_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    o_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    turn = 0
    counter = 0

    print("Welcome to Tic Tac Toe, to play select a number from 1-9.")

    #The game itself
    while True:
        if counter == 9:
            print_board(x_moves, o_moves)
            print("\nIt's a Draw!")
            break

        elif turn == 0:
            print_board(x_moves, o_moves)
            move = int(input("\nIs Player 'X' turn, select a number(1-9): "))

            if move_checker(x_moves, o_moves, move, True) == "Winning Move!":
                x_moves[move - 1] = "X"
                print_board(x_moves, o_moves)
                print("\nPlayer X wins, congratulations!")
                break

            elif move_checker(x_moves, o_moves, move, True) == "Invalid Move!":
                turn = 0
                print("\nInvalid Move!")

            elif move_checker(x_moves, o_moves, move, True) == "X":
                x_moves[move - 1] = "X"
                turn = 1
                counter += 1

        elif turn == 1:
            print_board(x_moves, o_moves)
            move = int(input("\nIs Player 'O' turn, select a number(1-9): "))

            if move_checker(x_moves, o_moves, move, False) == "Winning Move!":
                o_moves[move - 1] = "O"
                print_board(x_moves, o_moves)
                print("\nPlayer O wins, congratulations!")
                break
            
            elif move_checker(x_moves, o_moves, move, False) == "Invalid Move!":
                turn = 1
                print("\nInvalid Move!")
            
            elif move_checker(x_moves, o_moves, move, False) == "O":
                o_moves[move - 1] = "O"
                turn = 0
                counter += 1

def move_checker(x_mv, o_mv, move, is_x=False):
    """
    Checks if a move is valid and if its a winning one.
    Parameters:
        x_mv: The moves that "x" has done in the game.
        o_mv: The moves that "o" has done in the game.
        move: The move that is to be updated.
        is_x: If true will make move in x, else it will do it in o.
    Return: x_moves or o_moves.
    """
    if is_x:
        if o_mv[move - 1] != "O" and x_mv[move -1] != "X":
            x_mv[move - 1] = "X"
            if x_mv[0] == "X" and x_mv[1] == "X" and x_mv[2] == "X" or x_mv[3] == "X" and x_mv[4] == "X" and x_mv[5] == "X" \
            or x_mv[6] == "X" and x_mv [7] == "X" and x_mv[8] == "X":
                return "Winning Move!"
            elif x_mv[0] == "X" and x_mv[3] == "X" and x_mv[6] == "X" or x_mv[1] == "X" and x_mv[4] == "X" and x_mv[7] == "X" \
            or x_mv[2] == "X" and x_mv[5] == "X" and x_mv[8] == "X":
                return "Winning Move!"
            elif x_mv[0] == "X" and x_mv[4] == "X" and x_mv[8] == "X" or x_mv[2] == "X" and x_mv[4] == "X" and x_mv[6] == "X":
                return "Winning Move!"
            else:
                x_mv[move - 1] = move
                return "X"
        else: return "Invalid Move!"

    elif is_x == False:
        if x_mv[move - 1] != "X" and o_mv[move - 1] != "O":
            o_mv[move - 1] = "O"
            if o_mv[0] == "O" and o_mv[1] == "O" and o_mv[2] == "O" or o_mv[3] == "O" and o_mv[4] == "O" and o_mv[5] == "O" \
            or o_mv[6] == "O" and o_mv [7] == "O" and o_mv[8] == "O":
                return "Winning Move!"
            elif o_mv[0] == "O" and o_mv[3] == "O" and o_mv[6] == "O" or o_mv[1] == "O" and o_mv[4] == "O" and o_mv[7] == "O" \
            or o_mv[2] == "O" and o_mv[5] == "O" and o_mv[8] == "O":
                return "Winning Move!"
            elif o_mv[0] == "O" and o_mv[4] == "O" and o_mv[8] == "O" or o_mv[2] == "O" and o_mv[4] == "O" and o_mv[6] == "O":
                return "Winning Move!"
            else:
                o_mv[move - 1] = move 
                return "O"
        else: return "Invalid Move!"

def print_board(x_moves, o_moves):
    """
    Takes 2 lists with the moves of each player and prints the board in the terminal.
    Parameters:
        x_moves: The moves that "x" has done in the game.
        o_moves: The moves that "o" has done in the game.
    Return: Nothing
    """
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    counter = 0

    #Checks the moves of player x and then of player o
    for move in x_moves:
        if move == "X" or move == "Winning Move!":
            board[counter] = "X"
            counter += 1
        else:
            counter += 1
    counter = 0

    for move in o_moves:
        if move == "O" or move == "Winning Move!":
            board[counter] = "O"
            counter += 1
        else:
            counter += 1

    print(f"Board: \n{board[0]}|{board[1]}|{board[2]} \n----- \
        \n{board[3]}|{board[4]}|{board[5]} \n----- \n{board[6]}|{board[7]}|{board[8]}")

if __name__ == "__main__":
    main()