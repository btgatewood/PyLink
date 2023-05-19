import math
import pygame

from config import *


def flip_image_x(image):  # flip image on the x-axis
    return pygame.transform.flip(image, True, False)

def flip_image_y(image):  # flip image on the y-axis
    return pygame.transform.flip(image, False, True)

class Weapon(pygame.sprite.Sprite):
    def __init__(self, position: pygame.Vector2):
        super().__init__()
        # TODO: load animations if we need them
        self.image = pygame.image.load('data/weapons/weaponR1.png')
        self.rect = self.image.get_rect(center=position)
        self.rect.y += 40   # align weapon with player sprite
        self.flip_y = False # flag, aiming left if true

    def update(self):
        # flip image on y-axis if cursor is left of weapon (screen center)
        if pygame.mouse.get_pos()[0] < SCREEN_CENTER[0]:
            if not self.flip_y:
                self.image = flip_image_y(self.image)
                self.flip_y = True
        elif self.flip_y:
            self.image = flip_image_y(self.image)
            self.flip_y = False

        # rotate to face cursor (aim at target)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - SCREEN_CENTER[0]
        dy = mouse_y - SCREEN_CENTER[1]
        angle = math.degrees(math.atan2(-dy, dx))
        # using rotozoom for better rotation filtering
        self.rot_image = pygame.transform.rotozoom(self.image, angle, 1.0)
        self.rot_rect = self.rot_image.get_rect(center=self.rect.center)

    def render(self, screen, offset_pos):
        screen.blit(self.rot_image, offset_pos)