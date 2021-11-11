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
    #Import tower img here
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, red, self.rect)

class Glitch:
    boss = []
    def __init__(self):
        self.addh = 800
        self.addw = 800
        self.x = random.randint(0,800)
        self.y = random.randint(0,800)
        self.health = random.randint(50, 500)
        self.width = random.randint(10,100)
        self.height = random.randint(10,100)
        self.stick = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.irect = pygame.Rect(self.x + self.height, self.y + self.width, self.height, self.width)
        Glitch.boss.append(self)

    def tick(self, win):
        if self.health <= 0:
            death_pain = random.randint(0,2)
            if death_pain == 1:
                self.addw = 800
                self.addh = 800
                for d in Drone.droneloc:
                    d.ygrav = 0
                    d.xgrav = 0
                Glitch.boss.remove(self)
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
                Glitch.boss.remove(self)
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

class Fire:
    fireloc = []
    def __init__(self,x,y,firey,firex):
        self.color = purple_blue
        self.testx = 0
        self.testy = 0
        self.x = x
        self.y = y
        self.health = 1
        self.width = 1
        self.height = 1
        self.firex = firex
        self.firey = firey
        self.xvel = 0
        self.yvel = 0

        if self.firex < self.x:
            self.xvel = -1
        elif self.firex > self.x:
            self.xvel = 1

        if self.firey < self.y:
            self.yvel = -1
        elif self.firey > self.y:
            self.yvel = 1

        if (self.x - firex >= 0) and (self.y - firey <= 40 and self.y - firey >= -40):
            self.yvel = 0
            self.xvel = -1
        if (self.x - firex <= 0) and (self.y - firey <= 40 and self.y - firey >= -40):
            self.yvel = 0
            self.xvel = 1

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def tick(self, win, EnemyBuilderDrone):

        for e in Dummy.enemyloc:
            if e.rect.colliderect(self.rect):
                e.health -= self.health
                self.health = 0
                Fire.fireloc.remove(self)
                return
        for e in Glitch.boss:
            if e.rect.colliderect(self.rect):
                e.health -= self.health
                self.health = 0
                Fire.fireloc.remove(self)
                return
        for e in Glitch.boss:
            if e.irect.colliderect(self.rect):
                self.health = 0
                Fire.fireloc.remove(self)
                return
        for e in EnemyBuilderDrone.eDrones:
            if e.rect.colliderect(self.rect):
                e.health -= self.health
                self.health = 0
                Fire.fireloc.remove(self)
                return

        if self.xvel <= -1:
            self.testx = 0

            if self.firex <= self.x:
                self.x += self.xvel
            if self.firex >= self.x:
                self.x += self.xvel
                self.testx = 1

        if self.xvel >= 1:
            self.testx = 0

            if self.firex >= self.x:
                self.x += self.xvel
            if self.firex <= self.x:
                self.x += self.xvel
                self.testx = 1




        if self.yvel <= -1:
            self.testy = 0

            if self.firey <= self.y:
                self.y += self.yvel
            if self.firey >= self.y:
                self.y += self.yvel
                self.testy = 1

        if self.yvel >= 1:
            self.testy = 0

            if self.firey >= self.y:
                self.y += self.yvel
            if self.firey <= self.y:
                self.y += self.yvel
                self.testy = 1


        if self.testy and self.testx:
            Fire.fireloc.remove(self)
            return

        if self.health <= 0 or self.y == self.firey and self.x == self.firex:
            Fire.fireloc.remove(self)
            return


        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, self.color, self.rect)

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
        self.ygrav = 0
        self.xgrav = 0
        self.image = pygame.image.load("Art\Drone.png")
        self.image = pygame.transform.scale(self.image,(self.width, self.height))
        Drone.droneloc.append(self)
    def tick(self, keys, win, EnemyBuilderDrone):
        self.x += self.xgrav
        self.y += self.ygrav
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
        self.image = pygame.image.load("Art\Drone.png")
        for e in Dummy.enemyloc:
            if (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                self.image = pygame.image.load ( "Art\DroneAngry.png" )
                self.firex = e.x + e.width/2
                self.firey = e.y + e.height/2
                if len(Fire.fireloc) <= 15:
                    Fire.fireloc.append(Fire(self.x,self.y,self.firey,self.firex))
        for e in Glitch.boss:
            if (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                self.image = pygame.image.load("Art\DroneAngry.png")
                self.firex = e.x + e.width/2
                self.firey = e.y + e.height/2
                if len(Fire.fireloc) <= 15:
                    Fire.fireloc.append(Fire(self.x, self.y, self.firey, self.firex))
        for e in EnemyBuilderDrone.eDrones:
            if (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                self.image = pygame.image.load ( "Art\DroneAngry.png" )
                self.firex = e.x + e.width/2
                self.firey = e.y + e.height/2
                if len(Fire.fireloc) <= 15:
                    Fire.fireloc.append(Fire(self.x,self.y,self.firey,self.firex))

        for f in Fire.fireloc:
            f.tick(win, EnemyBuilderDrone)

        if self.x > windowwidth - self.width:
            self.x = windowwidth - self.width
            self.xgrav = 0
        if self.x < 0:
            self.x = 0 + self.width
            self.xgrav = 0
        if self.y > windowheight - self.height:
            self.y = windowheight - self.height
            self.ygrav = 0
        if self.y < 0:
            self.y = 0 + self.height
            self.ygrav = 0

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
