import pygame
import random
from towers import *
import math

windowwidth = 800
windowheight = 800
win = pygame.display.set_mode((windowwidth, windowheight))
droned = 2
windowwidth = 800
windowheight = 800
black = (0, 0, 0)
white = (255,255,255)
grey = (134,134,134)
mint_green = (111,222,123)
red = (255,0,0)
yellow = (255, 255, 0)
purple_blue = (180,40,255)
blue = (0,0,255)
green = (0,255,0)
#purple_blue = (199,21,133)
#purple_blue = (255,0,255)
#purple_blue = (128,0,128)
#purple_blue = (220,20,60)
#purple_blue = (255,255,0)


class Dummy:
    enemyloc = []
    def __init__(self):
        self.x = 400
        self.y = 400
        self.health = 20
        self.width = 20
        self.height = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        Dummy.enemyloc.append(self)
    def tick(self, win):


        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, red, self.rect)

#Bosses
class Glitch:
    glitchboss = []
    def __init__(self):
        self.addh = 800
        self.addw = 800
        self.x = random.randint(0,800)
        self.y = random.randint(0,800)
        self.health = random.randint(50, 500)
        self.width = random.randint(10,100)
        self.height = random.randint(10,100)
        self.stick = False
        self.futurex = 0
        self.futurey = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.irect = pygame.Rect(self.x + self.height, self.y + self.width, self.height, self.width)
        Glitch.glitchboss.append(self)

    def tick(self, win):
        if self.health <= 0:
            death_pain = random.randint(0,2)
            if death_pain == 1:
                self.addw = 800
                self.addh = 800
                for d in Drone.droneloc:
                    d.ygrav = 0
                    d.xgrav = 0
                Glitch.glitchboss.remove(self)
                return
            if death_pain == 0:
                self.x = random.randint(200,600)
                self.y = random.randint(200, 600)
                self.health = 1000
            if death_pain == 2:
                for e in Drone.droneloc:
                    if (self.x - e.x <= 100 and self.x - e.x >= -100) and (self.y - e.y <= 100 and self.y - e.y >= -100):
                        e.health = 0
                self.addw = 800
                self.addh = 800
                for d in Drone.droneloc:
                    d.ygrav = 0
                    d.xgrav = 0
                Glitch.glitchboss.remove(self)
                return

        time = random.randint(1,100)
        if time == 1:
            attack = random.randint(1,11)
            if attack == 1:
                self.x = random.randint(200, 600)
                self.y = random.randint(200, 600)
            if attack == 2:
                for d in Drone.droneloc:
                    d.x = random.randint(200, 600)
                    d.y = random.randint(200, 600)
            if attack == 3:
                self.addh = random.randint(100,1200)
                self.addw = random.randint(100,1200)
            if attack == 4:
                self.gravity = random.randint(1,4)
                for d in Drone.droneloc:
                    if self.gravity == 1:
                        d.ygrav = -10
                        d.xgrav = 0
                    if self.gravity == 2:
                        d.ygrav = 10
                        d.xgrav = 0
                    if self.gravity == 3:
                        d.xgrav = -10
                        d.ygrav = 0
                    if self.gravity == 4:
                        d.xgrav = 10
                        d.ygrav = 0
            if attack == 5:
                for d in Drone.droneloc:
                    d.ygrav = 0
                    d.xgrav = 0
            if attack == 6:
                self.addh = 800
                self.addw = 800
            if attack == 7:
                self.shield = random.randint(0,3)
                if self.shield == 0:
                    self.irect = pygame.Rect(self.x + self.width + 10, self.y, 10, self.height)
                if self.shield == 1:
                    self.irect = pygame.Rect(self.x - self.width - 10, self.y, 10, self.height)
                if self.shield == 2:
                    self.irect = pygame.Rect(self.x, self.y + self.height + 10, self.width, 10)
                if self.shield == 3:
                    self.irect = pygame.Rect(self.x, self.y - self.height - 10, self.width, 10)
                self.stick = True
                self.addh = 800
                self.addw = 800
            if attack == 8:
                self.x = random.randint(200, 600)
                self.y = random.randint(200, 600)
            if attack == 9:
                self.stick = False
            if attack == 10:
                self.addh = random.randint(100, 1200)
                self.addw = random.randint(100, 1200)
            if attack == 11:
                self.x = random.randint(200, 600)
                self.y = random.randint(200, 600)
        if self.stick == True:
            pygame.draw.rect(win, blue, self.irect)
        else:
            self.irect = pygame.Rect(0, 0, 0, 0)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        glitch_effect = random.randint(1,2)
        if glitch_effect == 1:
            pygame.draw.rect(win, red, self.rect)
