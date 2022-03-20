from states.state import State

class Menu(State):
    def setup(self):
        pass

    def update(self, events):
        if events.get("mousebuttondown"):
            if events["mousebuttondown"].button == 1:
                self.manager.transition_to("game")

    def render(self, surface):
        self.manager.render_text(surface, "Menu", self.manager.SCREEN_C[0], 300)
