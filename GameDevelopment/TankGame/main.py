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
bulletImage = pygame.image.load("assets/images/bullet_1.png")

ufo_1 = pygame.image.load('assets/images/ufo_1.png')
ufo_2 = pygame.image.load('assets/images/ufo_2.png')
ufo_3 = pygame.image.load('assets/images/ufo_3.png')

clock = pygame.time.Clock()
FPS = 100

def homeScreen():
    font = pygame.font.SysFont(None, 50)
    welcometext = font.render("Welcome to Tank Game", True, red)
    starttext = font.render("Press SPACE to Start Game", True, red)
    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.fill(white)
        screen.blit(welcometext, (230,100))
        screen.blit(starttext, (200, 200))
        pygame.display.update()


def fire(bullet_pos, bulletImage):
    for i in range(len(bullet_pos)):
        bullet_pos[i]['y'] -= 10
        screen.blit(bulletImage, [bullet_pos[i]['x'], bullet_pos[i]['y']])
        # print(bullet_pos[i]['x'], bullet_pos[i]['y'])
        # print(bullet_pos[i]['y'])

def score(counter):
    font = pygame.font.SysFont(None,40)
    text = font.render('Score : '+str(counter),True,red)
    screen.blit(text, (10,10))

def game():
    bullet_fired = -10

    ufo_x1 = width
    ufo_x2 = -220
    ufo_x3 = width / 2 - 105

    ufo_y1 = 100
    ufo_y2 = 250
    ufo_y3 = -200

    ufo_move_x1 = random.randint(2, 6)
    ufo_move_x2 = random.randint(2, 6)
    ufo_move_y = 4

    tank_x = width / 2 - 74
    tank_y = height - 140

    counter = 0

    bullet_list = []
    bullet_dict = {'x' : tank_x + 70, 'y' : tank_y - 20}
    bullet_list.append(bullet_dict)

    bullet_x = -100
    bullet_y = -100

    move_x = 0

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
                elif event.key == pygame.K_SPACE:
                    # if temp:
                    #     screen.blit(bulletImage, (bullet_x, bullet_y))
                    bullet_x = tank_x + 70
                    bullet_y = tank_y - 20
                    bullet_fired = -10
                    bullet_dict['x'] = bullet_x
                    bullet_dict['y'] = bullet_y
                    bullet_list.append(bullet_dict.copy())
                    # print(bulletList)

            elif event.type == pygame.KEYUP:
                move_x = 0

        screen.fill(white)
        screen.blit(backgroundImage, (0,0))
        screen.blit(tank, (tank_x,tank_y))
        screen.blit(ufo_1, (ufo_x1, ufo_y1))
        screen.blit(ufo_2, (ufo_x2, ufo_y2))
        screen.blit(ufo_3, (ufo_x3, ufo_y3))
        # screen.blit(bulletImage, (bullet_x, bullet_y))

        tank_x += move_x

        ufo_x1 -= ufo_move_x1
        ufo_x2 += ufo_move_x2

        # bullet_y += bullet_fired

        fire(bullet_list, bulletImage)

        if ufo_x1 < -212:
            ufo_move_x1 = random.randint(2, 6)
            ufo_x1 = width
        elif ufo_x2 > width:
            ufo_move_x2 = random.randint(2, 6)
            ufo_x2 = -220

        # print(bullet_list[0])
        bulletRect = pygame.Rect(bullet_list[0]['x'], bullet_list[0]['y'], bulletImage.get_width(), bulletImage.get_height())
        ufo_rect_1 = pygame.Rect(ufo_x1, ufo_y1, ufo_1.get_width(), ufo_1.get_height())
        ufo_rect_2 = pygame.Rect(ufo_x2, ufo_y2, ufo_2.get_width(), ufo_2.get_height())

        if bulletRect.colliderect(ufo_rect_1):
            ufo_x1 = width
            ufo_y1 = 100
            bullet_y = 0
            counter += 1
            # bullet_x = tank_x + 70
            # bullet_y = tank_y - 20
        elif bulletRect.colliderect(ufo_rect_2):
            ufo_x2 = -220
            ufo_y2 = 250
            bullet_y = 0
            counter += 1
            # bullet_x = tank_x + 70
            # bullet_y = tank_y - 20

        score(counter)

        pygame.display.flip()
        clock.tick(FPS)

# game()
homeScreen()