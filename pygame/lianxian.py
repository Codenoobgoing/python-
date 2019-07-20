import pygame, sys
pygame.init()
dot = [[54,68],[35,6],[65,65],[35,58]]
screen = pygame.display.set_mode([640,480])
screen.fill([0,0,0])
pygame.draw.lines(screen,[0,255,255],True,dot,2)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()