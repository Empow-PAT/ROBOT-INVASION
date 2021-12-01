import pygame
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
                        shootingtower = ShootingTower(self.x,self.y)
                        EnemyBuilderDrone.eDrones.remove(self)
                        return



                if self.health <= 0:
                        EnemyBuilderDrone.eDrones.remove(self)
                # self.image = pygame.transform.scale( self.image, (self.width, self.height))
                # win.blit(self.image, (self.x, self.y))
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                pygame.draw.rect(win, red, self.rect)

class BuilderTower:
        def __init__(self):
                self.x = 400
                self.y = 400
                self.health = 400
                self.width = 50
                self.height = 50
                self.buildspawn = 0
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


