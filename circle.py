import pygame

class Circle:
    
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.r = radius
        self.color = color
        self.dir = "right"
        
    def move(self, width):
        if self.dir == "right":
            self.x += 1
        elif self.dir == "left":
            self.x -= 1
            
        if self.x > width:
            self.dir = "left"
        elif self.x < 0:
            self.dir = "right"
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)