import pygame
import random
import math
from drones import *

windowwidth = 800
windowheight = 800
black = (0, 0, 0)
RandoColor = (0,255,255)
white = (255,255,255)
FireRed = (255, 69, 0)

class Enemy_tower:
    def __init__(self):
        self.x = 400
        self.health = 100
        self.projectile_timer = 0
        self.y = 400
        self.width = 20
        self.height = 100
        self.direction = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        Dummy.enemyloc.append(self)
    def tick(self, keys, win):
        self.projectile_timer += 1
        if self.projectile_timer == 10:
            self.direction += 8
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, RandoColor, self.rect)
        if self.health <= 0:
            Dummy.enemyloc.remove(self)

class Enemy_projectile:
    eproj = []
    def __init__(self, enemy_tower):
        self.width =10
        self.health = 1
        self.height = 10
        self.xvelocity = 10 * math.cos(math.radians(enemy_tower.direction))
        self.yvelocity = 10 * math.sin(math.radians(enemy_tower.direction))
        self.x = enemy_tower.x
        self.y = enemy_tower.y
        Enemy_projectile.eproj.append(self)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def tick(self, keys, win):
        self.x += self.xvelocity
        self.y += self.yvelocity
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        if self.health <= 0:
            Enemy_projectile.eproj.remove(self)
        pygame.draw.rect(win, white, self.rect)