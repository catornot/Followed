from states.state import State
from pygame import mixer

class Menu(State):
    def setup(self):
        self.music_playing = False

    def update(self, events):
        if events.get("mousebuttondown"):
            if events["mousebuttondown"].button == 1:
                self.manager.transition_to("game")
                self.manager.sfx["select"].play()
        
        if events.get("level"):
            self.manager.transition_to("level_editor")

    def render(self, surface):
        self.manager.render_text(surface, "Start", self.manager.SCREEN_C[0], 300)
