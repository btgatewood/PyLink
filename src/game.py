import pygame

from camera import YSortCameraGroup
from config import *
from console import Console
from player import Player

class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/spr_deco_tree_01_strip4.png')
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale_by(self.image, SCALE_FACTOR)
        self.rect = self.image.get_rect(center = SCREEN_CENTER)


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

        # load sprites & groups
        self.sprites = YSortCameraGroup()
        self.player = Player(console)
        self.sprites.add(self.player)
        self.sprites.add(Tree())

    def update(self, delta_time):
        self.sprites.update(delta_time)

    def render(self):
        self.screen.blit(self.bg_surf, self.bg_rect)
        self.sprites.draw(self.screen)


if __name__ == '__main__':  # hack for vscode
    import main