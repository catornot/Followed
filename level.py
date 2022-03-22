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

    def move(self, direction):
        positions = [[boundary.x, boundary.y] for boundary in self.boundaries]

        match direction:
            case "left":
                if not [self.player.x - 1, self.player.y] in positions and not [self.twin.x + 1, self.twin.y] in positions:
                    self.player.move("left")
                    self.twin.move("right")
                    return True
            case "right":
                if not [self.player.x + 1, self.player.y] in positions and not [self.twin.x - 1, self.twin.y] in positions:
                    self.player.move("right")
                    self.twin.move("left")
                    return True
            case "up":
                if not [self.player.x, self.player.y - 1] in positions and not [self.twin.x, self.twin.y + 1] in positions:
                    self.player.move("up")
                    self.twin.move("down")
                    return True
            case "down":
                if not [self.player.x - 1, self.player.y + 1] in positions and not [self.twin.x, self.twin.y - 1] in positions:
                    self.player.move("down")
                    self.twin.move("up")
                    return True

        return False

    def render(self, surface):
        self.player.render(surface)
        self.twin.render(surface)

        for boundary in self.boundaries:
            boundary.render(surface)
