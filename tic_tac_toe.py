'''
Author: Mohd Khizir Siddiqui
Github: khizirsiddiqui
Using Tutorial: https://inventwithpython.com/chapter10.html
Extended with: https://mblogscode.wordpress.com/2016/06/03/python-naughts-cross
                       estic-tac-toe-coding-unbeatable-ai/
'''

import time
import random
import os

player = 'Player (User)'
computer = 'Computer (AI)'
left_margin = '                 '


def draw_board(board):
    for i in range(1, 10):
        print()
    print(left_margin + '     |     |')
    print(left_margin + '  ' + board[7] +
          '  |  ' + board[8] + '  |  ' + board[9])
    print(left_margin + '     |     |')
    print(left_margin + '----------------')
    print(left_margin + '     |     |')
    print(left_margin + '  ' + board[4] +
          '  |  ' + board[5] + '  |  ' + board[6])
    print(left_margin + '     |     |')
    print(left_margin + '----------------')
    print(left_margin + '     |     |')
    print(left_margin + '  ' + board[1] +
          '  |  ' + board[2] + '  |  ' + board[3])
    print(left_margin + '     |     |')


def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print(left_margin + "Select X or O:")
        letter = input(left_margin).upper()
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
    print(left_margin + "Do you want to play again?")
    return input(left_margin).upper().startswith('Y')


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
    while True:
        print(left_margin + 'Play your move? (1-9)')
        move = input(left_margin)
        if move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
            print(left_margin + 'Select from a free space.')
        else:
            break
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


def getComputerMove(board, computerLetter, difficulty):
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

    if difficulty == 2 or difficulty == 3:
        for i in range(1, 10):
            if isSpaceFree(board, i) and testForkMove(board, computerLetter, i):
                return i

        for i in range(1, 10):
            if isSpaceFree(board, i) and testForkMove(board, playerLetter, i):
                return i

    if difficulty == 3:
        playerForks = 0
        for i in range(1, 10):
            if isSpaceFree(board, i) and testForkMove(board, playerLetter, i):
                playerForks += 1
                tempMove = i
        if playerForks == 1:
            return tempMove
        elif playerForks == 2:
            return chooseRandomMoveFromList(board, [1, 3, 5, 7])

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


print(left_margin + 'Welcome to Tic-Tac-Toe')
while True:
    theBoard = [' '] * 10

    playerLetter, computerLetter = inputPlayerLetter()

    print(left_margin + 'Select Difficulty Level:')
    print(left_margin + '1. Easy Beginner (Default)')
    print(left_margin + '2. Warmed Up Cooker')
    print(left_margin + '3. Defeat in Hell')
    difficulty = int(input(left_margin))
    if difficulty not in range(1, 3):
        print(left_margin + 'Try Again')
        continue

    turn = whoGoesFirst()
    move = ' '
    print(left_margin + turn + ' goes first')
    gameIsPlaying = True

    while gameIsPlaying:
        print()
        if turn == player:
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    print(left_margin + 'A TIE')
                    break
                else:
                    turn = computer
        else:
            move = getComputerMove(theBoard, computerLetter, difficulty)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    print(left_margin + 'The game is a tie')
                    break
                else:
                    turn = player
        os.system('cls' if os.name == 'nt' else 'clear')
        if isWinner(theBoard, playerLetter):
            print(left_margin + 'Hooray! ' + player + ' won.')
        elif isWinner(theBoard, computerLetter):
            print(left_margin + computer + ' won. You Lost')
        print()
        draw_board(theBoard)

    if not playAgain():
        break
