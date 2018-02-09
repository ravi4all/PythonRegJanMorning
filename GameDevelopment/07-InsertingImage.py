import pygame

pygame.init()

width = 800
height = 500

black = 0,0,0
white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode((width,height))

ball = pygame.image.load('ball.jpg')
ball = pygame.transform.scale(ball,(150,150))

x = 50
y = 50

move_x = 5
move_y = 5

clock = pygame.time.Clock()
FPS = 100

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    screen.blit(ball,[x,y])

    x += move_x
    y += move_y

    if x > width - 225 or x < 0:
        move_x = -move_x
    elif y > height - 225 or y < 0:
        move_y = -move_y

    pygame.display.flip()
    clock.tick(FPS)