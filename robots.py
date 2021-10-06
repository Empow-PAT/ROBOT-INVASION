import pygame

class Robot():
    def __init__(self,dis,x,y,speed,maxH,color):
       self.distance = dis
       self.x = x
       self.y = y
       self.speed = speed
       self.maxHealth = maxH
       self.health = self.maxHealth
       self.color = color
    def draw(self,win):
        rect = pygame.Rect(self.x,self.y,20,20)
        pygame.draw.rect(win,self.color ,rect)
    def tick(self,win):
        self.draw(win)