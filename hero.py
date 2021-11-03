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
    def draw(self,win):
        rect = pygame.Rect(self.x,self.y,60,60)
        pygame.draw.rect(win,self.color ,rect)
    def tick(self,win,keys):
        if self.x == path[0][self.pathstep] and self.y == path[1][self.pathstep]:
            if self.pathstep < len(path[0]):
                self.pathstep +=1
        elif self.x == path[0][self.pathstep-1] and self.y == path[1][self.pathstep-1]:
            if self.pathstep > 0:
                self.pathstep += -1
        stepbefore = self.pathstep - 1
        if stepbefore < 0:
            stepbefore = 0
        if keys[pygame.K_w]:
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

        self.draw(win)

class BlazeBot(Robot):
    def __init__(self):
        Robot.__init__(self,4,red)
