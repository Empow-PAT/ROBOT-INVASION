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
purple_blue = (180,40,255)
#purple_blue = (199,21,133)
#purple_blue = (255,0,255)
#purple_blue = (128,0,128)
#purple_blue = (220,20,60)
#purple_blue = (255,255,0)


class Dummy:
    enemyloc = []
    def __init__(self):
        self.x = random.randint(0,400)
        self.y = random.randint(0,400)
        self.health = 20
        self.width = 20
        self.height = 50
        self.image = pygame.image.load("Art\Tower Dude.jpg")
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        Dummy.enemyloc.append(self)
    def tick(self, keys, win):
        if self.health <= 0:
            Dummy.enemyloc.remove(self)
            return
    #Import tower img here
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.image,(self.x,self.y))

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
        self.image = pygame.image.load("Art\Drone.png")
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        Drone.droneloc.append(self)
    def tick(self, keys, win):
        if self.y == self.ygoal and self.x == self.xgoal:
            self.image = pygame.image.load ( "Art\Drone.png" )
        if self.y != self.ygoal and self.x != self.xgoal:
            self.image = pygame.image.load ( "Art\DroneMove.png" )
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
            self.image = pygame.image.load ( "Art\DroneMove.png" )
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
                self.image = pygame.image.load ( "Art\DroneAngry.png" )
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

        for e in Dummy.enemyloc:
            if e.rect.colliderect(self.rect):
                self.health -= 1
                e.health -= 1
        if self.health <= 0:
            Drone.droneloc.remove(self)

        self.image = pygame.transform.scale ( self.image, (self.width, self.height) )
        win.blit(self.image, (self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.draw.rect(win, self.color, self.rect)
