"""
This is our main driver file. It will be responsible for handling user input and displaying the current GameState object
"""

from tkinter.tix import IMAGE
import pygame as p
import CHESS_ENGINE as ChessEngine
from CHESS_ENGINE import GameState

p.init()
WIDTH = 512
HEIGHT = 512 #400 is an option (512 is a power of 2, can be nicely divided by 8)
DIMENSION = 8 #Dimensions of a chess board 8*8
SQ_SIZE = HEIGHT//DIMENSION #512//8
MAX_FPS = 15 #for animation
IMAGES = {}

'''
Initialize a global directoy of images. This will be called exactly once
We only want to load the images one time, at the beggining 
'''
def load_Imiages():
    pieces = ['wp','wR','wN','wB','wK','wQ','bp','bR','bN','bB','bK','bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("CHESS_PROJECT/Chess_Pieces/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    #Note: we can access an image by saying "IMAGES['wp']"

'''
This is the main driver for our code. This will handle user input and updating the graphics
'''
def main():
    p.init() #this is th efirst time in our code PyGame is being called so we can init it here
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    
    game_state = ChessEngine.GameState()  #calls the __init__ constructor in CHESS_ENGINE and creates the variables that we have set in it
    print(game_state.board)
    load_Imiages() #only done once
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #(x , y )

        DrawGameState(screen, game_state)  
        clock.tick(MAX_FPS)
        p.display.flip()

"""
Responsible for graphics within the game state    
"""
def DrawGameState(screen, game_state):

    DrawBoard(screen) #draw squares on the board
    # add in piece highlighting or move suggestions
    DrawPieces(screen, game_state.board) #draw pieces onto those squares
 
"""
Draw the squares on the board
"""    
def DrawBoard(screen):
    colors= [ p.Color('white'), p.Color('purple')]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row+col) % 2)]
            p.draw.rect(screen, color, p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))



"""
Draw the pieces on the board using the current game state
"""
def DrawPieces(screen, board):
     for row in range(DIMENSION):
         for col in range(DIMENSION):
             piece = board[row][col]
             if piece != "--": # if not empty square
                screen.blit(IMAGES[piece], p.Rect(col*SQ_SIZE, row*SQ_SIZE, SQ_SIZE, SQ_SIZE))



if __name__ == "__main__":
    main()
