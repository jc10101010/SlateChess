from ChessBoard import *
from random import shuffle
import time

#Global variables to track move count and maximum search depth
global count, maxDepth
count = 0
maxDepth = 3  #Depth for the negamax search

#Negamax algorithm with alpha-beta pruning
def negamax(board, depth, side, opposite, alpha, beta):
    global count, maxDepth

    #Generate all legal moves for the current board state
    moves = GenerateLegalMoves(board, side, opposite, depth, maxDepth)
    
    #If a checkmate or stalemate condition is detected
    if moves == "C":
        return "C"

    #If the maximum depth is reached, evaluate the board
    if depth == 0:
        count += 1  #Count the evaluation
        return EvaluateNegamax(board, side)

    maxScore = -10000000000  #Initialize max score to a very low value
    maxMove = ()  #Initialize max move

    #Iterate over all possible moves
    for i in range(len(moves[0])):
        #Recursively call negamax for the new board state after making the move
        score = negamax(Move(board, moves[0][i], moves[1][i]), depth-1, opposite, side, -beta, -alpha)
        
        #Skip checkmate branches
        if score == "C":
            continue
        
        score = -score  #Flip the score for negamax
        
        #Alpha-beta pruning: if score exceeds beta, prune this branch
        if score >= beta:
            return beta
        
        #Update alpha if a new best score is found
        if score > alpha:
            alpha = score
        
        #Keep track of the best move found
        if score > maxScore:
            maxScore = score
            maxMove = (moves[0][i], moves[1][i])

    #At the root of the search tree, return the best move
    if depth == maxDepth:
        print(count)  #Output the number of evaluated positions
        print(maxMove, maxScore)  #Output the best move and its score
        return maxMove

    #If no valid moves found, return a losing score
    if maxScore == -10000000000:
        return -1000
    
    return maxScore  #Return the best score found
