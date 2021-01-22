import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
bg_color = (230, 230, 230)
screen.fill(bg_color)

N = 10
white = (255, 255, 255)
red = (255, 0, 0)
black =(0, 0, 0)
green = (9, 148, 65)
brown = (101, 67, 33)
blue = (0, 0, 176)
yellow = (255,204,0)
sky_blue = (63, 79, 232)
tree_green = (144, 245, 0)
# sky
rect(screen, sky_blue, (0,0,400,200))
# house
rect(screen, green, (0,200,400,200))
rect(screen, brown, (40,160,120,120))
rect(screen, blue, (80,200,40,40))
# grass
polygon(screen, red, [(40,160),(100,80),(160,160)])
# sun
circle(screen, yellow, (340,60), 30)
# tree
line(screen, black, (280, 160), (280, 250), width = 15)
circle(screen, tree_green, (260,140), 15)
circle(screen, tree_green, (270,130), 15)
circle(screen, tree_green, (280,150), 15)
circle(screen, tree_green, (290,160), 15)
circle(screen, tree_green, (300,120), 15)
circle(screen, tree_green, (305,150), 15)
# cloud
circle(screen, white, (160,80), 20)
circle(screen, white, (175,80), 20)
circle(screen, white, (190,80), 20)
circle(screen, white, (205,80), 20)
circle(screen, white, (175,70), 30)
circle(screen, white, (185,70), 30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()