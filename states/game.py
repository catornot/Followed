from states.state import State

from level import Level
from utils import Utils

class Game(State):
    def setup(self):
        self.level = Level()
        self.levels = Utils.read_levels("levels")
        self.current_level = 0
        self.load_level(self.current_level)

    def next_level(self):
        self.level += 1
        if self.level >= len(self.levels):
            self.level = 0
        self.level.load_level(self.levels[self.level])

    def restart_level(self):
        self.level.load_level(self.levels[self.level])

    def load_level(self, level):
        self.level.load_level(self.levels[level])

    def update(self, events):
        if events.get("keydown-left"):
            self.level.move("left")
        elif events.get("keydown-right"):
            self.level.move("right")
        elif events.get("keydown-up"):
            self.level.move("up")
        elif events.get("keydown-down"):
            self.level.move("down")

    def render(self, surface):
        self.level.render(surface)
