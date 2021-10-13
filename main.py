import pygame
import pygame_gui
import random
from towers import *
from hero import *
from drones import *
from robots import  *
from maps import *
from collectible import *
from EnemyFile import*

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
manager = pygame_gui.UIManager((800, 800))
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                            text='PLAY',
                                            manager=manager)
clock = pygame.time.Clock()
run = True
while run:
    time_delta = clock.tick(60) / 1000.0
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:


            run = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    print('[Insert Text Here]')
        manager.process_events(event)
    manager.update(time_delta)

    keys = pygame.key.get_pressed()

    win.fill(black)
    manager.draw_ui(win)
    win.fill(deadgreen)
    for d in Drone.droneloc:
        d.tick(keys, win)
    for dummy in Dummy.enemyloc:
        dummy.tick(keys, win)
    for r in robots:
        r.tick(win)

    pygame.display.update()



















