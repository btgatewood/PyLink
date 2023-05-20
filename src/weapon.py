import math
import pygame

from config import *


class Weapon(pygame.sprite.Sprite):
    def __init__(self, position: pygame.Vector2):
        super().__init__()
        self.image = pygame.image.load('data/weapons/weaponR1.png')
        self.rect = self.image.get_rect(center=position)
        self.rect.y += 40   # align weapon with player sprite
        self.flip_y = False # flag, aiming left if true

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
        dy = mouse_y - SCREEN_CENTER[1]
        angle = math.degrees(math.atan2(-dy, dx))
        # using rotozoom for better filtering of rotated image
        self.rot_image = pygame.transform.rotozoom(self.image, angle, 1.0)
        self.rot_rect = self.rot_image.get_rect(center=self.rect.center)

    def render(self, screen, offset_pos):
        screen.blit(self.rot_image, offset_pos)