import pygame

from config import *

# TODO: Use custom font.

# setup pygame.font.render() args
antialias = True
color = 'white'
bgcolor = None                  # can be used for optimization
wraplength = SCREEN_WIDTH // 3  # max width (in pixels) before wrapping to new line

class Console:
    def __init__(self):
        self.font = pygame.font.Font(None, 24)  # TODO: use custom font
        self.messages = []
        # TODO: set timers for message lifespans & fade out
        self.surf = pygame.surface.Surface((0,0))
        self.rect = self.surf.get_rect()
        # self.fps_text = '0hz 0fps'
        self.fps_surf = pygame.surface.Surface((0,0))
        self.fps_rect = self.surf.get_rect()
        self.fps_bg_surf = pygame.surface.Surface((0,0))
        self.fps_bg_rect = self.surf.get_rect()
    
    def add_message(self, msg):
        if len(self.messages) == CONSOLE_MAX_LINES:
            self.messages.pop(0)  # remove first element
        self.messages.append(msg)

        text = ''
        for line in self.messages:
            text += line + '\n'

        self.surf = self.font.render(text, antialias, color, 
                                     bgcolor, wraplength).convert_alpha()
        
        # create transparent, inflated background  # TODO: Refactor.
        self.bg_rect = self.surf.get_rect()
        self.bg_rect.inflate_ip(16, 16)
        self.bg_surf = pygame.surface.Surface(self.bg_rect.size).convert_alpha()
        self.bg_surf.fill((0, 0, 0, 128))
        self.bg_rect.bottomleft = (8, SCREEN_HEIGHT - 8)

        self.rect = self.surf.get_rect(center = self.bg_rect.center)

    def set_fps_text(self, text):
        # self.fps_text = text
        self.fps_surf = self.font.render(text, antialias, color, 
                                         bgcolor).convert_alpha()
        
        # create transparent, inflated background  # TODO: Refactor.
        self.fps_bg_rect = self.fps_surf.get_rect()
        self.fps_bg_rect.inflate_ip(8, 8)
        self.fps_bg_surf = pygame.surface.Surface(self.fps_bg_rect.size).convert_alpha()
        self.fps_bg_surf.fill((0, 0, 0, 128))
        self.fps_bg_rect.topright = (SCREEN_WIDTH - 4, 4)

        self.fps_rect = self.fps_surf.get_rect(center = self.fps_bg_rect.center)
    
    def render(self, screen: pygame.Surface):
        screen.blit(self.bg_surf, self.bg_rect)
        screen.blit(self.surf, self.rect)
        screen.blit(self.fps_bg_surf, self.fps_bg_rect)
        screen.blit(self.fps_surf, self.fps_rect)

    
    ''' This method inverted the color of the fps text based on the current
            screen but the visual result wasn't very appealing. '''
    # def render_fps_text(self, screen):
    #     # NOTE: second attempt at inverted fps text
    #     self.fps_surf = self.font.render(
    #         self.fps_text, antialias, (255,255,255,255)).convert_alpha()
    #     self.fps_rect = self.fps_surf.get_rect(
    #         topright = (SCREEN_WIDTH - 10, 10))
    #     self.fps_surf.blit(screen, (0,0), self.fps_rect, pygame.BLEND_RGB_SUB)
    #     screen.blit(self.fps_surf, self.fps_rect)