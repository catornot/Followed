import pygame
from random import randint

class Block(object):
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.IsPickupable = False
        self.HasInventory = False
        self.id = randint( 0, 999999 ) # hope stuff won't be similar 

    def collide(self, x, y):
        if self.x == x and self.y == y:
            return True
        return False
    
    def PickupBlock( self, entity ):
        if not self.HasInventory or not entity.IsPickupable:
            return
        
        if entity.IsKey:
            self.inventory["keys"] += 1

    def move(self, direction):
        match direction:
            case "left":
                self.x -= 1
            case "right":
                self.x += 1
            case "up":
                self.y -= 1
            case "down":
                self.y += 1

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def render(self, surface):
        pygame.draw.rect(surface, self.color, (self.x*self.w, self.y*self.h, self.w, self.h))

    def __eq__(self, other):
        try:
            return self.id == other.id
        except:
            pass
        return False
