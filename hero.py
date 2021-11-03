import pygame

class Robot():
    robots = []
    def __init__(self,speed,maxH,color,moneyGive):
       self.distance = 1
       self.speed = speed
       self.color = color
       Robot.robots.append(self)
    def draw(self,win):
        rect = pygame.Rect(self.x,self.y,60,60)
        pygame.draw.rect(win,self.color ,rect)
    def tick(self,win):
        self.draw(win)
