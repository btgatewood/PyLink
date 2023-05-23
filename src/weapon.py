import math
import pygame

from config import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self, position: pygame.Vector2):
        super().__init__()
        self.image = pygame.image.load('data/weapons/weaponR1.png')
        self.rect = self.image.get_rect(center=position)
        self.offset_y = 40            # used for alignment and rotation
        self.rect.y += self.offset_y  # align weapon with player sprite
        self.flip_y = False           # flag, aiming left if true

    def update(self):
        # flip image on y-axis if cursor is left of weapon (screen center)
        # TODO: save flipped image instead of repeatedly flipping
        if pygame.mouse.get_pos()[0] < SCREEN_CENTER[0]:
            if not self.flip_y:
                self.image = pygame.transform.flip(self.image, False, True)
                self.flip_y = True
        elif self.flip_y:
            self.image = pygame.transform.flip(self.image, False, True)
            self.flip_y = False

        # rotate to face cursor (aim at target)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - SCREEN_CENTER[0]
        dy = mouse_y - (SCREEN_CENTER[1] + self.offset_y)
        angle = math.degrees(math.atan2(-dy, dx))
        # using rotozoom for better filtering of rotated image
        self.rot_image = pygame.transform.rotozoom(self.image, angle, 1.0)
        self.rot_rect = self.rot_image.get_rect(center=self.rect.center)

    def render(self, screen, offset_pos):
        screen.blit(self.rot_image, offset_pos)

        # offset_rect = self.rot_rect.copy()
        # offset_rect.topleft = offset_pos
        # pygame.draw.rect(screen, 'red', offset_rect, 4)

        # NOTE: failed attempt to add color to the weapon
        # surf = self.rot_image.copy()
        # surf.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)  # fill black?
        # surf.fill((255, 128, 0, 0), None, pygame.BLEND_RGBA_ADD) # tint orange?
        # screen.blit(surf, offset_pos)
