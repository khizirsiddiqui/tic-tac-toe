from random import randint

from board import Board, GAME_STATUS

def intToXY(num):
    pos = [(0, 0), (0, 1), (0, 2), 
           (1, 0), (1, 1), (1, 2), 
           (2, 0), (2, 1), (2, 2), ]
    return pos[num-1]

class Player():
    def __init__(self, symbol, name='Player'):
        self.name = name
        self.score = 0
        self.symbol = symbol

    def __str__(self):
        return str(self.name) + "(" + str(self.symbol) + ")"

class HumanPlayer(Player):
    def getMove(self, board=None, p2=None):
        [x, y] = input("Enter the space seperated cordinates -> x y:").split()
        return int(x), int(y)

class AIPlayer(Player):
    def getMove(self, board, p2):
        bd = [[board.getCopy() for i in range(0, 3)] for j in range(0, 3)]
        bd1 = [[board.getCopy() for i in range(0, 3)] for j in range(0, 3)]
        for i in range(0, 3):
            for j in range(0, 3):
                if bd[i][j].isValidMove(i, j):
                    bd[i][j].playMove(i, j, self.symbol)
                    print(i, j)
                    if bd[i][j].playerWins(i, j):
                        return i, j
                if bd1[i][j].isValidMove(i, j):
                    bd1[i][j].playMove(i, j, p2.symbol)
                    print(i, j)
                    if bd1[i][j].playerWins(i, j):
                        return i, j
        
        return randint(0, 2), randint(0, 2)
