GAME_STATUS = [
    'WIN',      # 0
    'DRAW',     # 1
    'NONE',     # 2
    'START'     # 3
]

class Board():
    def __init__(self, status=GAME_STATUS[3], positions=None):
        if positions is None:
            self.positions = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        else:
            self.positions = positions
        self.status=status
        if(status != GAME_STATUS[2]):
            self.draw()
    
    def draw(self):
        for i in range(0, 3):
            print("          |       |       ")
            print("    ", self.positions[i][0], "   |  ", self.positions[i][1], "  |   ", self.positions[i][2])
            print("          |       |       ")
            if (i < 2):
                print("==--------=-------=-------==")

    def playMove(self, x, y, symbol):
        if self.isValidMove(x, y):
            self.positions[x][y] = symbol
            return True
        return False

    def isValidMove(self, x, y):
        print("self.positions" + str(self.positions), end="")
        if (x > 2 or y > 2):
            print("FALSE")
            return False
        if(self.positions[x][y]==' '):
            print("TRUE")
            return True
        print("FALSE")
        return False

    def playerWins(self, x, y):
        if self.positions[0][y] == self.positions[1][y] == self.positions [2][y]:
            return True

        if self.positions[x][0] == self.positions[x][1] == self.positions [x][2]:
            return True

        if x == y and self.positions[0][0] == self.positions[1][1] == self.positions [2][2]:
            return True

        if x + y == 2 and self.positions[0][2] == self.positions[1][1] == self.positions [2][0]:
            return True

        return False 

    def getCopy(self, statusID=2):
        return Board(positions=self.positions, status=GAME_STATUS[statusID])
