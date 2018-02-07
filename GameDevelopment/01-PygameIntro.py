import pygame

pygame.init()

width = 800
height = 500

black = 0,0,0
white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode((width,height))

screen.fill(red)

pygame.display.flip()