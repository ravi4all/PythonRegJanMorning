import pygame

pygame.init()

size = width,height = 800,500
# width = 800
# height = 500

black = 0,0,0
white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode((width,height))

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

    screen.fill(red)

    pygame.draw.circle(screen,black,[x,y],50)

    x += move_x
    y += move_y

    if x > width - 50 or x < 50:
        move_x = -move_x
    elif y > height - 50 or y < 50:
        move_y = -move_y

    pygame.display.flip()
    clock.tick(FPS)