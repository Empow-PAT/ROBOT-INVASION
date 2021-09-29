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
black = (0, 0, 0)
white = (255,255,255)

drone= Drone()
drone2 = Drone()
drone3 = Drone()
drone4 = Drone()
drone5 = Drone()
drone6 = Drone()
drone7 = Drone()
drone8 = Drone()
drone9= Drone()
drone10 = Drone()
drone11 = Drone()
drone12 = Drone()
drone13 = Drone()
drone14 = Drone()
drone15 = Drone()
drone16 = Drone()
drone17 = Drone()
drone18 = Drone()
drone19 = Drone()
drone20 = Drone()
drone21 = Drone()
drone22 = Drone()
drone23 = Drone()
drone24 = Drone()
drone25 = Drone()
drone26 = Drone()
drone27 = Drone()
drone28 = Drone()
drone29 = Drone()
drone30 = Drone()
drone31 = Drone()
drone32 = Drone()
drone33 = Drone()
drone34 = Drone()
drone35 = Drone()

run = True
while run:
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:


            run = False

    keys = pygame.key.get_pressed()

    win.fill(black)
    drone.tick(keys, win)
    drone2.tick(keys, win)
    drone3.tick(keys, win)
    drone4.tick(keys, win)
    drone5.tick(keys, win)
    drone6.tick(keys, win)
    drone7.tick(keys, win)
    drone8.tick(keys, win)
    drone9.tick(keys, win)
    drone10.tick(keys, win)
    drone11.tick(keys, win)
    drone12.tick(keys, win)
    drone13.tick(keys, win)
    drone14.tick(keys, win)
    drone15.tick(keys, win)
    drone16.tick(keys, win)
    drone17.tick(keys, win)
    drone18.tick(keys, win)
    drone19.tick(keys, win)
    drone20.tick(keys, win)
    drone21.tick(keys, win)
    drone22.tick(keys, win)
    drone23.tick(keys, win)
    drone24.tick(keys, win)
    drone25.tick(keys, win)
    drone26.tick(keys, win)
    drone27.tick(keys, win)
    drone28.tick(keys, win)
    drone29.tick(keys, win)
    drone30.tick(keys, win)
    drone31.tick(keys, win)
    drone32.tick(keys, win)
    drone33.tick(keys, win)
    drone34.tick(keys, win)
    drone35.tick(keys, win)
    pygame.display.update()



















