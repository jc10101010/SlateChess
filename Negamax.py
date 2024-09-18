from ChessBoard import *
from random import shuffle
import time

#Global counters to keep track of evaluation calls and search depth
global count, maxDepth
count = 0
maxDepth = 3  #Depth of search for negamax algorithm

#Negamax algorithm with a depth-limited search
def negamax(board, depth, side, opposite):
    global count, maxDepth

    #Generate all legal moves for the current board state
    moves = GenerateLegalMoves(board, side, opposite, depth, maxDepth)
    
    #Check for a checkmate condition (denoted by "C")
    if moves == "C":
        return "C"
    
    #If we reach the maximum depth, evaluate the board
    if depth == 0:
        count += 1
        return EvaluateNegamax(board, side)

    #Initialize variables for tracking the best score and move
    maxScore = -10000000000
    maxMove = ()
    
    #Iterate over all legal moves
    for i in range(len(moves[0])):
        #Recursively call negamax for the new board state after making a move
        score = negamax(Move(board, moves[0][i], moves[1][i]), depth - 1, opposite, side)
        
        #If the result is checkmate, skip this branch
        if score == "C":
            continue
        
        #Negamax's trick: flip the score for the opponent's perspective
        score = -score
        
        #Track the move with the highest score
        if score > maxScore:
            maxScore = score
            maxMove = (moves[0][i], moves[1][i])

    #If at the root of the search tree, return the best move
    if depth == maxDepth:
        print(count)  #Print the number of evaluated positions
        print(maxMove, maxScore)  #Print the best move and its score
        return maxMove

    #If no valid moves were found, return a losing score (e.g., stalemate or no legal moves)
    if maxScore == -10000000000:
        return -1000
    
    return maxScore  #Return the best score found
