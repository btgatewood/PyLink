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

        self.surf = self.font.render(text, antialias, color)
        
        # create transparent, inflated background
        self.bg_rect = self.surf.get_rect()
        self.bg_rect.inflate_ip(16, 16)
        self.bg_surf = pygame.surface.Surface(self.bg_rect.size).convert_alpha()
        self.bg_surf.fill((0, 0, 0, 128))
        self.bg_rect.bottomleft = (16, SCREEN_HEIGHT - 16)

        self.rect = self.surf.get_rect(center = self.bg_rect.center)

    def set_fps_text(self, text):
        self.fps_surf = self.font.render(text, antialias, color)
        self.fps_rect = self.fps_surf.get_rect(
            topright = (1280 - 10, 10)  # TODO: use screen width 
        )

    def render(self, screen):
        screen.blit(self.bg_surf, self.bg_rect)
        screen.blit(self.surf, self.rect)
        screen.blit(self.fps_surf, self.fps_rect)