import pygame

from config import *
from console import Console
from player import Player

class ClearviewFarmGame:
    def __init__(self, console: Console):
        super().__init__()
        self.console = console
        self.console.add_message('Clearview Farm v0.1')
        self.screen = pygame.display.get_surface()

        # load background
        # TODO: util function to load images -> resource manager
        self.bg_surf = pygame.image.load('data/background.png').convert_alpha()
        self.bg_surf = pygame.transform.scale_by(self.bg_surf, SCALE_FACTOR)
        self.bg_rect = self.bg_surf.get_rect()

        # TODO: implement camera

        # load sprites & groups
        self.player = Player(console)
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)

    def update(self, delta_time):
        self.sprites.update(delta_time)

    def render(self):
        self.screen.blit(self.bg_surf, self.bg_rect)
        self.sprites.draw(self.screen)


if __name__ == '__main__':  # hack for vscode
    import main