class Boid:
    boidbosses = []
    def __init__(self):
        self.x = 400
        self.y = 600
        self.xvel = 0
        self.yvel = 0
        self.health = 10
        self.futurex = 0
        self.futurey = 0
        self.wait = 0
        self.targetnum = random.randint(0,len(Drone.droneloc) -1)
        self.target = Drone.droneloc[self.targetnum]
        self.dronelocLength = len(Drone.droneloc)
        self.firex = self.target.x + random.randint(-15, 15)
        self.firey = self.target.y + random.randint(-15, 15)
        self.xvel = (self.firex - self.x)
        self.yvel = (self.firey - self.y)
        self.width = 5
        self.height = 15
        self.triangle = [(self.x - self.width,self.y),
                         (self.x + self.width,self.y),
                         (self.x,self.y + self.height)]

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        Boid.boidbosses.append(self)
    def tick(self, win):

        if len(Drone.droneloc) <= 0:
            Boid.boidbosses.remove(self)
            return
        if self.target == None:
            self.targetnum = random.randint(0,len(Drone.droneloc) -1)
            self.target = Drone.droneloc[self.targetnum]
        if self.dronelocLength != len(Drone.droneloc):
            self.targetnum = random.randint(0,len(Drone.droneloc) -1)


        self.futurex = self.xvel * 50
        self.futurey = self.yvel * 50

        self.wait += 1
        if self.wait >= 60:
            self.target = Drone.droneloc[self.targetnum]
            self.firex = self.target.x + random.randint(-15, 15)
            self.firey = self.target.y + random.randint(-15, 15)
            self.xvel = (self.firex - self.x)
            self.yvel = (self.firey - self.y)

        self.x += self.xvel / 50
        self.y += self.yvel / 50

        self.tdx = self.target.x - self.x
        self.tdy = self.target.y - self.y

        self.pointx = self.x
        self.pointy = self.y


        self.rect = pygame.Rect(self.pointx - 2, self.pointy - self.height, self.width,self.height)
        self.triangle = [(self.pointx + self.width,self.pointy - self.height),
                         (self.pointx - self.width,self.pointy - self.height),
                         (self.pointx,self.pointy)]

        pygame.draw.lines(win,red,True,self.triangle)

class Fire:
    fireloc = []
    def __init__(self,x,y,target,accuracy):
        self.color = purple_blue
        self.testx = 0
        self.testy = 0
        self.x = x
        self.y = y
        self.accuracy = accuracy
        self.health = 1
        self.width = 2
        self.height = 2
        self.die = 0
        self.target = target
        self.LocState = "1"

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def tick(self, win):

        if self.LocState == "1":
            self.ex = self.target.x
            self.ey = self.target.y
            self.LocState = "2"
            return
        if self.LocState == "2":
            self.exvel = self.ex - self.target.x
            self.eyvel = self.ey - self.target.y
            self.LocState = "3"
            return
        if self.LocState == "3":
            self.firex = self.target.x + self.exvel + random.randint(-self.accuracy, self.accuracy)
            self.firey = self.target.y + self.exvel + random.randint(-self.accuracy, self.accuracy)
            self.xvel = (self.firex - self.x)
            self.yvel = (self.firey - self.y)
            self.LocState = "0"
            return

        if self.target.rect.colliderect(self.rect):
            self.target.health -= self.health
            self.health = 0
            Fire.fireloc.remove(self)
            return

        if self.x > windowwidth - self.width:
            Fire.fireloc.remove(self)
            return
        if self.x < 0:
            Fire.fireloc.remove(self)
            return
        if self.y > windowheight - self.height:
            Fire.fireloc.remove(self)
            return
        if self.y < 0:
            Fire.fireloc.remove(self)
            return
        if self.die >= 100:
            Fire.fireloc.remove(self)
            return

        self.x += self.xvel/50
        self.y += self.yvel/50
        self.die += 1

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, yellow, self.rect)

