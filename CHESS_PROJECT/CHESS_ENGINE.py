"""
This Class is responsible for storing all the information about the current state of a chess game. 
It will also be responsible for determining the valid moves at the current state. It will also keep a move log.
"""
class GameState():
    def __init__(self): 
        #this board will be a list of lists, with each list being a row
        #from white's point of view
        #Board is 8*8 2d list, each element of the list has two characters
        #the first character represents the color of the piece, "b" or "w"
        #The second character represents the type of the piece, "K", "Q","R","B","N" or "p"
        # "--" represents an empty space of the board with no pieces
        self.board = [
            ['bR','bN','bB','bQ','bK','bB','bN','bR'],
            ['bp','bp','bp','bp','bp','bp','bp','bp'],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ['wp','wp','wp','wp','wp','wp','wp','wp'],
            ['wR','wN','wB','wQ','wK','wB','wN','wR']
        ]
        self.WhitetoMove = True #determine who's move it is
        self.movelog = []       #a list of moves saved