#Global board for position weighting (positional evaluation)
global wBoard
wBoardString = """0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1
3 2 3 3 3 3 2 3
3 3 4 4 4 4 3 3
3 3 4 4 4 4 3 3
3 2 3 3 3 3 2 3
1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0"""

#Parse the positional weighting board into a 2D list
wBoard = [[float(i) for i in line.split()] for line in wBoardString.split("\n")[::-1]]

#Function to display the board state in a readable way
def Display(board):
    print("\n" * 5)  #Print blank lines to clear the screen
    DisplayCode = ["_", "P", "R", "N", "B", "Q", "K", "p", "r", "n", "b", "q", "k"]
    for row in board[::-1]:  #Reverse the board to display it with white at the bottom
        line = ""
        for item in row:
            line += DisplayCode[item] + " "  #Map the pieces to their respective symbols
        print(line)

#Return the value of a square for a specific side (white = 1, black = 2)
#Returns a penalty value if the position is out of bounds
def ValueOf(board, x, y, side):
    if 0 <= x < 8 and 0 <= y < 8:
        return board[y][x]
    else:
        return side * 4  #Penalty for invalid positions (used in slider movement)

#Check if a square is empty (0), occupied by own piece (1), or opponent's piece (2)
def Type(board, x, y):
    if 0 <= x < 8 and 0 <= y < 8:
        if board[y][x] == 0:
            return 0  #Empty
        elif board[y][x] <= 6:
            return 1  #Own piece
        else:
            return 2  #Opponent's piece
    else:
        return 3  #Out of bounds

#Handle sliding moves (used by rooks, bishops, queens)
def Slider(board, x, y, dx, dy, side, opposite):
    tempx, tempy = x, y
    Moves = []
    sliding = True
    
    #Sliding loop (moves until blocked)
    while sliding:
        tempx += dx
        tempy += dy
        currentValue = ValueOf(board, tempx, tempy, side)
        
        if currentValue != 0:
            sliding = False  #Stop sliding when encountering any piece
            if side == 1 and currentValue > 6 or side == 2 and currentValue <= 6:
                Moves.append((tempx, tempy))  #Capture opponent's piece
        else:
            Moves.append((tempx, tempy))  #Add valid move
    return Moves

#Pawn-specific move generation
def PawnMoves(board, x, y, side, opposite):
    Moves = []
    
    if side == 1:  #White pawns move upward
        if ValueOf(board, x, y + 1, side) == 0:
            Moves.append((x, y + 1))
            if y == 1 and board[y + 2][x] == 0:  #Double move for pawns on 2nd rank
                Moves.append((x, y + 2))
        if ValueOf(board, x - 1, y + 1, side) > 6:  #Capture diagonally
            Moves.append((x - 1, y + 1))
        if ValueOf(board, x + 1, y + 1, side) > 6:
            Moves.append((x + 1, y + 1))
    
    elif side == 2:  #Black pawns move downward
        if ValueOf(board, x, y - 1, side) == 0:
            Moves.append((x, y - 1))
            if y == 6 and board[y - 2][x] == 0:  #Double move for pawns on 7th rank
                Moves.append((x, y - 2))
        if ValueOf(board, x - 1, y - 1, side) > 0 and ValueOf(board, x - 1, y - 1, side) <= 6:
            Moves.append((x - 1, y - 1))
        if ValueOf(board, x + 1, y - 1, side) > 0 and ValueOf(board, x + 1, y - 1, side) <= 6:
            Moves.append((x + 1, y - 1))
    
    return Moves

#Knight-specific move generation
def KnightMoves(board, x, y, side, opposite):
    KnightAdjustments = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    Moves = []
    
    #Calculate knight moves
    for adjust in KnightAdjustments:
        move = (adjust[0] + x, adjust[1] + y)
        moveEnd = ValueOf(board, move[0], move[1], side)
        if side == 1 and (moveEnd == 0 or moveEnd > 6):  #Capture opponent's piece or empty square
            Moves.append(move)
        elif side == 2 and moveEnd <= 6:  #Capture opponent's piece
            Moves.append(move)
    
    return Moves

#Rook-specific move generation using the slider
def RookMoves(board, x, y, side, opposite):
    Moves = []
    Moves += Slider(board, x, y, 0, 1, side, opposite)  #Up
    Moves += Slider(board, x, y, 1, 0, side, opposite)  #Right
    Moves += Slider(board, x, y, 0, -1, side, opposite)  #Down
    Moves += Slider(board, x, y, -1, 0, side, opposite)  #Left
    return Moves

#Bishop-specific move generation using the slider
def BishopMoves(board, x, y, side, opposite):
    Moves = []
    Moves += Slider(board, x, y, 1, 1, side, opposite)   #Diagonal up-right
    Moves += Slider(board, x, y, 1, -1, side, opposite)  #Diagonal down-right
    Moves += Slider(board, x, y, -1, -1, side, opposite) #Diagonal down-left
    Moves += Slider(board, x, y, -1, 1, side, opposite)  #Diagonal up-left
    return Moves

#Queen-specific move generation (combines rook and bishop moves)
def QueenMoves(board, x, y, side, opposite):
    return RookMoves(board, x, y, side, opposite) + BishopMoves(board, x, y, side, opposite)