class Drone:
    droneloc = []
    def __init__(self, drone_skin):
        self.health = 10
        self.animation = 0
        self.skin = drone_skin
        self.x = 114
        self.y = 113
        self.accuracy = 15
        self.width = 17
        self.height = 17
        self.xgoal = self.x
        self.ygoal = self.y
        self.color = white
        self.fired = False
        self.target = self
        self.firelimit = 30
        self.targetSize = 10
        self.buffer = False
        self.goToBuffer = False
        self.toggle = False
        self.reload = 0
        self.checkCooldown = 10
        self.ygrav = 0
        self.xgrav = 0
        self.image = pygame.image.load("Art\Drone.png")
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        self.Frect = pygame.Rect(self.xgoal, self.ygoal, 1, 1)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        Drone.droneloc.append(self)

    def tick(self, keys, win,EnemyBuilderDrone,ShootingTower,Tower,BuilderTower,AntiDroneTower):

        if self.skin == 0:
            #print("Javi is in the general viciinity of the place he was before.")
            self.image = pygame.image.load("Art\Drone.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        elif self.skin == 1:
            self.image = pygame.image.load("Art\Drone Skin.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        if self.skin == 0:
            if self.y == self.ygoal and self.x == self.xgoal:
                self.image = pygame.image.load ( "Art\Drone.png" ).convert_alpha()
            if self.y != self.ygoal and self.x != self.xgoal:
                self.image = pygame.image.load ( "Art\DroneMove.png" ).convert_alpha()
        if self.skin == 1:
            if self.y == self.ygoal and self.x == self.xgoal:
                self.image = pygame.image.load ( "Art\Drone Skin.png" ).convert_alpha()
            if self.y != self.ygoal and self.x != self.xgoal:
                self.image = pygame.image.load ( "Art\Drone Skin2.png" ).convert_alpha()

        def Check():
            for e in AntiDroneTower.AAtowers:
                if e == self.target:
                    return
            for e in ShootingTower.towers:
                if e == self.target:
                    return
            for e in Glitch.glitchboss:
                if e == self.target:
                    return
            for e in EnemyBuilderDrone.eDrones:
                if e == self.target:
                    return
            for e in Tower.towers:
                if e == self.target:
                    return
            for e in BuilderTower.bTowers:
                if e == self.target:
                    return
            self.target = None

        def Target():
            for e in AntiDroneTower.AAtowers:
                if e.rect.colliderect(self.targetRect) and (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                    if self.image == 0:
                        self.image = pygame.image.load("Art\DroneAngry.png")
                    if self.image == 1:
                        self.image = pygame.image.load("Art\Drone Skin3.png").convert_alpha()
                    if len(Fire.fireloc) < self.firelimit and self.fired == False:
                        self.fired = True
                        Fire.fireloc.append(Fire(self.x, self.y, e, self.accuracy))
                        self.target = e
                        return
            for e in ShootingTower.towers:
                if e.rect.colliderect(self.targetRect) and (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                    if self.image == 0:
                        self.image = pygame.image.load("Art\DroneAngry.png")
                    if self.image == 1:
                        self.image = pygame.image.load("Art\Drone Skin3.png").convert_alpha()
                    if len(Fire.fireloc) < self.firelimit and self.fired == False:
                        self.fired = True
                        Fire.fireloc.append(Fire(self.x,self.y,e,self.accuracy))
                        self.target = e
                        return
            for e in Glitch.glitchboss:
                if e.rect.colliderect(self.targetRect) and (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                    if self.image == 0:
                        self.image = pygame.image.load("Art\DroneAngry.png")
                    if self.image == 1:
                        self.image = pygame.image.load("Art\Drone Skin3.png").convert_alpha()
                    if len(Fire.fireloc) < self.firelimit and self.fired == False:
                        self.fired = True
                        Fire.fireloc.append(Fire(self.x, self.y,e,self.accuracy))
                        self.target = e
                        return
            for e in EnemyBuilderDrone.eDrones:
                if e.rect.colliderect(self.targetRect) and (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                    if self.image == 0:
                        self.image = pygame.image.load("Art\DroneAngry.png")
                    if self.image == 1:
                        self.image = pygame.image.load("Art\Drone Skin3.png").convert_alpha()
                    if len(Fire.fireloc) < self.firelimit and self.fired == False:
                        self.fired = True
                        Fire.fireloc.append(Fire(self.x,self.y,e,self.accuracy))
                        self.target = e
                        return
            for e in Tower.towers:
                if e.rect.colliderect(self.targetRect) and (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                    if self.image == 0:
                        self.image = pygame.image.load("Art\DroneAngry.png")
                    if self.image == 1:
                        self.image = pygame.image.load("Art\Drone Skin3.png").convert_alpha()
                    if len(Fire.fireloc) < self.firelimit and self.fired == False:
                        self.fired = True
                        Fire.fireloc.append(Fire(self.x,self.y,e,self.accuracy))
                        self.target = e
                        return
            for e in BuilderTower.bTowers:
                if e.rect.colliderect(self.targetRect) and (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                    if self.image == 0:
                        self.image = pygame.image.load("Art\DroneAngry.png")
                    if self.image == 1:
                        self.image = pygame.image.load("Art\Drone Skin3.png").convert_alpha()
                    if len(Fire.fireloc) < self.firelimit and self.fired == False:
                        self.fired = True
                        Fire.fireloc.append(Fire(self.x,self.y,e,self.accuracy))
                        self.target = e
                        return


        for d in Drone.droneloc:
            if d != self and d.Frect.colliderect(self.Frect):
                xory = random.randint(0,3)
                if xory == 1:
                    #self.x = d.x + d.width + droned
                    self.xgoal = d.xgoal + d.width + droned
                if xory == 0:
                   #self.y = d.y + d.height + droned
                   self.ygoal = d.ygoal + d.height + droned
                if xory == 2:
                    #self.x = d.x - d.width - droned
                    self.xgoal = d.xgoal - d.width - droned
                if xory == 3:
                   #self.y = d.y - d.height - droned
                   self.ygoal = d.ygoal - d.height - droned

        if keys[pygame.K_e] == False:
            self.goToBuffer = False

        if keys[pygame.K_e] == True and self.goToBuffer == False:
            self.animation = 0
            self.goToBuffer = True
            if self.image == 0:
                self.image = pygame.image.load ( "Art\DroneMove.png" ).convert_alpha()
            if self.image == 1:
                self.image = pygame.image.load("Art\Drone Skin3.png").convert_alpha()
            Mx,My = pygame.mouse.get_pos()
            Mx += self.width/2
            My += self.height/2
            self.xgoal,self.ygoal = Mx,My

        if keys[pygame.K_q] == True and self.buffer == False and self.toggle != True:
            self.toggle = True
            self.buffer = True
        elif keys[pygame.K_q] == False:
            self.buffer = False

        if self.toggle == True:
            Mx, My = pygame.mouse.get_pos()
            pygame.draw.circle(win,red,(Mx,My),self.targetSize,int(self.targetSize/5))

            if self.target != None:
                if (self.x - self.target.x <= 150 and self.x - self.target.x >= -150) and (
                        self.y - self.target.y <= 150 and self.y - self.target.y >= -150):
                    pygame.draw.line(win, red, (self.x + self.width / 2, self.y + self.height / 2),
                                     (self.target.x + self.target.width / 2, self.target.y + self.target.height / 2))

            self.targetRect = (Mx - self.targetSize/2,My - self.targetSize/2,self.targetSize,self.targetSize)
            self.CrossRect1 = (Mx - self.targetSize,My - int(self.targetSize/5)/2,self.targetSize * 2,int(self.targetSize/5))
            self.CrossRect2 = (Mx - int(self.targetSize/5)/2,My - self.targetSize,int(self.targetSize/5),self.targetSize * 2)
            pygame.draw.rect(win,red,self.CrossRect1)
            pygame.draw.rect(win, red, self.CrossRect2)
            if self.buffer == False and keys[pygame.K_q] == True:
                self.toggle = False
                self.buffer = True
            if pygame.mouse.get_pressed()[0]:
                Target()

        if self.x < self.xgoal:
            self.x += 1
        if self.x > self.xgoal:
            self.x += -1
        if self.y < self.ygoal:
            self.y += 1
        if self.y > self.ygoal:
            self.y += -1


        def fire():
            if self.toggle == True:
                return
            for e in AntiDroneTower.AAtowers:
                if (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                    if self.image == 0:
                        self.image = pygame.image.load("Art\DroneAngry.png")
                    if self.image == 1:
                        self.image = pygame.image.load("Art\Drone Skin3.png").convert_alpha()
                    if len(Fire.fireloc) < self.firelimit and self.fired == False:
                        self.fired = True
                        Fire.fireloc.append(Fire(self.x, self.y, e, self.accuracy))
                        self.target = e
                        return
            for e in ShootingTower.towers:
                if (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                    if self.image == 0:
                        self.image = pygame.image.load("Art\DroneAngry.png")
                    if self.image == 1:
                        self.image = pygame.image.load("Art\Drone Skin3.png").convert_alpha()
                    if len(Fire.fireloc) < self.firelimit and self.fired == False:
                        self.fired = True
                        Fire.fireloc.append(Fire(self.x,self.y,e,self.accuracy))
                        self.target = e
                        return
            for e in Glitch.glitchboss:
                if (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                    if self.image == 0:
                        self.image = pygame.image.load("Art\DroneAngry.png")
                    if self.image == 1:
                        self.image = pygame.image.load("Art\Drone Skin3.png").convert_alpha()
                    if len(Fire.fireloc) < self.firelimit and self.fired == False:
                        self.fired = True
                        Fire.fireloc.append(Fire(self.x, self.y,e,self.accuracy))
                        self.target = e
                        return
            for e in EnemyBuilderDrone.eDrones:
                if (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                    if self.image == 0:
                        self.image = pygame.image.load("Art\DroneAngry.png")
                    if self.image == 1:
                        self.image = pygame.image.load("Art\Drone Skin3.png").convert_alpha()
                    if len(Fire.fireloc) < self.firelimit and self.fired == False:
                        self.fired = True
                        Fire.fireloc.append(Fire(self.x,self.y,e,self.accuracy))
                        self.target = e
                        return
            for e in Tower.towers:
                if (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                    if self.image == 0:
                        self.image = pygame.image.load("Art\DroneAngry.png")
                    if self.image == 1:
                        self.image = pygame.image.load("Art\Drone Skin3.png").convert_alpha()
                    if len(Fire.fireloc) < self.firelimit and self.fired == False:
                        self.fired = True
                        Fire.fireloc.append(Fire(self.x,self.y,e,self.accuracy))
                        self.target = e
                        return
            for e in BuilderTower.bTowers:
                if (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                    if self.image == 0:
                        self.image = pygame.image.load("Art\DroneAngry.png")
                    if self.image == 1:
                        self.image = pygame.image.load("Art\Drone Skin3.png").convert_alpha()
                    if len(Fire.fireloc) < self.firelimit and self.fired == False:
                        self.fired = True
                        Fire.fireloc.append(Fire(self.x,self.y,e,self.accuracy))
                        self.target = e
                        return

        fire()

        if self.x > windowwidth - self.width:
            self.x = windowwidth - self.width
        if self.x < 0:
            self.x = 0
        if self.y > windowwidth - self.height:
            self.y = windowwidth - self.height
        if self.y < 0:
            self.y = 0

        self.reload += 1
        if self.reload >= 60:
            self.fired = False
            self.reload = 0

        for e in ShootingTower.towers:
            if e.rect.colliderect(self.rect):
                self.health -= 1
                e.health -= 1
        if self.health <= 0:
            Drone.droneloc.remove(self)

        self.checkCooldown += 1
        if self.checkCooldown >= 100:
            Check()
            self.checkCooldown = 0

        def Animate():
            if self.animation <= 5:
                pygame.draw.circle(win, green, (self.xgoal + self.width/2,self.ygoal + self.height/2),4,1)
                self.animation += 1
                return
            if self.animation <= 10:
                pygame.draw.circle(win, green, (self.xgoal + self.width / 2, self.ygoal + self.height / 2), 3, 1)
                self.animation += 1
                return
            if self.animation <= 15:
                pygame.draw.circle(win, green, (self.xgoal + self.width / 2, self.ygoal + self.height / 2), 2, 1)
                self.animation += 1
                return
            if self.animation <= 20:
                pygame.draw.circle(win, green, (self.xgoal + self.width / 2, self.ygoal + self.height / 2), 3, 1)
                self.animation += 1
                self.animation = 0
                return


        self.image = pygame.transform.scale (self.image, (self.width, self.height))
        win.blit(self.image, (self.x, self.y))
        self.Frect = pygame.Rect(self.xgoal , self.ygoal, 1, 1)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.distance = math.hypot(self.xgoal - self.x, self.ygoal - self.y)
        if not self.distance <= 4:
            Animate()
        else:
            self.start = False

