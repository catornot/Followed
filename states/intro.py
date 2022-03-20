from states.state import State

class Intro(State):
    def setup(self):
        pass

    def update(self, events):
        if events.get("mousebuttondown"):
            self.manager.transition_to("menu")

    def render(self, surface):
        self.manager.render_text(surface, "Intro", self.manager.SCREEN_C[0], 300)
