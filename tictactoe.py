import random
def drawBoard(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[1] + "|" + board[2] + "|" + board[3])

def inputPlayerLetter():
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()
    
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]

def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return "Computer"
    else:
        return "Player"

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return (
        (bo[7] == le and bo[8] == le and bo[9] == le) or # Across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # Across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # Across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # Down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # Down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # Down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # Diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le) # Diagonal
        )

def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == " "

def getPlayerMove(board):
    move = " "
    while move not in  "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(move)):
        print("What is your next move? (1-9)")
        move = input()
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
    
def getComputerMove(board, computerLetter):
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"
    
    ### Tic-Tac-Toe AI ###
    # Check if the computer can win in the next move
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
            
    # Check if the player can win in the next move and block them
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
            
    # Try to take one of the corners, if possible
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    
    # Try to take the center, if possible
    if isSpaceFree(board, 5):
        return 5
    
    #Move on one of the sides
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

print("Welcome to Tic-Tac-Toe!")

while True:
    theBoard = [" "] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("The " + turn + " will go first.")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == "Player":
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Hooray! You have won the game!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = "Computer"
        
        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("The computer has beaten you! You lost.")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie!")
                    break
                else:
                    turn = "Player"
    
    print("Do you want to play again? (yes or no)")
    if not input().lower().startswith("y"):
        break