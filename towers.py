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







class ShootingTower:
    towers = []
    def __init__(self,damage,range,reloadTime,x,y):
        self.dame = damage
        self.range = range
        self.reloadTime = reloadTime
        self.x = x
        self.y = y
        self.closest = None
        self.timer = 0
    def findRobot(self):
        self.closest = None
        closest = False
        for robot in Robot.robots:
            dist = math.hypot(robot.x - self.x, robot.y - self.y)
            if dist < self.range:
                closest = robot

        dx, dy = closest.x - self.x, closest.y - self.y
        angle = math.degrees(math.atan2(-dy, dx))
    def tick(self):
        self.timer += 1
        self.findRobot()
        if self.timer >= self.reloadTime:
            newFire = TowerFire()
            self.timer = 0


