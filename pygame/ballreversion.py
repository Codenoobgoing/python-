import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([116, 209, 234])
my_ball = pygame.image.load("D:\\Pylearn\\pygame\\beach_ball.png")
x = 0
y = 0
x_speed = 5
y_speed = 5
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(my_ball, [x, y])
    pygame.time.delay(10)
    pygame.draw.rect(screen, [116, 209, 234], [x, y, 90, 90], 0)
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width():
        x = -90
    if y >screen.get_height():
        y = -90
    screen.blit(my_ball, [x, y])
    pygame.display.flip()
pygame.quit()




