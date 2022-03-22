from classes.player import Player
from classes.twin import Twin
from classes.boundary import Boundary

class Level(object):
    def __init__(self):
        self.player = Player(0, 0)
        self.twin = Twin(0, 0)
        self.boundaries = []

    def load_level(self, level):
        self.player.move_to(0, 0)
        self.twin.move_to(0, 0)
        self.boundaries.clear()

        for y, row in enumerate(level):
            for x, block in enumerate(row):
                match block:
                    case "p":
                        self.player.move_to(x, y)
                    case "t":
                        self.twin.move_to(x, y)
                    case "b":
                        self.boundaries.append(Boundary(x, y))

    def render(self, surface):
        self.player.render(surface)
        self.twin.render(surface)

        for boundary in self.boundaries:
            boundary.render(surface)
