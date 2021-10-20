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
Background = pygame.image.load("Art/Robot Invasion Title.jpg")
moneytime = 0

win = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption("Robot Invasion")
black = (0, 0, 0)
white = (255,255,255)
red = (255,0,0)
def Play():
    for i in range(35):
        drone = Drone()
    for i in range(20):
        dummy = Dummy()
    for i in range(1):
        enemy = Enemy_tower()


    robot = Normal()
    robot2 = Speedy()
    robot3 = Slow()
    # ROBOTBUYBUTTONS
    normal = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 750), (100, 50)),
                                          text='Normal: $5',
                                          manager=manager)
    speedy = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 750), (100, 50)),
                                          run = True
    while run:

        pygame.time.delay(6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                    if event.ui_element == normal:
                        if money >= 5:
                            Normal()
                            money -= 5
                    if event.ui_element == speedy:
                        if money >= 10:
                            Speedy()
                            money -= 10
            manager.process_events(event)

        keys = pygame.key.get_pressed()

        win.fill(black)
        for d in Drone.droneloc:
            d.tick(keys, win)
        for dummy in Dummy.enemyloc:
            dummy.tick(keys, win)
        for r in Robot.robots:
            r.tick(win)
        moneytime += 1
        if moneytime == 40:
            moneytime = 0
            for r in robots:
                money += r.moneyGive
        moneyText = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((650, 0), (150, 50)),
                                                    text="$ " + str(money),
                                                    manager=manager)
        pygame.display.update()
image_surface = pygame.image.load("Art\PlayButton.jpg"),
manager = pygame_gui.UIManager((800, 800))
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                            text='PLAY',
                                            manager=manager)
clock = pygame.time.Clock()

run2 = True
while run2:
    time_delta = clock.tick(60) / 1000.0
    pygame.time.delay(25)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:


            run2 = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == play_button:
                    print('[Insert Text Here]')
                    Play()
        manager.process_events(event)
    manager.update(time_delta)

    keys = pygame.key.get_pressed()

    win.fill(black)
    win.blit(Background,(0,0))
    manager.draw_ui(win)


    pygame.display.update()

