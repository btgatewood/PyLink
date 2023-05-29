import math
import pygame

from config import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self, position: pygame.Vector2):
        super().__init__()
        self.image_right = pygame.image.load('data/weapons/weaponR1.png')
        self.image_left = pygame.transform.flip(self.image_right, False, True)

        self.image = self.image_right
        self.rect = self.image.get_rect(center=position)

        self.offset_y = 40            # used for alignment and rotation
        self.rect.y += self.offset_y  # align weapon with player sprite

    def update(self):
        # flip image on y-axis if cursor is left of weapon (screen center)
        if pygame.mouse.get_pos()[0] < SCREEN_CENTER[0]:
            self.image = self.image_left
        else:
            self.image = self.image_right

        # rotate to face cursor (aim at target)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - SCREEN_CENTER[0]
        dy = mouse_y - (SCREEN_CENTER[1] + self.offset_y)
        angle = math.degrees(math.atan2(-dy, dx))

        # rotate using rotozoom() for better filtering of rotated image
        self.rot_image = pygame.transform.rotozoom(self.image, angle, 1.0)
        self.rot_rect = self.rot_image.get_rect(center=self.rect.center)

    def render(self, screen, offset_pos):
        screen.blit(self.rot_image, offset_pos)
