import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
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
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width() - 90 or x < 0:
        x_speed = - x_speed
    if y > screen.get_height() - 90 or y < 0:
        y_speed = - y_speed
    screen.blit(my_ball, [x, y])
    pygame.display.flip()
pygame.quit()
