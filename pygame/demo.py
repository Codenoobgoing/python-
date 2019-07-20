import pygame, sys, random
from pygame.color import THECOLORS
pygame.init()
screen = pygame.display.set_mode([1920, 1080])
screen.fill([255, 255, 255])
for i in range(100):
    width = random.randint(0, 250)
    height = random.randint(0,100)
    top = random.randint(0, 700)
    left = random.randint(0, 1620)
    color_name = random.choice(list(THECOLORS.keys()))
    color = THECOLORS[color_name]
    line_width = random.randint(1,3)
    pygame.draw.rect(screen, color, [left, top, width, height], line_width)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()