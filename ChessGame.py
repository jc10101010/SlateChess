from NegamaxAlphaBetaMoveOrder import *
import time
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
8 0 0 0 12 0 0 8
7 10 7 0 0 7 10 7
0 7 9 0 7 0 7 0
0 4 0 0 0 0 4 0
0 9 0 0 0 0 0 0
0 0 0 1 0 1 0 3
1 0 0 3 0 1 0 1
0 0 2 0 6 0 0 2"""




board = [ [int(i) for i in line.split()] for line in  BoardString.split("\n")[::-1]]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
move = ""
Display(board)
while move != "STOP":
	
	
	startTime = time.time()
	minimaxMove = negamax(board, maxDepth, 1 , 2, -10000, 10000)
	board = Move(board, minimaxMove[0], minimaxMove[1])
	
	print((time.time() - startTime) *1000)
	Display(board)
	
	
	inpList = input().split()
	move = [list(i) for i in inpList]
	move[0][0] = alphabet.index(move[0][0])
	move[0][1] = int(move[0][1]) -1
	move[1][0] = alphabet.index(move[1][0])
	move[1][1] = int(move[1][1])-1
	
	board = Move(board, move[0], move[1])
	Display(board)

	
	
	

# , null move search, iterative deepening, aspiration windows, hsitory history heuristic