#King-specific move generation
def KingMoves(board, x, y, side, opposite):
    KnightAdjustments = [(1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0)]
    Moves = []
    
    for adjust in KnightAdjustments:
        move = (adjust[0] + x, adjust[1] + y)
        moveEnd = ValueOf(board, move[0], move[1], side)
        if side == 1 and (moveEnd == 0 or moveEnd > 6):  #Capture or move
            Moves.append(move)
        elif side == 2 and moveEnd <= 6:
            Moves.append(move)
    
    return Moves

#Generate all legal moves for a given side
def GenerateLegalMoves(board, side, opposite, depth, maxDepth):
    MoveStart, MoveEnd = [], []
    
    #For each piece on the board, generate its legal moves
    for y in range(8):
        for x in range(8):
            piece = board[y][x]
            if side == 1 and 0 < piece <= 6:  #White pieces
                pieceMoves = []
                if piece == 1: pieceMoves = PawnMoves(board, x, y, side, opposite)
                elif piece == 2: pieceMoves = RookMoves(board, x, y, side, opposite)
                elif piece == 3: pieceMoves = KnightMoves(board, x, y, side, opposite)
                elif piece == 4: pieceMoves = BishopMoves(board, x, y, side, opposite)
                elif piece == 5: pieceMoves = QueenMoves(board, x, y, side, opposite)
                elif piece == 6: pieceMoves = KingMoves(board, x, y, side, opposite)
                
                MoveStart += [(x, y)] * len(pieceMoves)
                MoveEnd += pieceMoves
            
            elif side == 2 and piece > 6:  #Black pieces
                pieceMoves = []
                if piece == 7: pieceMoves = PawnMoves(board, x, y, side, opposite)
                elif piece == 8: pieceMoves = RookMoves(board, x, y, side, opposite)
                elif piece == 9: pieceMoves = KnightMoves(board, x, y, side, opposite)
                elif piece == 10: pieceMoves = BishopMoves(board, x, y, side, opposite)
                elif piece == 11: pieceMoves = QueenMoves(board, x, y, side, opposite)
                elif piece == 12: pieceMoves = KingMoves(board, x, y, side, opposite)
                
                MoveStart += [(x, y)] * len(pieceMoves)
                MoveEnd += pieceMoves
    
    #Check for winning conditions at maximum depth
    if depth != maxDepth:
        for endSpot in MoveEnd:
            if (side == 1 and board[endSpot[1]][endSpot[0]] == 12) or \
               (side == 2 and board[endSpot[1]][endSpot[0]] == 6):
                return "C"
    
    return [MoveStart, MoveEnd]

#Execute a move and return a new board state
def Move(board, start, end):
    newBoard = [line[:] for line in board]  #Copy the board
    piece = newBoard[start[1]][start[0]]    #Get the piece at the start position
    newBoard[start[1]][start[0]] = 0        #Remove the piece from the start position
    newBoard[end[1]][end[0]] = piece        #Place the piece at the end position
    return newBoard

#Remove a piece from the board
def Remove(board, start):
    newBoard = [line[:] for line in board]
    newBoard[start[1]][start[0]] = 0
    return newBoard

#Basic material evaluation function (without positional weighting)
def Evaluate(board):
    Material = [0, 1, 5, 3, 3, 9, 0, -1, -5, -3, -3, -9, 0]
    Value = 0
    for y in range(8):
        for x in range(8):
            piece = board[y][x]
            Value += Material[piece]  #Add the material value of the piece
    return Value

#Evaluation function used in negamax, including positional weighting
def EvaluateNegamax(board, side):
    global wBoard
    Material = [0, 1, 5, 3, 3, 9, 0, -1, -5, -3, -3, -9, 0]
    MaterialPosition = [0, 3, 3, 2.75, 4, 0, 0, -3, -3, -2.75, -4, 0, 0]
    Value = 0
    
    #Add material and positional value of each piece
    for y in range(8):
        for x in range(8):
            piece = board[y][x]
            Value += Material[piece] + (MaterialPosition[piece] * wBoard[y][x] / 100)
    
    return Value if side == 1 else -Value

#Move ordering based on material gain
def MoveOrder(board, side, opposite, res):
    results = [line[:] for line in res]  #Copy the move results
    value = []
    sorted = [[], []]
    
    #Evaluate moves based on material gain
    for i in range(len(results[0])):
        start = results[0][i]
        end = results[1][i]
        startPiece = board[start[1]][start[0]]
        endPiece = board[end[1]][end[0]]
        Material = [0, 1, 5, 3, 3, 9, 0, 1, 5, 3, 3, 9, 0]
        
        if endPiece > 0:
            value.append(Material[endPiece] - Material[startPiece])  #Favor captures
        else:
            value.append(-100)  #Penalize non-captures
    
    #Sort moves by value
    while len(value) > 0:
        largest = max(value)
        largestIndex = value.index(largest)
        sorted[0].append(results[0][largestIndex])
        sorted[1].append(results[1][largestIndex])
        value.pop(largestIndex)
        results[0].pop(largestIndex)
        results[1].pop(largestIndex)
    
    return sorted
