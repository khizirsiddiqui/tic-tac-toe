'''
Author: Mohd Khizir Siddiqui
Github: khizirsiddiqui
Using Tutorial: https://inventwithpython.com/chapter10.html
'''

import random
import os

player = 'Player (User)'
computer = 'Computer (AI)'


def draw_board(board):
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('     |     |')
    print('----------------')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('     |     |')
    print('----------------')
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('     |     |')


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("Select X or O:")
        letter = input().upper()
    if letter is 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    if random.randint(0, 1):
        return computer
    else:
        return player


def playAgain():
    print("Do you want to play again?")
    return input().upper().startswith('Y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))


def getBoardCopy(board):
    mockBoard = []
    for i in board:
        mockBoard.append(i)
    return mockBoard


def isSpaceFree(board, move):
    return board[move] == ' '


def getPlayerMove(board):
    move = ' '
    while (move not in '1 2 3 4 5 6 7 8 9'.split() or
           not isSpaceFree(board, int(move))):
        print("Enter your next move:")
        move = input()
        if move in '1 2 3 4 5 6 7 8 9'.split():
            break
        else:
            print('Enter Valid Move')
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def testWinMove(board, letter, move):
    bCopy = getBoardCopy(board)
    makeMove(bCopy, letter, move)
    return isWinner(bCopy, letter)


def testForkMove(board, letter, move):
    bCopy = getBoardCopy(board)
    makeMove(bCopy, letter, move)
    winningMoves = 0
    for j in range(1, 10):
        if testWinMove(bCopy, letter, j) and isSpaceFree(bCopy, j):
            winningMoves += 1
    return winningMoves > 1


def getComputerMove(board, computerLetter):
    if computerLetter is 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        if isSpaceFree(board, i) and testWinMove(board, computerLetter, i):
                return i

    for i in range(1, 10):
        if isSpaceFree(board, i) and testWinMove(board, playerLetter, i):
                return i

    for i in range(1, 10):
        if isSpaceFree(board, i) and testForkMove(board, computerLetter, i):
            return i

    for i in range(1, 10):
        if isSpaceFree(board, i) and testForkMove(board, playerLetter, i):
            return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic-Tac-Toe')
while True:
    theBoard = [' '] * 10

    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()

    print(turn + ' goes first')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == player:
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                print('Hooray! You won.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    print('A TIE')
                    break
                else:
                    turn = computer
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                print('The Computer won. You Lost')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    print('The game is a tie')
                    break
                else:
                    turn = player
        os.system('cls' if os.name == 'nt' else 'clear')
        if isWinner(theBoard, playerLetter):
            print('Hooray! You won.')
        elif isWinner(theBoard, computerLetter):
            print('The Computer won. You Lost')
        else:
            draw_board(theBoard)

    if not playAgain():
        break
