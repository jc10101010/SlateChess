
global wBoard
wBoardString = """0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
3 2 3 3 3 3 2 3
3 3 4 4 4 4 3 3
3 3 4 4 4 4 3 3
3 2 3 3 3 3 2 3
1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0"""




wBoard = [ [float(i) for i in line.split()] for line in  wBoardString.split("\n")[::-1]]



def Display(board):
	print("\n"*5)
	DisplayCode = ["_", "P", "R", "N", "B", "Q", "K", "p", "r", "n", "b", "q", "k"]
	for row in board[::-1]:
		line = ""
		for item in row:
			line += DisplayCode[item]
			line += " "
		print(line)
		
def ValueOf(board, x,y, side):
	if x > -1 and x < 8 and y > -1 and y < 8:
		return board[y][x]
	else:
		return side *4

def Type(board,x,y):
	if y >= 0 and y <= 7 and x >= 0 and x <= 7:
		if board[y][x] == 0:
			return 0
		elif board[y][x] <= 6:
			return 1
		elif board[y][x] > 6:
			return 2
	else:
		return 3

def Slider(board, x, y , dx, dy, side, opposite):
	tempx = x
	tempy = y
	Moves = []
	sliding = True
	if side == 1:
		while sliding:
			tempx += dx
			tempy += dy
			
			currentValue = ValueOf(board, tempx, tempy, side)
			if currentValue != 0:
				sliding = False
				if currentValue > 6:
					Moves.append( (tempx,tempy))
			else:
				Moves.append( (tempx,tempy))
		return Moves
	elif side == 2:
		while sliding:
			tempx += dx
			tempy += dy
			
			currentValue = ValueOf(board, tempx, tempy, side)
			
			if currentValue != 0:
				sliding = False
				if currentValue <= 6:
					Moves.append( (tempx,tempy))
			else:
				Moves.append( (tempx,tempy))
		return Moves




def PawnMoves(board, x, y, side, opposite):

	Moves = []
	if side == 1:
		if ValueOf(board,x, y+1, side) == 0:
			Moves.append( (x,y+1))
			if y == 1 and board[y+2][x] == 0:
				Moves.append( (x,y+2))
		if ValueOf(board,x-1, y+1, side) > 6:
			Moves.append( (x-1,y+1))
		if ValueOf(board,x+1, y+1, side) > 6:
			Moves.append( (x+1,y+1))
	elif side == 2:
		if ValueOf(board,x, y-1, side) == 0:
				Moves.append( (x,y-1))
				if y == 6 and board[y-2][x] == 0:
					Moves.append( (x,y-2))
		bl = ValueOf(board,x-1, y-1, side)
		if  bl > 0 and bl <= 6:
			Moves.append( (x-1,y-1))
		br = ValueOf(board,x+1, y-1, side)
		if br > 0 and br <= 6:
			Moves.append( (x+1,y-1))
			
		
			
			
				
	return Moves
	
def KnightMoves(board, x, y, side, opposite):
	KnightAdjustments = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
	Moves = []
	if side == 1:
		for adjust in KnightAdjustments:
			move = (adjust[0] + x, adjust[1] + y)
			moveEnd = ValueOf(board, move[0], move[1], side)
			if moveEnd == 0 or moveEnd > 6:
				Moves.append(move)
		return Moves
	elif side == 2:
		for adjust in KnightAdjustments:
			move = (adjust[0] + x, adjust[1] + y)
			moveEnd = ValueOf(board, move[0], move[1], side)
			if moveEnd <= 6:
				Moves.append(move)
		return Moves
	
	
def RookMoves(board, x, y, side, opposite):
	Moves = []
	Moves += Slider(board,x,y, 0,1,side,opposite)
	Moves += Slider(board,x,y, 1,0,side,opposite)
	Moves += Slider(board,x,y, 0,-1,side,opposite)
	Moves += Slider(board,x,y, -1,0,side,opposite)
	return Moves
	
	
def BishopMoves(board, x, y, side, opposite):
	Moves = []
	Moves += Slider(board,x,y, 1,1,side,opposite)
	Moves += Slider(board,x,y, 1,-1,side,opposite)
	Moves += Slider(board,x,y, -1,-1,side,opposite)
	Moves += Slider(board,x,y, -1,1,side,opposite)
	return Moves
	
def QueenMoves(board, x, y, side, opposite):
	Moves = []
	Moves += Slider(board,x,y, 0,1,side,opposite)
	Moves += Slider(board,x,y, 1,0,side,opposite)
	Moves += Slider(board,x,y, 0,-1,side,opposite)
	Moves += Slider(board,x,y, -1,0,side,opposite)
	Moves += Slider(board,x,y, 1,1,side,opposite)
	Moves += Slider(board,x,y, 1,-1,side,opposite)
	Moves += Slider(board,x,y, -1,-1,side,opposite)
	Moves += Slider(board,x,y, -1,1,side,opposite)
	return Moves
	
	
	
def KingMoves(board, x, y, side, opposite):
	KnightAdjustments = [(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0)]
	Moves = []
	if side == 1:
		for adjust in KnightAdjustments:
			move = (adjust[0] + x, adjust[1] + y)
			moveEnd = ValueOf(board, move[0], move[1], side)
			if moveEnd == 0 or moveEnd > 6:
				Moves.append(move)
		return Moves
	elif side == 2:
		for adjust in KnightAdjustments:
			move = (adjust[0] + x, adjust[1] + y)
			moveEnd = ValueOf(board, move[0], move[1], side)
			if moveEnd <= 6:
				Moves.append(move)
		return Moves

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

def Move(board, start, end):
	newBoard = [line[:] for line in board]
	piece = newBoard[start[1]][start[0]]
	newBoard[start[1]][start[0]] = 0
	newBoard[end[1]][end[0]] = piece
	return newBoard
def Remove(board, start):
	newBoard = [line[:] for line in board]
	newBoard[start[1]][start[0]] = 0
	return newBoard
	

		
def Evaluate(board):
	Material = [0,1,5,3,3,9,0,-1,-5,-3,-3,-9,0]
	Value = 0
	for y in range(8):
		for x in range(8):
			piece = board[y][x]
			Value += Material[piece]
	return Value


def EvaluateNegamax(board, side):
	global wBoard
	Material = [0,1,5,3,3,9,0,-1,-5,-3,-3,-9,0]
	MaterialPosition = [0,3,3,2.75,4,0,0,-3,-3,-2.75,-4,0,0]
	Value = 0
	addition = 0
	for y in range(8):
		for x in range(8):
			piece = board[y][x]
			Value += Material[piece]
			Value += MaterialPosition[piece] * wBoard[y][x] / 100
	if side == 1:
		return Value
	elif side == 2:
		return -Value

def MoveOrder(board, side,opposite, res):
    results = [line[:] for line in res]
    value = []
    sorted = [[],[]]
    for i in range(len(results[0])):
        start = results[0][i]
        end = results[1][i]

        startPiece = board[start[1]][start[0]]
        endPiece = board[end[1]][end[0]]
        Material = [0,1,5,3,3,9,0,1,5,3,3,9,0]
        if endPiece > 0:
            value.append(Material[endPiece] - Material[startPiece])
        else:
            value.append(-100)
    while len(value)> 0:
        largest = max(value)
        largestIndex = value.index(largest)
        sorted[0].append(results[0][largestIndex])
        sorted[1].append(results[1][largestIndex])
        value.pop(largestIndex)
        results[0].pop(largestIndex)
        results[1].pop(largestIndex)

    return sorted