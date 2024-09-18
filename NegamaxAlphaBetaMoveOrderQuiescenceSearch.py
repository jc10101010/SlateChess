from ChessBoard import *
from random import shuffle
import time
global count, maxDepth
count = 0

maxDepth = 5




def negamax(board, depth, side, opposite, alpha, beta):
    global count, maxDepth
    moves = GenerateLegalMoves(board, side, opposite, depth, maxDepth)
    if moves == "C":
        return "C"
    moves = MoveOrder(board, side, opposite, moves)
    if depth == 0:
        max = -10000000000
        capture = False
        for i in range(len(moves[1])):
            if board[moves[1][i][1]][moves[1][i][0]] != 0:
                capture = True
                score = negamax(Move(board, moves[0][i], moves[1][i]), 0, opposite, side, -beta, -alpha)
                if score == "C":
                    continue
                score = -score
                if score >= beta:
                    return beta
                if score > alpha:
                    alpha = score
                if score > max:
                    max = score
        if capture == False:
            count += 1
            return EvaluateNegamax(board, side)
        if max ==  -10000000000:
            return "C"
        return max
    max = -10000000000
    maxMove = ()
    for i in range(len(moves[0])):
        score = negamax(Move(board, moves[0][i], moves[1][i]), depth-1, opposite, side, -beta, -alpha)
        if score == "C":
            continue
        score = -score
        if depth == maxDepth:
            print(moves[0][i], moves[1][i],score)
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

