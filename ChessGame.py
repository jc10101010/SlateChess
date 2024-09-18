from NegamaxAlphaBetaMoveOrder import *
import time

#Board configuration
BoardString = """8 0 0 0 12 0 0 8
7 10 7 0 0 7 10 7
0 7 9 0 7 0 7 0
0 4 0 0 0 0 4 0
0 9 0 0 0 0 0 0
0 0 0 1 0 1 0 3
1 0 0 3 0 1 0 1
0 0 2 0 6 0 0 2"""

#Parse the board string into a 2D list and reverse to match the board's orientation
board = [[int(i) for i in line.split()] for line in BoardString.split("\n")[::-1]]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

move = ""
Display(board)

while move != "STOP":
    startTime = time.time()
    
    #Get the best move using the negamax algorithm
    minimaxMove = negamax(board, maxDepth, 1, 2, -10000, 10000)
    
    #Update the board with the engine's move
    board = Move(board, minimaxMove[0], minimaxMove[1])
    
    print((time.time() - startTime) * 1000)  #Output move calculation time
    Display(board)
    
    #Parse player move input
    inpList = input().split()
    move = [list(i) for i in inpList]
    move[0][0] = alphabet.index(move[0][0])
    move[0][1] = int(move[0][1]) - 1
    move[1][0] = alphabet.index(move[1][0])
    move[1][1] = int(move[1][1]) - 1
    
    #Update the board with the player's move
    board = Move(board, move[0], move[1])
    Display(board)
