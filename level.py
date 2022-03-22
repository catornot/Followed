from classes.player import Player
from classes.twin import Twin
from classes.exit import Exit
from classes.boundary import Boundary
from classes.trap import Trap
from classes.key import Key

class Level(object):
    def __init__(self):
        self.player = Player(0, 0)
        self.twin = Twin(0, 0)
        self.exit = Exit(0, 0)
        self.boundaries = []
        self.traps = []
        self.keys = []

    def load_level(self, level):
        self.player.move_to(0, 0)
        self.twin.move_to(0, 0)
        self.exit.move_to(0, 0)
        self.boundaries.clear()
        self.traps.clear()
        self.keys.clear()

        for y, row in enumerate(level):
            for x, block in enumerate(row):
                match block:
                    case "p":
                        self.player.move_to(x, y)
                    case "t":
                        self.twin.move_to(x, y)
                    case "e":
                        self.exit.move_to(x, y)
                    case "b":
                        self.boundaries.append(Boundary(x, y))
                    case "T":
                        self.traps.append(Trap(x, y))
                    case "k":
                        self.keys.append(Key(x, y))

    def move(self, direction):
        positions = [[boundary.x, boundary.y] for boundary in self.boundaries]

        match direction:
            case "left":
                if not [self.player.x - 1, self.player.y] in positions:
                    self.player.move("left")
            case "right":
                if not [self.player.x + 1, self.player.y] in positions:
                    self.player.move("right")
            case "up":
                if not [self.player.x, self.player.y - 1] in positions:
                    self.player.move("up")
            case "down":
                if not [self.player.x - 1, self.player.y + 1] in positions:
                    self.player.move("down")
        
        twin_direction = self.twin.move_toward(self.player.x, self.player.y)
        match twin_direction:
            case "left":
                if not [self.twin.x - 1, self.twin.y] in positions:
                    self.twin.move("left")
            case "right":
                if not [self.twin.x + 1, self.twin.y] in positions:
                    self.twin.move("right")
            case "up":
                if not [self.twin.x, self.twin.y - 1] in positions:
                    self.twin.move("up")
            case "down":
                if not [self.twin.x, self.twin.y + 1] in positions:
                    self.twin.move("down")

    def render(self, surface):
        self.player.render(surface)
        self.twin.render(surface)
        self.exit.render(surface)

        for boundary in self.boundaries:
            boundary.render(surface)

        for trap in self.traps:
            trap.render(surface)

        for key in self.keys:
            key.render(surface)
