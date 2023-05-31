import pygame

MAX_LINES = 8

# setup pygame.font.render() args
antialias = True
color = 'white'
bgcolor = 'black'  # can be used for optimization
wraplength = 0     # max width (in pixels) before wrapping to new line

class Console:
    def __init__(self):
        self.font = pygame.font.Font(None, 24)  # TODO: use custom font
        self.messages = []
        self.surf = None
        self.rect = None
        self.fps_surf = None
        self.fps_rect = None
    
    def add_message(self, msg):
        if len(self.messages) == MAX_LINES:
            self.messages.pop(0)  # remove first element
        self.messages.append(msg)

        text = ''
        for line in self.messages:
            text += line + '\n'

        self.surf = self.font.render(text, antialias, color)
        self.rect = self.surf.get_rect(topleft = (10,10))
    
    def set_fps_text(self, text):
        self.fps_surf = self.font.render(text, antialias, color)
        self.fps_rect = self.fps_surf.get_rect(
            topright = (1280 - 10, 10))  # TODO: use screen width

    def render(self, screen):
        screen.blit(self.surf, self.rect)
        if self.fps_surf != None:
            screen.blit(self.fps_surf, self.fps_rect)