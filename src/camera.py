import pygame

from config import *

class CameraGroup(pygame.sprite.Group):
    ''' YSort and PlayerCenter camera groups from Clear Code tutorials...'''
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_width = self.screen.get_size()[0] // 2
        self.half_height = self.screen.get_size()[1] // 2

        # load background
        self.bg_surf = pygame.image.load('data/background.png').convert_alpha()
        self.bg_surf = pygame.transform.scale_by(self.bg_surf, SCALE_FACTOR)
        self.bg_rect = self.bg_surf.get_rect()

    def draw(self, player):
        # player center camera
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # draw background
        bg_offset = self.bg_rect.topleft - self.offset
        self.screen.blit(self.bg_surf, bg_offset)

        # y-sort draw
        for sprite in sorted(self.sprites(), 
                             key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.screen.blit(sprite.image, offset_pos)
