import pygame

from camera import CameraGroup
from config import *
from debug import console
from player import Player


class Trees(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('data/spr_deco_tree_01_strip4.png')
        self.image = self.image.convert_alpha()
        self.image = pygame.transform.scale_by(self.image, SCALE_FACTOR)
        self.rect = self.image.get_rect(center = SCREEN_CENTER)
        self.rect.x -= 50
        self.rect.y += 200


class ClearviewFarmGame:
    def __init__(self):
        super().__init__()
        console.add_message('Clearview Farm v0.1')
        self.screen = pygame.display.get_surface()

        # load sprites & groups
        self.sprites = CameraGroup()
        self.player = Player()
        self.sprites.add(self.player)
        self.sprites.add(Trees())

    def update(self, delta_time):
        self.sprites.update(delta_time)

    def render(self):
        self.sprites.draw(self.player)  # NOTE: Camera uses player pos.


if __name__ == '__main__':  # hack for vscode
    import main