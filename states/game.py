from states.state import State

class Game(State):
    def setup(self):
        pass

    def update(self, events):
        pass

    def render(self, surface):
        self.manager.render_text(surface, "Game", self.manager.SCREEN_C[0], 300)
