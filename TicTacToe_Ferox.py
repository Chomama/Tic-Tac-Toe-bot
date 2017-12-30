"""Team Ferox
Tic Tac Toe
11/15/16"""


#draw board
import random
def drawboard():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    print()
def getBoardCopy(board): #reference to http://inventwithpython.com/chapter10.html
    # Make a duplicate of the board list and return it the duplicate.
    copyofboard = []

    for i in board:
        copyofboard.append(i)

    return copyofboard

#Def moves for player
def playermove(move):
    while move < 0 or move > 9:
        print("Invalid input")
        return False
    else:
        if board[move-1] != "x" and board[move-1]!="o":
            board[move-1]="x"
        else:
            print("This space is already taken")
            return False

def isSpaceFree(board, move): #reference http://inventwithpython.com/chapter10.html
    # Return true if the passed move is free on the passed board.
    if board[move] != "x" and board[move]!="o":
        return True
def makeMove(board, player, move): 
    board[move] = player

#Def moves for computer
def ai():
    corners=[0,2,6,8]
    possiblecorners=[]
    center=4
    sides=[1,3,5,7]
    possiblesides=[]
    possiblemoves=[]
    for x in range(0,len(board)): 
        if board[x]!="x" and board[x]!="o":
            possiblemoves.append(x) #prints possible moves
        #print(possiblemoves)
    for i in range(0, 9): #reference http://inventwithpython.com/chapter10.html
        #checks if the ai could win in the next move
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, 'o', i)
            if isWinner(copy, 'o'):
                return i
    for i in range(0, 9): #refernce http://inventwithpython.com/chapter10.html
        #checcks if player could win in the next move
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, 'x', i)
            if isWinner(copy, 'x'):
                return i
    if board[4]=='o':  #goes to side to prevent player from using corner strat
        if corners[1] not in possiblemoves and corners[2] not in possiblemoves:
            if 7 in possiblemoves:
                return 7
        if corners[0] not in possiblemoves and corners[3] not in possiblemoves:
            if 1 in possiblemoves:
                return 1
    if len(possiblemoves)>0:
        for i in range(0,4): #if a corner is taken, ai takes middle
            if corners[i] not in possiblemoves and 4 in possiblemoves:
                return 4
        for i in range(0,4): #lists possible corners
            if corners[i] in possiblemoves:
                possiblecorners.append(corners[i])
        if len(possiblecorners)>0: #goes to corner if available
            return possiblecorners[random.randint(0, len(possiblecorners)-1)]
        if isSpaceFree(board, 4):  #goes to center if no corners
            return 4
        for i in range(0,4):
            if sides[i] in possiblemoves:
                possiblesides.append(sides[i])
                print(possiblesides)
                return possiblesides[0]
        
    
#determine win conditions
def isWinner(bo, le): #reference http://inventwithpython.com/chapter10.html
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or # across the bottom
    (bo[3] == le and bo[4] == le and bo[5] == le) or # across the middle
    (bo[0] == le and bo[1] == le and bo[2] == le) or # across the top
    (bo[6] == le and bo[3] == le and bo[0] == le) or # down the left side
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the middle
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the right side
    (bo[6] == le and bo[4] == le and bo[2] == le) or # diagonal
    (bo[8] == le and bo[4] == le and bo[0] == le)) # diagonal
def boardfull(board):
    count=0
    for x in range(0,9):
        if board[x]=='x' or board[x]=='o':
            count+=1
    #print("count", count)
    if count==8:
        return False
    else:
        return True

#count for who wins
countPlayer=0
countAI=0
board=[1,2,3,4,5,6,7,8,9]
gamerun=True
while gamerun:
    drawboard()
    gamerun=boardfull(board)
    if gamerun==False:
        move= int(input("Your moves are represented by x.  Please enter where your move(1-9): "))
        board[move-1]='x'
        drawboard()
        print("The board is full.  It is a tie")
        print("The current score is: Player=", countPlayer, "AI=", countAI)
        restart=input("Do you wish to play again?(y/n): ")
        if restart == "y":
            gamerun=True
            board=[1,2,3,4,5,6,7,8,9]
    elif gamerun == True:
        move= int(input("Your moves are represented by x.  Please enter your move(1-9): "))
        while playermove(move)==False:
            move= int(input("Your moves are represented by x.  Please enter where your move(1-9): "))
        board[ai()]='o'
    if isWinner(board, 'x'):
        drawboard()
        print("You won")
        countPlayer+=1
        gamerun=False
    elif isWinner(board, 'o'):
        drawboard()
        print("You Lost")
        countAI+=1
        gamerun=False
    if gamerun==False:
        print("The current score is: Player=", countPlayer, "AI=", countAI)
        restart=input("Do you wish to play again?(y/n): ")
        if restart == "y":
            gamerun=True
            board=[1,2,3,4,5,6,7,8,9]
        
        
