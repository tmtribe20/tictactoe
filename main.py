
import random
import os
import sys

game_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_on = True

def reset_board():
    game_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return game_board

def draw_board(game_board):
    print(
        f" {game_board[0]} | {game_board[1]} | {game_board[2]}\n {game_board[3]} | {game_board[4]} | {game_board[5]}\n {game_board[6]} | {game_board[7]} | {game_board[8]}")

def chose_starting_player():
    starting_player = random.randint(1,2)
    return starting_player

def player(selected_player):
    if selected_player == 1:
        selected_player = 2
        return selected_player
    elif selected_player == 2:
        selected_player = 1
        return selected_player


def player_turn(game_board,selected_player):

    draw_board(game_board)
    player_move = input(f"Player {selected_player} turn , please"
                        f" enter a valid position from board :")
    player_move = int(player_move)
    if selected_player == 1:
        if player_move in range(1, 10):
            if player_move in game_board:
                game_board[player_move-1] = "X"
            else:
                print("Please enter a valid position")
                player_turn(game_board, selected_player)
        else:
            print("Please enter a valid position")
            player_turn(game_board, selected_player)
    elif selected_player == 2:
        if player_move in range(1, 10):
            if player_move in game_board:
                game_board[player_move-1] = "O"
            else:
                print("Please enter a valid position")
                player_turn(game_board, selected_player)
    os.system("clear")
    return game_board, selected_player

def check_winner(game_board):
    if game_board[0] == game_board[1] == game_board[2] == "X":
        print("Winner is player 1")
        game_on = False
        return game_on

    elif game_board[0] == game_board[1] == game_board[2] == "O":
        print("Winner is player 2")
        game_on = False
        return game_on

    elif game_board[3] == game_board[4] == game_board[5] == "X":
        print("Winner is player 1")
        game_on = False
        return game_on

    elif game_board[3] == game_board[4] == game_board[5] == "O":
        print("Winner is player 2")
        game_on = False
        return game_on

    elif game_board[6] == game_board[7] == game_board[8] == "X":
        print("Winner is player 1")
        game_on = False
        return game_on

    elif game_board[6] == game_board[7] == game_board[8] == "O":
        print("Winner is player 2")
        game_on = False
        return game_on

    elif game_board[0] == game_board[3] == game_board[6] == "X":
        print("Winner is player 1")
        game_on = False
        return game_on

    elif game_board[0] == game_board[3] == game_board[6] == "O":
        print("Winner is player 2")
        game_on = False
        return game_on

    elif game_board[1] == game_board[4] == game_board[7] == "X":
        print("Winner is player 1")
        game_on = False
        return game_on

    elif game_board[1] == game_board[4] == game_board[7] == "O":
        print("Winner is player 2")
        game_on = False
        return game_on

    elif game_board[2] == game_board[5] == game_board[8] == "X":
        print("Winner is player 1")
        game_on = False
        return game_on

    elif game_board[2] == game_board[5] == game_board[8] == "O":
        print("Winner is player 2")
        game_on = False
        return game_on

    elif game_board[0] == game_board[4] == game_board[8] == "X":
        print("Winner is player 1")
        game_on = False
        return game_on

    elif game_board[0] == game_board[4] == game_board[8] == "O":
        print("Winner is player 2")
        game_on = False
        return game_on

    elif game_board[2] == game_board[4] == game_board[6] == "X":
        print("Winner is player 1")
        game_on = False
        return game_on

    elif game_board[2] == game_board[4] == game_board[6] == "O":
        print("Winner is player 2")
        game_on = False
        return game_on
    if not all(isinstance(x, (str)) for x in game_board):
        game_on = True
        return game_on

    else:
        print("Draw")
        game_on = False
        return game_on


def main(game_board):
    global game_on
    selected_player = chose_starting_player()

    while game_on:
        selected_player = player(selected_player)
        print(selected_player)
        os.system("clear")
        player_turn(game_board, selected_player)
        game_on = check_winner(game_board)


    new_game = input("Would you like to play again? (y/n)")
    if new_game == "y":
        game_on = True
        game_board=reset_board()
        main(game_board)
    else:
        print("Thanks for playing!")
        sys.exit()






if __name__ == "__main__":
    main(game_board)
