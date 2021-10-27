import pygame
import pygame_gui
import random
from towers import *
from hero import *
from drones import *
from robots import *
from maps import *
from collectible import *
from EnemyFile import*

pygame.init()

windowwidth = 800
windowheight = 800
Background = pygame.image.load("Art/Robot Invasion Title.jpg")

win = pygame.display.set_mode((windowwidth, windowheight))
boss = False
game_virus = False
pygame.display.set_caption("Robot Invasion")
black = (0, 0, 0)
deadgreen = (120, 150, 0)
white = (255,255,255)
red = (255,0,0)


def Play():
    bosscount = 0
    windowwidth = 800
    windowheight = 800
    manager2 = pygame_gui.UIManager((800, 800), 'gui_theme.json')
    moneytime = 0
    money = 40
    for i in range(1):
        shootingtower = ShootingTower(random.randint(100,700),random.randint(100,700))
        buildertower = BuilderTower()
    for i in range(35):
        drone = Drone()
    for i in range(0):
        enemy = Enemy_tower()

    robot = Normal()
    robot2 = Speedy()
    robot3 = Slow()
    # ROBOTBUYBUTTONS
    normal = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 750), (100, 50)),
                                          text='Normal: $5',
                                          manager=manager2)
    speedy = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 750), (100, 50)),
                                          text='Speedy: $10',
                                          manager=manager2)
    run = True
    while run:
        win = pygame.display.set_mode((windowwidth, windowheight))

        time_delta = clock.tick(60) / 1000.0

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
            manager2.process_events(event)
        manager2.update(time_delta)
        keys = pygame.key.get_pressed()

        win.fill(deadgreen)
        for e in ShootingTower.towers:
            e.tick(keys, win)
        for b in EnemyBuilderDrone.eDrones:
            b.tick(keys, win)
        for enemy in Dummy.enemyloc:
            enemy.tick(keys, win)
        for d in Drone.droneloc:
            d.tick(keys, win, EnemyBuilderDrone)
        for r in Robot.robots:
            r.tick(win)
        if boss == True and bosscount == 0:
            glitch = Glitch()
            bosscount = len(Glitch.boss)
        if boss == True:
            for b in Glitch.boss:
                if game_virus == True:
                    glitch = Glitch()
                b.tick(win)
                windowwidth = b.addw
                windowheight = b.addh
                pygame.display.update()

        moneytime += 1
        if moneytime == 40:
            moneytime = 0
            for r in Robot.robots:
                money += r.moneyGive
        moneyText = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((650, 0), (150, 50)),
                                                text="$ " + str(money),
                                                manager=manager2)
        manager2.draw_ui(win)
        pygame.display.update()


manager = pygame_gui.UIManager((800, 800), 'gui_theme.json')
play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                           text='',
                                           object_id="mainplay",
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
        manager.process_events(event)
    manager.update(time_delta)

    keys = pygame.key.get_pressed()
    win.fill(black)
    win.blit(Background,(0,0))
    manager.draw_ui(win)

    pygame.display.update()



















