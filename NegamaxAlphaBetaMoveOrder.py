from ChessBoard import *
from random import shuffle
import time

#Global variables to track evaluation count and maximum search depth
global count, maxDepth
count = 0
maxDepth = 5  #Search depth limit for the negamax algorithm

#Negamax algorithm with alpha-beta pruning and move ordering
def negamax(board, depth, side, opposite, alpha, beta):
    global count, maxDepth

    #Generate all legal moves for the current board state
    moves = GenerateLegalMoves(board, side, opposite, depth, maxDepth)
    
    #Check for checkmate or stalemate condition
    if moves == "C":
        return "C"

    #If the maximum depth is reached, evaluate the board
    if depth == 0:
        count += 1  #Increment evaluation count
        return EvaluateNegamax(board, side)  #Return the evaluation score
    
    #Reorder moves to improve alpha-beta pruning efficiency
    moves = MoveOrder(board, side, opposite, moves)
    
    maxScore = -10000000000  #Initialize maximum score to a very low value
    maxMove = ()  #Variable to store the best move

    #Iterate through all available moves
    for i in range(len(moves[0])):
        #Recursively call negamax for the new board state after making a move
        score = negamax(Move(board, moves[0][i], moves[1][i]), depth - 1, opposite, side, -beta, -alpha)
        
        #Skip branches that return a checkmate condition
        if score == "C":
            continue
        
        score = -score  #Flip the score for negamax
        
        #If at the root level, print the move and its score (for debugging)
        if depth == maxDepth:
            print(moves[0][i], moves[1][i], score)
        
        #Alpha-beta pruning: if score exceeds beta, prune this branch
        if score >= beta:
            return beta
        
        #Update alpha if a new best score is found
        if score > alpha:
            alpha = score
        
        #Track the best move and its score
        if score > maxScore:
            maxScore = score
            maxMove = (moves[0][i], moves[1][i])

    #If at the root level, print the number of evaluated positions and return the best move
    if depth == maxDepth:
        print(count)  #Output the number of evaluated positions
        print(maxMove, maxScore)  #Output the best move and its score
        return maxMove

    #If no valid moves were found, return a losing score
    if maxScore == -10000000000:
        return -1000

    return maxScore  #Return the best score found
