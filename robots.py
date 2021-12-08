import pygame
import pygame_gui
from maps import *

points = 0

black = (235, 89, 235)
white = (255,255,255)
red = (255,0,0)
dimGray = (105,105,105)
blue = (25,35,255)
darkGray = (50,50,200)
darkerGray = (20,20,20)

class Robot():
    robots = []
    def __init__(self,dis,speed,maxH,color,moneyGive):
       self.distance = dis
       self.speed = speed
       self.maxHealth = maxH
       self.health = self.maxHealth
       self.color = color
       self.moneyGive = moneyGive
       self.pathstep = 0
       self.x = path[0][self.pathstep]
       self.y = path[1][self.pathstep]
       Robot.robots.append(self)
    def draw(self,win):
        rect = pygame.Rect(self.x,self.y,20,20)
        pygame.draw.rect(win,self.color ,rect)
    def tick(self,win):
        self.draw(win)
        if self.x == path[0][self.pathstep] and self.y == path[1][self.pathstep]:
            self.pathstep += 1
            try:
                a = path[0][self.pathstep]
            except IndexError:
                Robot.robots.remove(self)
                global points
                points += 1
                return

        if self.x < path[0][self.pathstep]:
            self.x += self.speed
        if self.x > path[0][self.pathstep]:
            self.x += -self.speed
        if self.y < path[1][self.pathstep]:
            self.y += self.speed
        if self.y > path[1][self.pathstep]:
            self.y += -self.speed
        #mousePos = pygame.mouse.get_pos()
        #manager2 = pygame_gui.UIManager((800, 800), 'gui_theme.json')
        #if mousePos[0] > self.x and mousePos[0] < self.x+20 or mousePos[0] < self.x and mousePos[0] > self.x-20:
          #  if mousePos[1] > self.y and mousePos[1] < self.y+20 or mousePos[1] < self.y and mousePos[1] > self.y-20:
        #ShowHealth = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((200,200),(50, 50)),
         #                                           text=str(self.health)+"/"+str(self.maxHealth),
          #                                          manager=manager2)
        if self.health <=0:
            Robot.robots.remove(self)
            del self


class Normal(Robot):
    def __init__(self):
        Robot.__init__(self,0,2,4,dimGray,5)

class Speedy(Robot):
    def __init__(self):
        Robot.__init__(self,0,4,3,blue,6)

class Slow(Robot):
    def __init__(self):
        Robot.__init__(self,0,0.5,10,darkGray,10)

class SlowBoss(Robot):
    def __init__(self):
        Robot.__init__(self,0,0.5,100,darkerGray,50)

class DeathGuard(Robot):
    def __init__(self):
        Robot.__init__(self,0,0.2,250000,black,2500)

class DeathKing(Robot):
    def __init__(self):
        Robot.__init__(self,0,0.2,500000,black,5000)

def spawnRobot(robotType):
    globals()[robotType]()



