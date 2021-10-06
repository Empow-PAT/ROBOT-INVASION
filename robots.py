import pygame

path = [[0,800],[400,400]]
robots = []
class Robot():
    def __init__(self,dis,speed,maxH,color):
       self.distance = dis
       self.speed = speed
       self.maxHealth = maxH
       self.health = self.maxHealth
       self.color = color
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
                return

        if self.x < path[0][self.pathstep]:
            self.x += self.speed
        if self.x > path[0][self.pathstep]:
            self.x += -self.speed
        if self.y < path[1][self.pathstep]:
            self.y += self.speed
        if self.y > path[1][self.pathstep]:
            self.y += -self.speed

