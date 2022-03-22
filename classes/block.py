import pygame

class Block(object):
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

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
