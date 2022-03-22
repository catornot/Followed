from states.state import State

from level import Level
from utils import Utils

class Game(State):
    def setup(self):
        self.level = Level()
        self.levels = Utils.read_levels("levels")
        self.current_level = 0
        self.load_level(self.current_level)

    def load_level(self, level):
        self.level.load_level(self.levels[level])

    def update(self, events):
        if events.get("keydown-left"):
            self.level.player.move("left")
            self.level.twin.move("right")
        elif events.get("keydown-right"):
            self.level.player.move("right")
            self.level.twin.move("left")
        elif events.get("keydown-up"):
            self.level.player.move("up")
            self.level.twin.move("down")
        elif events.get("keydown-down"):
            self.level.player.move("down")
            self.level.twin.move("up")

    def render(self, surface):
        self.level.render(surface)
