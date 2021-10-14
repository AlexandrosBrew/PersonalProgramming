import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(500):
        screen.fill((255, 255, 255))
        if i != 500:
            pygame.draw.circle(screen, (0, 0, 255), (250, i), 75)
        else:
            break
        running = False
        pygame.display.flip()

pygame.quit()
