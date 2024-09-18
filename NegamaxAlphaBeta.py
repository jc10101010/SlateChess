from ChessBoard import *
from random import shuffle
import time
global count, maxDepth
count = 0

maxDepth = 3
def negamax(board, depth, side, opposite, alpha, beta):
    global count, maxDepth
    moves = GenerateLegalMoves(board, side, opposite, depth, maxDepth)
    if moves == "C":
        return "C"
    if depth == 0:
        count += 1
        return EvaluateNegamax(board, side)
    max = -10000000000
    maxMove = ()
    for i in range(len(moves[0])):
        score = negamax(Move(board, moves[0][i], moves[1][i]), depth-1, opposite, side, -beta, -alpha)
        if score == "C":
            continue
        score = -score
        if score >= beta:
            return beta
        if score > alpha:
            alpha = score
        if score > max:
            max = score
            maxMove = (moves[0][i], moves[1][i])
    if depth == maxDepth:
        print(count)
        print(maxMove, max)
        return maxMove
    if max == -10000000000:
        return -1000
    return max
BoardString = """
8 9 10 11 12 10 9 8
7 7 7 7 7 7 7 7
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
2 3 4 5 6 4 3 2"""

BoardString = """
8 0 10 8 0 0 12 0
7 7 7 0 11 7 7 7
0 0 9 0 0 0 9 0
4 0 0 0 7 0 0 10
0 0 1 2 0 1 0 0
1 0 0 4 0 0 3 0
0 1 1 0 5 1 0 1
0 2 4 0 6 0 0 2"""

#if depth == maxDepth:
    #print(moves[0][i], moves[1][i], score)


board = [ [int(i) for i in line.split()] for line in  BoardString.split("\n")[::-1]]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
move = ""

	
	
startTime = time.time()
minimaxMove = negamax(board, maxDepth, 1 , 2, -10000, 10000)
board = Move(board, minimaxMove[0], minimaxMove[1])
print((time.time() - startTime) *1000)
print("\n\n")
	