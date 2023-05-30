import pygame

# setup pygame.font.render() args
antialias = True
color = 'white'
bgcolor = 'black'
wraplength = 0  # max width (in pixels) before wrapping to new line

class Console:
    def __init__(self):
        self.font = pygame.font.Font(None, 24)
        self.text = None
        self.surf = None
        self.rect = None
    
    def add_text(self, msg):  # add message to console
        if self.text == None:
            self.text = msg
        else:
            self.text += '\n' + msg
        self.surf = self.font.render(self.text, antialias, color)
        self.rect = self.surf.get_rect(topleft = (10,10))
    
    def draw_text(self, screen):
        screen.blit(self.surf, self.rect)