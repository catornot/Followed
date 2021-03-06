import pygame
import sys

from states.intro import Intro
from states.menu import Menu
from states.game import Game
from states.transition import Transition
from states.editor import Editor

from utils import music_manager as Music_Manager

import random

class Main(object):
    def __init__(self):
        pygame.init()

        self.SCREEN_W = 960
        self.SCREEN_H = 640
        self.SCREEN_C = (self.SCREEN_W / 2, self.SCREEN_H / 2)
        self.SCREEN = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.CLOCK = pygame.time.Clock()

        self.DISPLAY = pygame.Surface((self.SCREEN_W, self.SCREEN_H), flags=pygame.SRCALPHA)


        pygame.display.set_icon(pygame.image.load('assets/icons/icon.ico'))
        pygame.display.set_caption('Followed')
        
        self.music_manager = Music_Manager()

        self.fonts = {
            "general": pygame.font.Font("assets/fonts/oswald.ttf", 25)
        }

        self.sfx = {
            "transtion": pygame.mixer.Sound("assets/sfx/transtion.wav"),
            "select": pygame.mixer.Sound("assets/sfx/select.wav"),
        }

        self.screen_shake = {
            "intensity": 0,
            "duration": 0,
            "active": False
        }

        self._events = {}

        self._states = {
            "intro": Intro(self),
            "menu": Menu(self),
            "game": Game(self),
            "transition": Transition(self),
            "level_editor": Editor(self)
        }

        self._state = "intro"

    def events(self):
        self._events.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.shutdown()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self._events["mousebuttondown"] = event

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self._events["keydown-left"] = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self._events["keydown-right"] = True
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self._events["keydown-up"] = True
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self._events["keydown-down"] = True
                elif event.key == pygame.K_r:
                    self._events["restart"] = True
                elif event.key == pygame.K_l:
                    self._events["level"] = True
                elif event.key == pygame.K_y:
                    self._events["save"] = True
                elif event.key == pygame.K_1:
                    self._events["1"] = True
                elif event.key == pygame.K_2:
                    self._events["2"] = True
                elif event.key == pygame.K_3:
                    self._events["3"] = True
                elif event.key == pygame.K_4:
                    self._events["4"] = True
                elif event.key == pygame.K_5:
                    self._events["5"] = True
                elif event.key == pygame.K_6:
                    self._events["6"] = True
                elif event.key == pygame.K_7:
                    self._events["7"] = True
                elif event.key == pygame.K_8:
                    self._events["8"] = True
                elif event.key == pygame.K_9:
                    self._events["9"] = True
                elif event.key == pygame.K_0:
                    self._events["0"] = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self._events["keydown-left"] = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self._events["keydown-right"] = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    self._events["keydown-up"] = False
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self._events["keydown-down"] = False
                elif event.key == pygame.K_r:
                    self._events["restart"] = False
                elif event.key == pygame.K_l:
                    self._events["level"] = False
                elif event.key == pygame.K_y:
                    self._events["save"] = False
                elif event.key == pygame.K_1:
                    self._events["1"] = False
                elif event.key == pygame.K_2:
                    self._events["2"] = False
                elif event.key == pygame.K_3:
                    self._events["3"] = False
                elif event.key == pygame.K_4:
                    self._events["4"] = False
                elif event.key == pygame.K_5:
                    self._events["5"] = False
                elif event.key == pygame.K_6:
                    self._events["6"] = False
                elif event.key == pygame.K_7:
                    self._events["7"] = False
                elif event.key == pygame.K_8:
                    self._events["8"] = False
                elif event.key == pygame.K_9:
                    self._events["9"] = False
                elif event.key == pygame.K_0:
                    self._events["0"] = False

    def update(self):
        self._states[self._state].update(self._events)
        self._states["transition"].update()

        if self.screen_shake["active"]:
            if self.screen_shake["duration"] > 0:
                self.screen_shake["duration"] -= 1
            else:
                self.screen_shake["active"] = False
        
        self.music_manager.update( self._state )

    def render(self):
        self.DISPLAY.fill((0, 0, 0))

        self._states[self._state].render(self.DISPLAY)
        self._states["transition"].render(self.DISPLAY)

        display_offset = [0, 0]

        if self.screen_shake["active"]:
            display_offset[0] += random.randint(-self.screen_shake["intensity"][0], self.screen_shake["intensity"][0])
            display_offset[1] += random.randint(-self.screen_shake["intensity"][1], self.screen_shake["intensity"][1])

        self.SCREEN.blit(self.DISPLAY, display_offset)

        pygame.display.update()

    def screenshake(self, intensity=[2, 2], duration=20):
        self.screen_shake["intensity"] = intensity
        self.screen_shake["duration"] = duration
        self.screen_shake["active"] = True

    def render_text(self, surface, text, x, y, font="general", render_centerx=True, render_centery=True):
        for i, line in enumerate(text.split("\n")):
            text_surface = self.fonts[font].render(line, True, (255, 255, 255))
            text_surface_3D = self.fonts[font].render(line, True, (120, 120, 120))

            match render_centerx, render_centery:
                case True, True:
                    text_rect = text_surface.get_rect(center=(x, y + text_surface.get_height() * i))
                case True, False:
                    text_rect = text_surface.get_rect(centerx=x, top=y + text_surface.get_height() * i)
                case False, True:
                    text_rect = text_surface.get_rect(left=x, centery=y + text_surface.get_height() * i)
                case False, False:
                    text_rect = text_surface.get_rect(topleft=(x, y + text_surface.get_height() * i))

            text_rect_3D = text_rect.copy()
            text_rect_3D.x += 3
            text_rect_3D.y -= 3

            surface.blit(text_surface_3D, text_rect_3D)
            surface.blit(text_surface, text_rect)

    def loop(self):
        while True:
            self.events()
            self.update()
            self.render()
            self.CLOCK.tick(60)

    def transition_to(self, state, setup=True, speed=2):
        if not self._states["transition"].active:
            if setup:
                self._states[state].setup()
            self._states["transition"].setup()
            self._states["transition"].speed = speed
            self._states["transition"].active = True
            self._states["transition"].endstate = state

    def shutdown(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Main().loop()
