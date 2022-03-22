from states.state import State

#constants
LevelAmount = 1

from level import Level
# from utils import Utils

class Game(State):
    def setup(self):
        self.level = Level()
        # self.levels = Utils.read_levels("levels")
        self.current_level = 0
        self.load_level(self.current_level)

    
    def next_level(self):
        self.current_level += 1
        if self.current_level >= len(LevelAmount):
            self.current_level = 0
        self.level.loadLevelByIndex(self.current_level)

    def restart_level(self):
        self.level.loadLevelByIndex(self.current_level)

    def load_level(self, level:int):
        self.level.loadLevelByIndex(level)

    def update(self, events):
        if events.get("keydown-left"):
            if not self.level.move("left"): self.manager.screenshake()
        elif events.get("keydown-right"):
            if not self.level.move("right"): self.manager.screenshake()
        elif events.get("keydown-up"):
            if not self.level.move("up"): self.manager.screenshake()
        elif events.get("keydown-down"):
            if not self.level.move("down"): self.manager.screenshake()

    def render(self, surface):
        self.level.render(surface)
