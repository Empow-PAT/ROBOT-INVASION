import pygame
import random
import towers
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
#purple_blue = (199,21,133)
#purple_blue = (255,0,255)
#purple_blue = (128,0,128)
#purple_blue = (220,20,60)
#purple_blue = (255,255,0)

class ShootingTower:
    enemyloc = []
    def __init__(self):
        self.x = 200
        self.y = 400
        self.health = 10000
        self.width = 40
        self.height = 100
        self.rect = pygame.Rect ( self.x, self.y, self.width, self.height )
        self.image = pygame.image.load ( "Art/Tower Dude.jpg" ).convert_alpha()
        self.image = pygame.transform.scale ( self.image, (self.width, self.height))
        self.origimage = self.image

        ShootingTower.enemyloc.append (self)
    def tick(self, keys, win):
        if len ( Drone.droneloc ) > 0:

            mindist = 100000
            closest = False
            for drone in Drone.droneloc:
                dist = math.hypot(drone.x - self.x, drone.y - self.y)
                if dist < mindist:
                    closest = drone
                    print(self.health)
            dx, dy = closest.x - self.x, closest.y - self.y
            angle = math.degrees ( math.atan2 ( -dy, dx ) )
            print(angle)
            self.image = pygame.transform.rotate ( self.origimage, angle )
        for e in Fire.fireloc:
            if e.rect.colliderect ( self.rect ):
                self.health -= 10
                e.health -= 10
                Fire.fireloc.remove (e)
        if self.health <= 0:
            ShootingTower.enemyloc.remove(self)
            return
        if self.health == 0:
            ShootingTower.enemyloc.remove(self)
            return
        win.blit ( self.image, (self.x, self.y) )

#class Dummy:
 #   enemyloc = []
  #  def __init__(self):
   #     self.x = random.randint(0,400)
    #    self.y = random.randint(0,400)
     #   self.health = 20
      #  self.width = 20
       # self.height = 20
        #self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

#        Dummy.enemyloc.append(self)
 #   def tick(self, keys, win):
  #      if self.health <= 0:
   #         Dummy.enemyloc.remove(self)
    #        return
    #Import tower img here
     #   self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
      #  pygame.draw.rect(win, mint_green, self.rect)

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
        if self.health <= 0:
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
        pygame.draw.rect(win, yellow, self.rect)

class Drone:
    droneloc = []
    def __init__(self, drone_skin):
        self.health = 10
        self.skin = drone_skin
        self.x = 114
        self.y = 113

        self.width = 17
        self.height = 17
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.xgoal = 400
        self.ygoal = 400
        self.color = white

        self.image = pygame.image.load("Art\Drone.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.width, self.height))


        Drone.droneloc.append(self)


    def tick(self, keys, win):
        if self.skin == 0:
            #print("Javi is in the general viciinity of the place he was before.")
            self.image = pygame.image.load("Art\Drone.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        elif self.skin == 1:
            self.image = pygame.image.load("Art\DroneSkin.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        if self.skin == 0:
            if self.y == self.ygoal and self.x == self.xgoal:
                self.image = pygame.image.load ( "Art\Drone.png" ).convert_alpha()
            if self.y != self.ygoal and self.x != self.xgoal:
                self.image = pygame.image.load ( "Art\DroneMove.png" ).convert_alpha()
        if self.skin == 1:
            if self.y == self.ygoal and self.x == self.xgoal:
                self.image = pygame.image.load ( "Art\DroneSkin.png" ).convert_alpha()
            if self.y != self.ygoal and self.x != self.xgoal:
                self.image = pygame.image.load ( "Art\DroneSkin2.png" ).convert_alpha()
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
            if self.image == 0:
                self.image = pygame.image.load ( "Art\DroneMove.png" ).convert_alpha()
            if self.image == 1:
                self.image = pygame.image.load("Art\DroneSkin3.png").convert_alpha()
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
        for e in ShootingTower.enemyloc:
            if (self.x - e.x <= 150 and self.x - e.x >= -150) and (self.y - e.y <= 150 and self.y - e.y >= -150):
                self.image = pygame.image.load ( "Art\DroneAngry.png" ).convert_alpha()
                self.firex = e.x
                self.firey = e.y
                if len(Fire.fireloc) <= 15:
                    fire = Fire(self.x,self.y,self.firey,self.firex)
                    #Fire.fireloc.append(fire)
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

        for e in ShootingTower.enemyloc:
            if e.rect.colliderect(self.rect):
                self.health -= 1
                e.health -= 1
        if self.health <= 0:
            Drone.droneloc.remove(self)

        self.image = pygame.transform.scale ( self.image, (self.width, self.height) )
        win.blit(self.image, (self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.draw.rect(win, self.color, self.rect)