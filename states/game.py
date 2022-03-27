from states.state import State

#constants
LevelAmount = 11

from level import Level

from utils import mouseToGrid

class Game(State):
    def setup(self):
        self.level = Level()
        self.current_level = 0
        self.load_level(self.current_level)
        # self.level.loadLevelByIndex(9)
        # self.current_level = 9

    def next_level(self):
        self.current_level += 1
        if self.current_level >= LevelAmount:
            self.current_level = 0
        self.level.loadLevelByIndex(self.current_level)

    def restart_level(self):
        self.level.loadLevelByIndex(self.current_level)

    def load_level(self, level:int):
        self.level.loadLevelByIndex(level)

    def update(self, events):
        if events.get("keydown-left"):
            self.level.move("left")
        elif events.get("keydown-right"):
            self.level.move("right")
        elif events.get("keydown-up"):
            self.level.move("up")
        elif events.get("keydown-down"):
            self.level.move("down")
        
        if events.get("restart"):
            self.restart_level()
        
        #for testing
        if events.get("mousebuttondown"):
            if events["mousebuttondown"].button == 1:
                print( mouseToGrid() )


        
        if self.level.requestNextLevel:
            self.level.requestNextLevel = False
            self.next_level()
        elif self.level.requestRestartLevel:
            self.level.requestRestartLevel = False
            self.restart_level()

    def render(self, surface):
        self.level.render(surface)
