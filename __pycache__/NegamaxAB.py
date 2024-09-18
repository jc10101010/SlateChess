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
    #
    moves[0] = moves[0][::-1]
    moves[1] = moves[1][::-1]
    #
    if depth == 0:
        count += 1
        return -EvaluateNegamax(board, side)
    maxValue = -10000000000
    maxMove = ()
    checkCount = 0
    for i in range(len(moves[0])):
        score = negamax(Move(board, moves[0][i], moves[1][i]), depth-1, opposite, side, -beta, -alpha)
        #
        if depth == maxDepth:
            print(moves[0][i], moves[1][i], score) 
        #
        if score == "C":
            checkCount += 1
            continue
        if score != "B" and score > maxValue:
            maxValue = score
            maxMove = (moves[0][i], moves[1][i]) 
        alpha = max(alpha, maxValue)
        if alpha >= beta:
            return "B"
    if maxValue == -10000000000:
        if checkCount == len(moves[0]):
            return -1000
        else:
            return "B" 
    if depth == maxDepth:
        print(count)
        return maxMove
    
    return -maxValue