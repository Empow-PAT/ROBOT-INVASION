import pygame
import random
from towers import *
from hero import *
from drones import *
from maps import *
from collectible import *

pygame.init()

windowwidth = 800
windowheight = 800

win = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption("Drone Tests")
black = (0, 191, 255)
white = (255,0,255)

for i in range(35):
    drone = Drone()
for i in range(20):
    dummy = Dummy()

run = True
while run:
    win = pygame.display.set_mode((windowwidth, windowheight))
    pygame.time.delay(6)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            run = False

    keys = pygame.key.get_pressed()

    win.fill(black)
    for d in Drone.droneloc:
        d.tick(keys, win)
    for dummy in Dummy.enemyloc:
        dummy.tick(keys, win)

    pygame.display.update()



















