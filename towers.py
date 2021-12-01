import pygame
import math
from robots import *
import random
windowwidth = 800
windowheight = 800
win = pygame.display.set_mode((windowwidth, windowheight))
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
yellow = (255, 255, 0)


class ShootingTower:
        towers = []
        def __init__(self, x, y):
                self.x = x
                self.y = y
                self.health = 400
                self.width = 100
                self.height = 100
                self.image = pygame.image.load( "Art/TowerPlaceHolder.png")
                self.rect = pygame.Rect( self.x, self.y, self.width, self.height )
                ShootingTower.towers.append(self)
        def tick(self, keys, win):


                self.image = pygame.transform.scale ( self.image, (self.width, self.height) )
                win.blit ( self.image, (self.x - self.width/2, self.y - self.height/2) )
                self.rect = pygame.Rect ( self.x, self.y, self.width, self.height )

class EnemyBuilderDrone:
        eDrones = []
        def __init__(self,x,y):
                self.x = x
                self.y = y
                self.xgoal = random.randint(100,700)
                self.ygoal = random.randint(100,700)
                self.health = 5
                self.width = 10
                self.height = 10
                # self.image = pygame.image.load( "Art/TowerPlaceHolder.png")
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                EnemyBuilderDrone.eDrones.append(self)

        def tick(self, keys, win):

                if self.x < self.xgoal:
                        self.x += 1
                if self.x > self.xgoal:
                        self.x -= 1
                if self.y < self.ygoal:
                        self.y += 1
                if self.y > self.ygoal:
                        self.y -= 1

                if self.y == self.ygoal and self.x == self.xgoal:
                        shootingtower = ShootingTower(self.x,self.y)
                        EnemyBuilderDrone.eDrones.remove(self)
                        return
                if self.health <= 0:
                        EnemyBuilderDrone.eDrones.remove(self)
                # self.image = pygame.transform.scale( self.image, (self.width, self.height))
                # win.blit(self.image, (self.x, self.y))
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                pygame.draw.rect(win, red, self.rect)

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
        self.width = 25
        self.height = 25
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.image.load("Art/Turret.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
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
        win.blit(self.image, (self.x, self.y))




class BuilderTower:
        def __init__(self):
                self.x = 400
                self.y = 400
                self.health = 400
                self.width = 50
                self.height = 50
                self.buildspawn = 0
                #self.image = pygame.image.load( "Art/TowerPlaceHolder.png")
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                ShootingTower.towers.append(self)
        def tick(self, keys, win):

                self.buildspawn += 1
                if self.buildspawn >= 100:
                        self.buildspawn = 0
                        builder = EnemyBuilderDrone(self.x, self.y)

                #self.image = pygame.transform.scale( self.image, (self.width, self.height))
                #win.blit(self.image, (self.x, self.y))
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                pygame.draw.rect(win, blue, self.rect)