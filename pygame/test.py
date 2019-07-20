import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 200])
pygame.draw.circle(screen, [0, 255, 0], [320, 240], 30, 0)
pygame.draw.rect(screen,[255, 0,0],[320, 240, 100, 200],0)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()