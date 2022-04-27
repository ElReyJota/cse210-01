#CSE210 Week 2
#Tic-tac-toe game made with python by Julian Hernandez

def main():
    print("\n----------------------------------------Tic Tac Toe----------------------------------------\n")
    x_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    o_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    end = 0

    print("Welcome to Tic Tac Toe, to play select a number from 1-9.")

    #The game itself
    while end != 9:
        move = int(input("\nIs Player 'X' turn, select a number(1-9): "))
        x_moves[move - 1] = "X"
        print_board(x_moves, o_moves)
        end += 1

        if end != 9:
            move = int(input("\nIs Player 'O' turn, select a number(1-9): "))
            o_moves[move - 1] = "O"
            print_board(x_moves, o_moves)
            end += 1
    
    print("\nGood game!")

def move_checker(x_moves, o_moves, move, is_x):
    """
    Checks if a move is valid and if its a winning one.
    
    """

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
        if move.upper() == "X":
            board[counter] = move
            counter += 1
        else:
            counter += 1
    counter = 0

    for move in o_moves:
        if move.upper() == "O":
            board[counter] = move
            counter += 1
        else:
            counter += 1

    print(f"Board: \n{board[0]}|{board[1]}|{board[2]} \n----- \
        \n{board[3]}|{board[4]}|{board[5]} \n----- \n{board[6]}|{board[7]}|{board[8]}")

if __name__ == "__main__":
    main()