import pygame
import random

pygame.init()

width = 1060
height = 600

black = 0,0,0
white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode((width,height))

backgroundImage = pygame.image.load('assets/images/background.png')
tank = pygame.image.load('assets/images/tank_1.png')

ufo_1 = pygame.image.load('assets/images/ufo_1.png')
ufo_2 = pygame.image.load('assets/images/ufo_2.png')
ufo_3 = pygame.image.load('assets/images/ufo_3.png')

ufo_x1 = width
ufo_x2 = -220
ufo_x3 = width/2 - 105

ufo_y1 = 100
ufo_y2 = 250
ufo_y3 = -200

ufo_move_x1 = random.randint(2,6)
ufo_move_x2 = random.randint(2,6)
ufo_move_y = 4

x = width/2 - 74
y = height - 140

move_x = 0

clock = pygame.time.Clock()
FPS = 100

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 3
            elif event.key == pygame.K_LEFT:
                move_x = -3
        elif event.type == pygame.KEYUP:
            move_x = 0

    screen.fill(white)
    screen.blit(backgroundImage, (0,0))
    screen.blit(tank, (x,y))
    screen.blit(ufo_1, (ufo_x1, ufo_y1))
    screen.blit(ufo_2, (ufo_x2, ufo_y2))
    screen.blit(ufo_3, (ufo_x3, ufo_y3))

    x += move_x

    ufo_x1 -= ufo_move_x1
    ufo_x2 += ufo_move_x2

    if ufo_x1 < -212:
        ufo_move_x1 = random.randint(2, 6)
        ufo_x1 = width
    elif ufo_x2 > width:
        ufo_move_x2 = random.randint(2, 6)
        ufo_x2 = -220

    pygame.display.flip()
    clock.tick(FPS)