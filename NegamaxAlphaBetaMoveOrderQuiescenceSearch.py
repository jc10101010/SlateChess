from ChessBoard import *
from random import shuffle
import time

#Global variables to track evaluation count and maximum search depth
global count, maxDepth
count = 0
maxDepth = 5  #Maximum search depth for the negamax algorithm

#Negamax algorithm with alpha-beta pruning and move ordering and quiescence search
def negamax(board, depth, side, opposite, alpha, beta):
    global count, maxDepth

    #Generate all legal moves for the current board state
    moves = GenerateLegalMoves(board, side, opposite, depth, maxDepth)
    
    #Check for checkmate or stalemate condition
    if moves == "C":
        return "C"

    #Reorder moves to improve pruning efficiency (move sorting helps alpha-beta pruning)
    moves = MoveOrder(board, side, opposite, moves)

    #Base case: If depth is 0, evaluate the position
    if depth == 0:
        maxScore = -10000000000  #Initialize the max score with a very low value
        capture = False  #Flag to check if a capture move is available

        #Loop through moves to check for capture moves
        for i in range(len(moves[1])):
            if board[moves[1][i][1]][moves[1][i][0]] != 0:  #If a capture move is possible
                capture = True
                #Recursively call negamax with depth 0 for captures
                score = negamax(Move(board, moves[0][i], moves[1][i]), 0, opposite, side, -beta, -alpha)
                if score == "C":
                    continue
                score = -score  #Negate the score for the opponent

                #Apply alpha-beta pruning
                if score >= beta:
                    return beta
                if score > alpha:
                    alpha = score
                if score > maxScore:
                    maxScore = score
        
        #If no capture moves, perform a regular evaluation
        if capture == False:
            count += 1  #Count the evaluation
            return EvaluateNegamax(board, side)  #Return the evaluation score

        #If no valid move is found, return "C" (e.g., checkmate)
        if maxScore == -10000000000:
            return "C"
        
        return maxScore  #Return the max score for capture moves

    #Regular negamax search beyond depth 0
    maxScore = -10000000000  #Initialize the max score
    maxMove = ()  #Variable to store the best move

    #Loop through all available moves
    for i in range(len(moves[0])):
        #Recursively call negamax for the new board state
        score = negamax(Move(board, moves[0][i], moves[1][i]), depth - 1, opposite, side, -beta, -alpha)
        
        #Skip branches that return a checkmate condition
        if score == "C":
            continue
        
        score = -score  #Negate the score for negamax
        
        #If at the root level, print the move and score (for debugging)
        if depth == maxDepth:
            print(moves[0][i], moves[1][i], score)

        #Apply alpha-beta pruning: If score exceeds beta, prune this branch
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
