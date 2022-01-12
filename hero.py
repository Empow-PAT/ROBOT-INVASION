import pygame
from maps import *

red = (255,0,0)

class Robot():
    robots = []
    def __init__(self,speed,color):
       self.distance = 0
       self.speed = speed
       self.color = color
       self.pathstep = 0
       self.x = path[0][self.pathstep]
       self.y = path[1][self.pathstep]
       Robot.robots.append(self)
       self.width = 100
       self.height = 100
       rect = pygame.Rect(self.x,self.y,60,60)
       self.image = pygame.image.load("Art\Robot Squirrel2.png")
       self.image = pygame.transform.scale(self.image, (self.width, self.height))
    def tick(self,win,keys):
        if self.pathstep < len(path[0]):
            if self.x == path[0][self.pathstep] and self.y == path[1][self.pathstep]:
                    self.pathstep +=1
                    print(self.pathstep)
                    print(self.x, self.y)
        elif self.x == path[0][self.pathstep-1] and self.y == path[1][self.pathstep-1]:
            print(self.pathstep)
            print(self.x, self.y)
            if self.pathstep > 0:
                self.pathstep += -1
        stepbefore = self.pathstep - 1
        if stepbefore < 0:
            stepbefore = 0
        if keys[pygame.K_w]:
            if self.pathstep < len(path[0]):
                if self.x < path[0][self.pathstep]:
                    self.x += self.speed
                if self.x > path[0][self.pathstep]:
                    self.x += -self.speed
                if self.y < path[1][self.pathstep]:
                    self.y += self.speed
                if self.y > path[1][self.pathstep]:
                    self.y += -self.speed
        if keys[pygame.K_s]:
            if self.x < path[0][stepbefore]:
                self.x += self.speed
            if self.x > path[0][stepbefore]:
                self.x += -self.speed
            if self.y < path[1][stepbefore]:
                self.y += self.speed
            if self.y > path[1][stepbefore]:
                self.y += -self.speed
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        win.blit(self.image, (self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

class BlazeBot(Robot):
    def __init__(self):
        Robot.__init__(self,4,red)