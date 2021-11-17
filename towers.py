import pygame
import math
from robots import *
windowwidth = 800
windowheight = 800
win = pygame.display.set_mode((windowwidth, windowheight))
yellow = (255, 255, 0)


class TowerFire():
    towerFire = []
    def __init__(self,endPosition,startPosition,win):
        self.endPosition = endPosition
        self.startPosition = startPosition
        self.win = win
        self.counter = 0
        TowerFire.towerFire.append(self)


    def tick(self):
        pygame.draw.line(win, yellow,self.startPosition, self.endPosition, 3)
        self.counter += 1
        if self.counter >= 2:
            TowerFire.towerFire.remove(self)
            del self







class Tower():
    towers = []
    def __init__(self,damage,range,reloadTime,x,y,win):
        self.damage = damage
        self.range = range
        self.reloadTime = reloadTime
        self.x = x
        self.y = y
        self.closest = False
        self.timer = 0
        self.win = win
        Tower.towers.append(self)
    def findRobot(self):
        self.closest = False
        for robot in Robot.robots:
            dist = abs(robot.x - self.x)+abs(robot.y - self.y)
            if dist < self.range:
                self.closest = robot

    def tick(self):
        self.timer += 1
        self.findRobot()
        if self.timer >= self.reloadTime:
            if not self.closest == False:
                newFire = TowerFire((self.closest.x,self.closest.y),(self.x,self.y),win)
                self.closest.health -= self.damage
                self.timer = 0


