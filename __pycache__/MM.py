from ChessBoard import *
from random import shuffle
import time
global count
count = 0


def GenerateLegalMoves(board, side, opposite, depth, maxDepth):
	MoveStart = []
	MoveEnd = []
	if side == 1:
		for y in range(8):
			for x in range(8):
				piece = board[y][x]
				if piece > 0 and piece <=6:
					if piece == 1:#pawn
						pieceMoves = PawnMoves(board, x,y, side, opposite)
					elif piece == 2:#rook
						pieceMoves = RookMoves(board, x,y, side, opposite)
					elif piece == 3:#knight:
						pieceMoves = KnightMoves(board, x,y, side, opposite)
					elif piece == 4:#bishop
						pieceMoves = BishopMoves(board, x,y, side, opposite)
					elif piece == 5:#queen
						pieceMoves = QueenMoves(board, x,y, side, opposite)
					elif piece == 6:#king
						pieceMoves = KingMoves(board, x,y, side, opposite)
					MoveStart += [(x,y) for i in range(len(pieceMoves))]
					MoveEnd += pieceMoves
		if depth != maxDepth:
			for endSpot in MoveEnd:
				if board[endSpot[1]][endSpot[0]] == 12:
					return "C"
	elif side == 2:
		for y in range(8):
			for x in range(8):
				piece = board[y][x]
				if piece > 6:
					if piece == 7:#pawn
						pieceMoves = PawnMoves(board, x,y, side, opposite)
					elif piece == 8:#rook
						pieceMoves = RookMoves(board, x,y, side, opposite)
					elif piece == 9:#knight:
						pieceMoves = KnightMoves(board, x,y, side, opposite)
					elif piece == 10:#bishop
						pieceMoves = BishopMoves(board, x,y, side, opposite)
					elif piece == 11:#queen
						pieceMoves = QueenMoves(board, x,y, side, opposite)
					elif piece == 12:#king
						pieceMoves = KingMoves(board, x,y, side, opposite)
					MoveStart += [(x,y) for i in range(len(pieceMoves))]
					MoveEnd += pieceMoves
		if depth != maxDepth:
			for endSpot in MoveEnd:
				if board[endSpot[1]][endSpot[0]] == 6:
					return "C"
				
	return [MoveStart, MoveEnd]


def minimax(board, side, opposite, depth, maxDepth, alpha, beta):
	global count
	if depth == 0:
		GenResults = GenerateLegalMoves(board, side, opposite, depth, maxDepth)
		if GenResults == "C":
			return "C"
		count += 1
		return Evaluate(board)
	GenResults = GenerateLegalMoves(board, side, opposite, depth, maxDepth)
	if GenResults == "C":
		return "C"
	MoveStart = GenResults[0]
	MoveEnd = GenResults[1]
	MoveResults = []
	ValueResults = []
	cCount = 0
	if side == 1:
		for i in range(len(MoveEnd)):
			nextBoard = Move(board, MoveStart[i], MoveEnd[i])
			currentValue = minimax(nextBoard, opposite, side, depth-1,maxDepth,alpha, beta)
			if currentValue == "C":
				cCount += 1
				continue
			ValueResults.append(currentValue)
			MoveResults.append((MoveStart[i], MoveEnd[i]))
		if len(MoveResults) == 0 and bCount == 0:
			return -10000000
		if depth == maxDepth:
			for i in range(len(ValueResults)):
				print(MoveResults[i], ValueResults[i])
			result = ValueResults.index(max(ValueResults))
			print(MoveResults[result][0], MoveResults[result][1], alpha)
			print(count)
			return (MoveResults[result][0], MoveResults[result][1])
		return max(ValueResults)
		
		
	elif side == 2:
		for i in range(len(MoveEnd)):
			nextBoard = Move(board, MoveStart[i], MoveEnd[i])
			currentValue = minimax(nextBoard, opposite, side, depth-1,maxDepth,alpha, beta)
			if currentValue == "C":
				cCount += 1
				continue
			ValueResults.append(currentValue)
			MoveResults.append((MoveStart[i], MoveEnd[i]))
			
		if len(MoveResults) == 0:
			return 10000000
		if depth == maxDepth:
			result = ValueResults.index(min(ValueResults))
			print(MoveResults[result][0], MoveResults[result][1], beta)
			print(count)
			return (MoveResults[result][0], MoveResults[result][1])
		return min(ValueResults)
		
		
		
		
BoardString = """
8 9 10 11 12 10 9 8
7 7 7 7 7 7 7 7
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
2 3 4 5 6 4 3 2"""



board = [ [int(i) for i in line.split()] for line in  BoardString.split("\n")[::-1]]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
move = ""
depth = 4


	
	
startTime = time.time()
minimaxMove = minimax(board, 1 , 2, depth, depth, -1000000000000000, 1000000000000000)
board = Move(board, minimaxMove[0], minimaxMove[1])

print((time.time() - startTime) *1000)
Display(board)


