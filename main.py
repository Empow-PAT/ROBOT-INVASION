import pygame
import random

pygame.init()

windowwidth = 800
windowheight = 800
win = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption("Drone Tests")
black = (0, 0, 0)
white = (255,255,255)

class Drone:
    droneloc = []
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.xgoal = 0
        self.ygoal = 0
        Drone.droneloc.append(self)
    def tick(self):
        for d in Drone.droneloc:
            if d != self and d.rect.colliderect(self.rect):
                xory = random.randint(0,3)
                if xory == 1:
                    self.x = d.xgoal + d.width + 5
                    self.xgoal = d.xgoal + d.width + 5
                if xory == 0:
                    self.y = d.ygoal + d.height + 5
                    self.ygoal = d.ygoal + d.height + 5
                if xory == 2:
                    self.x = d.xgoal - d.width - 5
                    self.xgoal = d.xgoal - d.width - 5
                if xory == 3:
                    self.y = d.ygoal - d.height - 5
                    self.ygoal = d.ygoal - d.height - 5
        if keys[pygame.K_e] == True:
            Mx,My = pygame.mouse.get_pos()
            Mx += -10
            My += -10
            self.xgoal,self.ygoal = Mx,My

        if self.x < self.xgoal:
            self.x += 5
        if self.x > self.xgoal:
            self.x += -5
        if self.y < self.ygoal:
            self.y += 5
        if self.y > self.ygoal:
            self.y += -5

        if self.x > windowwidth - self.width:
            self.x = windowwidth - self.width
        if self.x < 0:
            self.x = 0
        if self.y > windowwidth - self.height:
            self.y = windowwidth - self.height
        if self.y < 0:
            self.y = 0

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, white, self.rect)


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
    drone.tick()
    drone2.tick()
    drone3.tick()
    drone4.tick()
    drone5.tick()
    drone6.tick()
    drone7.tick()
    drone8.tick()
    drone9.tick()
    drone10.tick()
    drone11.tick()
    drone12.tick()
    drone13.tick()
    drone14.tick()
    drone15.tick()
    drone16.tick()
    drone17.tick()
    drone18.tick()
    drone19.tick()
    drone20.tick()
    drone21.tick()
    drone22.tick()
    drone23.tick()
    drone24.tick()
    drone25.tick()
    drone26.tick()
    drone27.tick()
    drone28.tick()
    drone29.tick()
    drone30.tick()
    drone31.tick()
    drone32.tick()
    drone33.tick()
    drone34.tick()
    drone35.tick()
    pygame.display.update()



















