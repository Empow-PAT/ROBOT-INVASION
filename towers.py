import pygame
import math
from robots import *
import random
from drones import *
windowwidth = 800
windowheight = 800
win = pygame.display.set_mode((windowwidth, windowheight))
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)
grey = (134,134,134)
yellow = (255, 255, 0)


class ShootingTower:
        towers = []
        def __init__(self, x, y):
                self.x = x
                self.y = y
                self.health = 400
                self.width = 100
                self.futurex = 0
                self.futurey = 0
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
        def __init__(self,x,y,toSpawn):
                self.x = x
                self.y = y
                self.pathchoice = random.randint(1,3)
                if self.pathchoice == 1:
                    self.ygoal = random.randint(200,325)
                    self.xgoal = random.randint(0,450)
                if self.pathchoice == 2:
                    self.ygoal = random.randint(0, 800)
                    self.xgoal = random.randint(600, 700)
                if self.pathchoice == 3:
                    self.ygoal = random.randint(400, 800)
                    self.xgoal = random.randint(300, 450)
                self.health = 5
                self.tower = toSpawn
                self.futurex = 0
                self.futurey = 0
                self.width = 10
                self.height = 10
                self.yvel = 0
                self.xvel = 0
                if self.x < self.xgoal:
                        self.xvel = 1
                if self.x > self.xgoal:
                        self.xvel = -1
                if self.y < self.ygoal:
                        self.yvel = 1
                if self.y > self.ygoal:
                        self.yvel = -1
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

                self.futurex = self.xvel * 50
                self.futurey = self.yvel * 50

                if self.y == self.ygoal and self.x == self.xgoal:
                        if self.tower == Tower:
                            shootingtower = self.tower(1,100,10,self.x,self.y,win)
                            EnemyBuilderDrone.eDrones.remove(self)
                            return
                        else:
                            spawnedTower = self.tower(self.x,self.y)
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
            return

class AATowerFire():
    AAtowerFire = []
    def __init__(self,endPosition,startPosition,win):
        self.endPosition = endPosition
        self.startPosition = startPosition
        self.win = win
        self.counter = 0
        AATowerFire.AAtowerFire.append(self)


    def tick(self):
        pygame.draw.line(win, green,self.startPosition, self.endPosition, 3)
        self.counter += 1
        if self.counter >= 2:
            AATowerFire.AAtowerFire.remove(self)
            return

class Tower():
    towers = []
    def __init__(self,damage,range,reloadTime,x,y,win):
        self.damage = damage
        self.range = range
        self.reloadTime = reloadTime
        self.x = x
        self.y = y
        #adding a futurex so Gabe's new boss code does not break
        #this should be added differently
        self.futurex = 0
        self.futurey = 0

        self.closest = False
        self.timer = 0
        self.win = win
        self.health = 30
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
                newFire = TowerFire((self.closest.x + self.closest.width/2,self.closest.y + self.closest.height/2),(self.x + self.width/2,self.y + self.height/2),win)
                self.closest.health -= self.damage
                self.timer = 0

        if self.health <= 0:
            Tower.towers.remove(self)
            return


        win.blit(self.image, (self.x, self.y))


class AntiDroneTower():
    AAtowers = []
    def __init__(self,damage,range,reloadTime,x,y,win):
        self.damage = damage
        self.range = range
        self.reloadTime = reloadTime
        self.x = x
        self.y = y
        self.futurex = 0
        self.futurey = 0
        self.closest = False
        self.timer = 0
        self.color = mint_green
        self.win = win
        self.health = 20
        AntiDroneTower.AAtowers.append(self)
        self.width = 10
        self.height = 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #self.image = pygame.image.load("Art/Turret.png").convert_alpha()
        #self.image = pygame.transform.scale(self.image, (self.width, self.height))
    def findRobot(self):
        self.closest = False
        for d in Drone.droneloc:
            dist = abs(d.x - self.x)+abs(d.y - self.y)
            if dist < self.range:
                self.closest = d

    def tick(self):
        self.timer += 1
        self.findRobot()
        if self.timer >= self.reloadTime:
            if not self.closest == False:

                newFire = AATowerFire((self.closest.x + self.closest.width/2,self.closest.y + self.closest.height/2),(self.x + self.width/2,self.y + self.height/2),win)
                self.closest.health -= self.damage
                self.timer = 0
                self.color = green
            else:
                self.color = mint_green

        if self.health <= 0:
            AntiDroneTower.AAtowers.remove(self)
            return

        pygame.draw.rect(win,self.color,self.rect)
        #win.blit(self.image, (self.x, self.y))

class Turret(Tower):
    def __init__(self):
        Tower.__init__(self,1,100,10,0,0,win)

class BuilderTower:
        bTowers = []
        def __init__(self,x,y):
                self.x = x
                self.y = y
                self.health = 400
                self.width = 80
                self.height = 80
                self.futurex = 0
                self.futurey = 0
                self.buildtimer = 100
                self.buildspawn = 0
                self.suduku = False
                self.image = pygame.image.load("Art/BuilderTower.png")
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                BuilderTower.bTowers.append(self)
        def tick(self, keys, win):

                self.buildspawn += 1
                if self.buildspawn >= self.buildtimer:
                        if self.suduku == False:
                            self.buildspawn = 0
                            builder = EnemyBuilderDrone(self.x + self.width/2, self.y + self.height/2,Tower)
                        elif self.suduku == True:
                            for i in range(15):
                                if i <= 12:
                                    builder = EnemyBuilderDrone(self.x + self.width/2, self.y + self.height/2,Tower)
                                elif i >= 13:
                                    builder = EnemyBuilderDrone(self.x + self.width / 2, self.y + self.height / 2,
                                                                BuilderTower)
                            BuilderTower.bTowers.remove(self)
                            return

                if self.health <= 0:
                    BuilderTower.bTowers.remove(self)
                    return


                #self.image = pygame.transform.scale( self.image, (self.width, self.height))
                #win.blit(self.image, (self.x, self.y))
                self.image = pygame.transform.scale(self.image, (self.width, self.height))
                win.blit(self.image, (self.x, self.y))
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                if self.suduku == False:
                    self.image = pygame.image.load("Art\BuilderTower.png")
                elif self.suduku == True:
                    self.image = pygame.image.load("Art\BuilderTower-Red.png")