import pygame, sys, random, math
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([126, 45, 125])
my_ball = pygame.image.load("D:\\Pylearn\\pygame\\beach_ball.png")
x = 50
y = 50
x_speed = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for looper in range(1, 100):
        screen.blit(my_ball, [x, y])
        pygame.time.delay(20)
        pygame.draw.rect(screen, [126, 45, 125], [x, y, 90, 90], 0)
        x = x + x_speed
        screen.blit(my_ball, [x, y])
        pygame.display.flip()
        if x > screen.get_width() - 90 or x < 0:
            x_speed = - x_speed
            screen.blit(my_ball, [x, y])
            pygame.display.flip()
pygame.quit()
