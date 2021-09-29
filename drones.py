import pygame
import random

windowwidth = 800
windowheight = 800
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
    def tick(self, keys, win):
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