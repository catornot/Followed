from states.state import State

class Intro(State):
    def setup(self):
        pass

    def update(self, events):
        if events.get("mousebuttondown"):
            if events["mousebuttondown"].button == 1:
                self.manager.transition_to("menu")
                self.manager.sfx["select"].play()

    def render(self, surface):
        self.manager.render_text(surface, "Intro\n\nmade by\nParallax\ncatornot", self.manager.SCREEN_C[0], 300)
