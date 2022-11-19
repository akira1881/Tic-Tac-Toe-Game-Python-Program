import os


# Programmed by: Charina C. Vallecera
# BSCOE 2-2
# Tic Tac Toe Game

def printBoard(gameValues):
    print(f" {gameValues[0]} | {gameValues[1]} | {gameValues[2]} ")
    print(f"---|---|---")
    print(f" {gameValues[3]} | {gameValues[4]} | {gameValues[5]} ")
    print(f"---|---|---")
    print(f" {gameValues[6]} | {gameValues[7]} | {gameValues[8]} ")


def checkWin(gameValues):
    # All Winning Patterns
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        if gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'X':
            printBoard(gameValues)
            print("X Won the match")
            return 1

        if gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'O':
            printBoard(gameValues)
            print("O Won the match")
            return 0

        if all(isinstance(item, str) for item in gameValues):
            printBoard(gameValues)
            return -2

    return -1


if __name__ == '__main__':
    print("Welcome to the Game")
    gameValues=[0, 1, 2, 3, 4, 5, 6, 7, 8]
    chance = 1