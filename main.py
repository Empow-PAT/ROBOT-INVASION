import pygame
import random
from towers import *
from hero import *
from drones import *
from robots import  *
from maps import *
from collectible import *

pygame.init()

windowwidth = 800
windowheight = 800

win = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption("Drone Tests")
deadgreen = (120, 150, 0)
white = (255,255,255)
red = (255,0,0)
for i in range(35):
    drone = Drone()
for i in range(20):
    dummy = Dummy()


robot = Normal()
robot2 = Speedy()
robot3 = Slow()
run = True
while run:
    pygame.time.delay(6)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:


            run = False

    keys = pygame.key.get_pressed()

    win.fill(deadgreen)
    for d in Drone.droneloc:
        d.tick(keys, win)
    for dummy in Dummy.enemyloc:
        dummy.tick(keys, win)
    for r in robots:
        r.tick(win)

    pygame.display.update()



















