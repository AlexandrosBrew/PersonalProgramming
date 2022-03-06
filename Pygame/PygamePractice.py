import pygame as py
import os

cdir = os.getcwd()
FPS, WHITE, BLACK, WIDTH, HEIGHT, VEL = 60, (255, 255, 255), (0, 0, 0), 900, 500, 5
SS_WIDTH, SS_HEIGHT = 55, 40
YELLOW_SS_IMG = py.image.load(cdir + '/Pygame/Assets/spaceship_yellow.png')
YELLOW_SS_IMG = py.transform.scale(YELLOW_SS_IMG, (SS_WIDTH, SS_HEIGHT))
YELLOW_SS_IMG = py.transform.rotate(YELLOW_SS_IMG, -90)
RED_SS_IMG = py.image.load(cdir + '/Pygame/Assets/spaceship_red.png')
RED_SS_IMG = py.transform.scale(RED_SS_IMG, (SS_WIDTH, SS_HEIGHT))
RED_SS_IMG = py.transform.rotate(RED_SS_IMG, 90)

BORDER = py.Rect((WIDTH/2)-5, 0 , 10, HEIGHT)
WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Spaceships")


def draw_window(red, yellow):
    WIN.fill(WHITE)
    py.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SS_IMG, (yellow.x, yellow.y))
    WIN.blit(RED_SS_IMG, (red.x, red.y))
    py.display.update()

def r_move(keys_pressed, red):
    if keys_pressed[py.K_a]: red.x -= VEL #Left
    if keys_pressed[py.K_d]: red.x += VEL #Right
    if keys_pressed[py.K_w]: red.y -= VEL #Up
    if keys_pressed[py.K_s]: red.y += VEL #Down

def y_move(keys_pressed, yellow):
    if keys_pressed[py.K_LEFT] and yellow.x + VEL + yellow.width > BORDER.x: yellow.x -= VEL #Left
    if keys_pressed[py.K_RIGHT] and yellow.x - VEL > 0: yellow.x += VEL #Right
    if keys_pressed[py.K_UP] and yellow.y - VEL > 0: yellow.y -= VEL #Up
    if keys_pressed[py.K_DOWN] and yellow.y + VEL + yellow.height < HEIGHT: yellow.y += VEL #Down
    

def main():
    red = py.Rect(100, 300, SS_WIDTH, SS_HEIGHT)
    yellow = py.Rect(700, 300, SS_WIDTH, SS_HEIGHT)

    clock = py.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False

        keys_pressed = py.key.get_pressed()
        r_move(keys_pressed, red)
        y_move(keys_pressed, yellow)
        draw_window(red, yellow)

    py.quit()

if __name__=="__main__":
    main()