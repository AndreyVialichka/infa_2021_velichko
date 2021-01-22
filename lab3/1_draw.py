import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

N = 10
color = (255, 255, 0)
color1 = (255, 0, 0)
color2 =(0,0,0)

circle(screen, color, (200,200), 100)
circle(screen, color1, (150,180), 20)
circle(screen, color1, (250,180), 20)
circle(screen, color2, (150,180), 10)
circle(screen, color2, (250,180), 10)

line(screen, color2, (150, 250), (250, 250), width = 20)
line(screen, color2, (280, 140), (230, 170), width = 15)
line(screen, color2, (130, 150), (180, 180), width = 15)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()