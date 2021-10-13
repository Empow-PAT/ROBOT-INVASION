import pygame
import random

droned = 2
windowwidth = 800
windowheight = 800
black = (0, 0, 0)
white = (255,255,255)
grey = (134,134,134)
mint_green = (111,222,123)
red = (255,0,0)
purple_blue = (138,43,226)


class Wall:
    def __init__(self):
        self.x = 200
        self.y = 200
        self.width = 100
        self.height = 100
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def tick(self, keys, win):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, purple_blue, self.rect)


class Dummy:
    enemyloc = []
    def __init__(self):
        self.x = random.randint(0,400)
        self.y = random.randint(0,400)
        self.health = 20
        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        Dummy.enemyloc.append(self)
    def tick(self, keys, win):
        if self.health <= 0:
            Dummy.enemyloc.remove(self)
            return

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, mint_green, self.rect)

class Fire:
    fireloc = []
    def __init__(self,x,y,firey,firex):
        self.x = x
        self.y = y
        self.health = 1
        self.width = 1
        self.height = 1
        self.firex = firex
        self.firey = firey
        self.xvel = 0
        self.yvel = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        Fire.fireloc.append(self)
    def tick(self, win):
        for e in Dummy.enemyloc:
            if e.rect.colliderect(self.rect):
                e.health -= self.health
                self.health -= 1
                Fire.fireloc.remove(self)
                return
        if self.health <= 0:
            Fire.fireloc.remove(self)
            return

        if (self.firey <= self.y + 10 and self.firey >= self.y -10) and (self.firex <= self.x + 10 and self.firex >= self.x -10):
            Fire.fireloc.remove(self)
            return

        if self.firex < self.x:
            self.xvel = -1
        if self.firex > self.x:
            self.xvel = 1
        if self.firey < self.y:
            self.yvel = -1
        if self.firey > self.y:
            self.yvel = 1

        self.x += self.xvel
        self.y += self.yvel

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, purple_blue, self.rect)

class Drone:
    droneloc = []
    def __init__(self):
        self.health = 10
        self.x = 400
        self.y = 400
        self.width = 17
        self.height = 17
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.xgoal = 400
        self.ygoal = 400
        self.color = white
        Drone.droneloc.append(self)
    def tick(self, keys, win, wall):
        if self.y == self.ygoal and self.x == self.xgoal:
            self.color = white
        if self.y != self.ygoal and self.x != self.xgoal:
            self.color = grey
        for d in Drone.droneloc:
            if d != self and d.rect.colliderect(self.rect):
                xory = random.randint(0,3)
                if xory == 1:
                    self.x = d.x + d.width + droned
                    self.xgoal = d.xgoal + d.width + droned
                if xory == 0:
                    self.y = d.y + d.height + droned
                    self.ygoal = d.ygoal + d.height + droned
                if xory == 2:
                    self.x = d.x - d.width - droned
                    self.xgoal = d.xgoal - d.width - droned
                if xory == 3:
                    self.y = d.y - d.height - droned
                    self.ygoal = d.ygoal - d.height - droned
        if keys[pygame.K_e] == True:
            Mx,My = pygame.mouse.get_pos()
            Mx += -10
            My += -10
            self.xgoal,self.ygoal = Mx,My
        if self.x < self.xgoal:
            self.x += 1
        if self.x > self.xgoal:
            self.x += -1
        if self.y < self.ygoal:
            self.y += 1
        if self.y > self.ygoal:
            self.y += -1
        for e in Dummy.enemyloc:
            if (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                self.color = red
                self.firex = e.x
                self.firey = e.y
                if len(Fire.fireloc) <= 15:
                    fire = Fire(self.x,self.y,self.firey,self.firex)
                    Fire.fireloc.append(fire)
                for f in Fire.fireloc:
                    f.tick(win)

        if self.x > windowwidth - self.width:
            self.x = windowwidth - self.width
        if self.x < 0:
            self.x = 0
        if self.y > windowwidth - self.height:
            self.y = windowwidth - self.height
        if self.y < 0:
            self.y = 0


        if wall.rect.colliderect(self.rect):
            if (self.width - self.x) <= (wall.width - wall.x):
                self.x += 17


        if self.health <= 0:
            Drone.droneloc.remove(self)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, self.color, self.rect)
