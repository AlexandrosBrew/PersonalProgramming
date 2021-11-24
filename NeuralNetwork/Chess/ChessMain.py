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

    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
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