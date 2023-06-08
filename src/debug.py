import pygame

from config import *

# TODO: Use custom font.
# TODO: Draw transparent background behind text.

# setup pygame.font.render() args
antialias = True
color = 'white'
bgcolor = 'black'  # can be used for optimization
wraplength = 0     # max width (in pixels) before wrapping to new line


class Console:
    def __init__(self):
        self.font = pygame.font.Font(None, 24)  # TODO: use custom font
        self.messages = []
        # TODO: set timers for message lifespans & fade out?
        self.surf = pygame.surface.Surface((0,0))
        self.rect = self.surf.get_rect()
        self.fps_surf = pygame.surface.Surface((0,0))
        self.fps_rect = self.surf.get_rect()
    
    def add_message(self, msg):
        if len(self.messages) == CONSOLE_MAX_LINES:
            self.messages.pop(0)  # remove first element
        self.messages.append(msg)

        text = ''
        for line in self.messages:
            text += line + '\n'

        self.surf = self.font.render(text, antialias, color, bgcolor)
        self.rect = self.surf.get_rect(
            bottomleft = (10, 720 - 10)  # TODO: use screen height
        )
    
    def set_fps_text(self, text):
        self.fps_surf = self.font.render(text, antialias, color, bgcolor)
        self.fps_rect = self.fps_surf.get_rect(
            topright = (1280 - 10, 10)  # TODO: use screen width 
        )

    def render(self, screen):
        screen.blit(self.surf, self.rect)
        screen.blit(self.fps_surf, self.fps_rect)