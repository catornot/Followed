from states.state import State
from pygame import mixer

class Menu(State):
    def setup(self):
        mixer.fadeout(20)
        self.music_playing = False

    def update(self, events):
        if events.get("mousebuttondown"):
            if events["mousebuttondown"].button == 1:
                self.manager.transition_to("game")
                mixer.fadeout(20)
                self.manager.music["select"].play()
        
        if events.get("level"):
            self.manager.transition_to("level_editor")
        
        if not self.music_playing:
            self.manager.music["main_menu"].set_volume(0.2)
            self.manager.music["main_menu"].play(loops=1000000)

    def render(self, surface):
        self.manager.render_text(surface, "Menu", self.manager.SCREEN_C[0], 300)
