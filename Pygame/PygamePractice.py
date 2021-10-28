import pygame as py
import os

FPS, WHITE, WIDTH, HEIGHT = 60, (255, 255, 255), 900, 500
YELLOW_SS_IMG = py.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SS_IMG = py.image.load(os.path.join('Assets', 'spaceship_red.png')) 
WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Spaceships")


def draw_window():
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SS_IMG, (675, 375))
    WIN.blit(RED_SS_IMG, (225, 125))
    py.display.update()

def main():
    clock = py.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        draw_window()

    py.quit()

if __name__=="__main__":
    main()