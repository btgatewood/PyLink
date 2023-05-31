import pygame

MAX_LINES = 16

# setup pygame.font.render() args
antialias = True
color = 'white'
bgcolor = 'black'  # used for optimization
wraplength = 0  # max width (in pixels) before wrapping to new line

class Console:
    def __init__(self):
        self.font = pygame.font.Font(None, 24)
        self.lines = []
        self.text = None
        self.surf = None
        self.rect = None
    
    def add_text(self, msg):  # add message to console
        if len(self.lines) == MAX_LINES:
            self.lines.pop(0)  # remove first element
        self.lines.append(msg)

        self.text = ''
        for line in self.lines:
            self.text += line + '\n'

        self.surf = self.font.render(self.text, antialias, color)
        self.rect = self.surf.get_rect(topleft = (10,10))
    
    def draw_text(self, screen):
        screen.blit(self.surf, self.rect)