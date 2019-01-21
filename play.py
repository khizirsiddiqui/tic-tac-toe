import os
from player import AIPlayer, HumanPlayer
from board import Board

if __name__ == "__main__":
    bd = Board()
    p1 = HumanPlayer(symbol='X')
    p2 = AIPlayer(symbol='O')
    idx = 1
    moves = 0
    while True:
        os.system('clear')
        print("Total " + str(moves) + " moves played")
        if idx == 1:
            p = p1
            q = p2
        elif idx == 0:
            p = p2
            q = p1
        x, y = p.getMove(bd, q)
        if bd.isValidMove(x, y):
            moves += 1
            bd.playMove(x, y, p.symbol)
            bd.draw()
            if bd.playerWins(x, y):
                print(str(p), " WINS ")
                break
            idx = (idx + 1)%2
        else:
            print("Invalid Move " + str(p) + " Try Again")
        
