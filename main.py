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
import time
from pygame.locals import *

pygame.init()

windowwidth = 800
windowheight = 800
Background = pygame.image.load("Art/Robot Invasion Title.jpg").convert_alpha()
bglevel = pygame.image.load("Art/BackgroundPicture.png").convert_alpha()



win = pygame.display.set_mode((windowwidth, windowheight), DOUBLEBUF)
pygame.display.set_caption("Robot Invasion")
black = (0, 0, 0)
deadgreen = (120, 150, 0)
white = (255,255,255)
gray = (40, 40,40)
red = (255,0,0)
def HowToPlay():
    run3 = True
    manager3 = pygame_gui.UIManager((800, 800), 'gui_theme.json')



    BackButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20,20), (90, 50)),
                                                  text='',
                                                  object_id="back_button",
                                                  manager=manager3)
    while run3:
        time_delta = clock.tick(60) / 1000.0

        pygame.time.delay(6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run3 = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == BackButton:
                        run3 = False
            manager3.process_events(event)
        manager3.update(time_delta)
        win.blit(pygame.image.load("Art/MenuBackground.jpg"), (0,0))
        manager3.draw_ui(win)
        pygame.display.update()

def Store():
    run4 = True
    manager4 = pygame_gui.UIManager((800, 800), 'gui_theme.json')

    BackButton = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((20, 20), (90, 50)),
                                              text='',
                                              object_id="back_button",
                                              manager=manager4)
    DroneButton1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((120,75), (90, 50)),
                                              text='',
                                              object_id="drone_button1",
                                              manager=manager4)

    while run4:
        time_delta = clock.tick(60) / 1000.0

        pygame.time.delay(6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run4 = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == BackButton:
                        run4 = False
                    if event.ui_element == DroneButton1:
                        for drone in Drone.droneloc:

                            drone.change_skin()
            manager4.process_events(event)
        manager4.update(time_delta)
        win.fill(gray)
        manager4.draw_ui(win)
        pygame.display.update()
def Play():
    global run2
    manager2 = pygame_gui.UIManager((800, 800), 'gui_theme.json')
    moneytime = 0
    robotTime = 0
    # WAVESTUFF
    waveQueue = []
    wave = 0
    money = 10
    hero = BlazeBot()
    for i in range(35):
        drone = Drone()
    for i in range(0):
        enemy = Enemy_tower()
    ST = Tower(1,1000,13,333,333,win)
    # ROBOTBUYBUTTONS
    normal = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 750), (100, 50)),
                                          text='Normal: $5',
                                          manager=manager2)
    speedy = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 750), (100, 50)),
                                          text='Speedy: $10',
                                          manager=manager2)
    slow = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 750), (100, 50)),
                                          text='Slow: $50',
                                          manager=manager2)
    slowBoss = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 750), (100, 50)),
                                        text='Slow Boss: $1000',
                                        manager=manager2)
    deathGuard = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((400, 750), (100, 50)),
                                            text='Death Guard: $100000',
                                            manager=manager2)
    deathKing = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((500, 750), (100, 50)),
                                              text='Death Guard: $1000000',
                                              manager=manager2)
    waveStart = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((600, 750), (100, 50)),
                                             text='Start Wave!',
                                             manager=manager2)

    spawnStart = False
    run = True
    while run:
        time_delta = clock.tick(30) / 1000.0

        #pygame.time.delay(6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                run2 = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:

                    if event.ui_element == normal:
                        if money >= 5:
                            waveQueue.append("Normal")
                            money -= 5
                    if event.ui_element == speedy:
                        if money >= 10:
                            waveQueue.append("Speedy")
                            money -= 10
                    if event.ui_element == slow:
                        if money >= 50:
                            waveQueue.append("Slow")
                            money -= 50
                    if event.ui_element == slowBoss:
                        if money >= 1000:
                            waveQueue.append("SlowBoss")
                            money -= 1000
                    if event.ui_element == deathGuard:
                        if money >= 100000:
                            waveQueue.append("DeathGuard")
                            money -= 100000
                    if event.ui_element == waveStart:
                        if len(Robot.robots) == 0:
                            spawnStart = True
                            wave += 1




            manager2.process_events(event)
        manager2.update(time_delta)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_h] == True:
            Drone.droneloc = []
            for i in range ( 35 ):
                drone = Drone ()

        win.blit(bglevel, (0, 0))

        if spawnStart:
            for r in waveQueue:
                if robotTime>10:
                    robotTime = 0
                    spawnRobot(r)
                    waveQueue.remove(r)
            if len(waveQueue) == 0:
                spawnStart = False

        for d in Drone.droneloc:
            d.tick(keys, win)
        for shoot in ShootingTower.enemyloc:
            shoot.tick(keys, win)
        for r in Robot.robots:
            r.tick(win)
        for f in TowerFire.towerFire:
            f.tick()
        for t in Tower.towers:
            t.tick()
        hero.tick(win,keys)
        moneytime += 1
        robotTime += 1
        if moneytime == 40:
            moneytime = 0
            for r in Robot.robots:
                money += r.moneyGive
        moneyText = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((650, 0), (150, 50)),
                                                text="$ " + str(money),
                                                manager=manager2)
        waveText = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((100, 0), (150, 50)),
                                                text="Wave: " + str(wave),
                                                manager=manager2)
        manager2.draw_ui(win)
        pygame.display.update()


manager = pygame_gui.UIManager((800, 800), 'gui_theme.json')
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 210), (120, 75)),
                                           text='',
                                           object_id="mainplay",
                                           manager=manager)
how_to_play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 310), (120, 75)),
                                           text='',
                                           object_id="HowToPlay",
                                           manager=manager)
store_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 410), (120, 75)),
                                           text='',
                                           object_id="Store_Button",
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
                    Play()
                if event.ui_element == how_to_play_button:
                    HowToPlay()
                if event.ui_element ==store_button:
                    Store()
        manager.process_events(event)
    manager.update(time_delta)

    keys = pygame.key.get_pressed()

    win.fill(black)
    win.blit(Background,(0,0))
    manager.draw_ui(win)

    pygame.display.update()
