from states.state import State
from pygame import Surface, SRCALPHA, mixer

class Transition(State):
    def setup(self):
        self.image = Surface((self.manager.SCREEN_W, self.manager.SCREEN_H), flags=SRCALPHA)
        self.alpha = 0
        self.speed = 2
        self.active = False
        self.endstate = None

    def update(self):
        if self.active:
            self.image.fill((50, 50, 50, self.alpha))
            self.alpha += self.speed
            if self.alpha >= 250:
                self.speed = -5
                self.manager._state = self.endstate
            # if self.alpha == 150: # maybe a better transition sfx
            #     self.manager.sfx["transtion"].play()
            elif self.alpha <= 0:
                self.active = False

    def render(self, surface):
        if self.active:
            surface.blit(self.image, (0, 0))
