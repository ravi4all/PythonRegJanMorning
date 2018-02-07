import pygame

pygame.init()

size = width,height = 800,500
# width = 800
# height = 500

black = 0,0,0
white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode((width,height))

x = 5
y = 5

move_x = 0
move_y = 0

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
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x = -3
                move_y = 0
            elif event.key == pygame.K_UP:
                move_y = -3
                move_x = 0
            elif event.key == pygame.K_DOWN:
                move_y = 3
                move_x = 0

    screen.fill(red)

    pygame.draw.rect(screen,black,[x,y,50,50])

    x += move_x
    y += move_y

    if x > width:
        x = -50
    elif x < -50:
        x = width
    elif y > height:
        y = -50
    elif y < -50 :
        y = height

    pygame.display.flip()
    clock.tick(FPS)