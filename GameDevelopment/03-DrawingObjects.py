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

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill(red)

    pygame.draw.rect(screen,black,[x,10,50,50])

    x += 0.5

    pygame.display.flip()