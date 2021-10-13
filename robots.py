import pygame
import pygame_gui

path = [[0,800],[400,400]]
robots = []
points = 0
money = 40

black = (235, 89, 235)
white = (255,255,255)
red = (255,0,0)
dimGray = (105,105,105)
blue = (25,35,255)
darkGray = (50,50,200)
darkerGray = (20,20,20)

class Robot():
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
       robots.append(self)
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
                robots.remove(self)
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

class DeathKing(Robot):
    def __init__(self):
        Robot.__init__(self,0,0.2,500000,black,5000)




