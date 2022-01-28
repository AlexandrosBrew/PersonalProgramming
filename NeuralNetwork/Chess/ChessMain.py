from logging.handlers import QueueListener
import pygame as py
from pygame.image import load
import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}
WHITE = [255, 255, 255]
LIGHT_GRAY = [211, 211, 211]
GRAY = [128, 128, 128]
def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wK", "wQ", "bp", "bR", "bN", "bB", "bK", "bQ"]
    for piece in pieces:
        print("/Users/alexandrosbrew/Documents/PersonalProgramming/NeuralNetwork/Chess/ChessPieces/" + piece + ".png")
        IMAGES[piece] = py.image.load("/Users/alexandrosbrew/Documents/PersonalProgramming/NeuralNetwork/Chess/ChessPieces/" + piece + ".png", str((SQ_SIZE, SQ_SIZE)))
    
def main():
    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))
    clock = py.time.Clock()
    screen.fill(WHITE)
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    sqSelected = ()
    playerClicks = []  

    while running:
        for event in py.event.get():
            if event.type == py.QUIT or event.type == py.KEYDOWN:
                if event.key == py.K_q:
                    running = False
            elif event.type == py.MOUSEBUTTONDOWN:
                location = py.mouse.get_pos()
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    gs.makeMove(move)
                    sqSelected, playerClicks = (), []
            elif event.type == py.KEYDOWN:
                if event.key == py.K_u:
                    gs.undoMove()


        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        py.display.flip()

def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

def drawBoard(screen):
    colours = [LIGHT_GRAY, GRAY]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colours[((r+c)%2)]
            py.draw.rect(screen, color, py.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], py.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


if __name__ == "__main__":
    main()