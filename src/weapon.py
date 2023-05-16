import math
import pygame

from config import *

def flip_image_x(image):  # flip image on the y-axis
    return pygame.transform.flip(image, True, False)

def flip_image_y(image):  # flip image on the y-axis
    return pygame.transform.flip(image, False, True)

class Weapon(pygame.sprite.Sprite):
    def __init__(self, position: pygame.Vector2):
        super().__init__()
        # TODO: load animations if we need them
        self.image = pygame.image.load('data/weaponR3.png')
        self.rect = self.image.get_rect(center=position)
        self.rect.y += 40   # align weapon with player sprite
        self.flip_y = False # flag, aiming left if true

    def update(self):
        # flip image on y-axis if cursor is left of weapon
        if pygame.mouse.get_pos()[0] < self.rect.centerx:
            if not self.flip_y:
                self.image = flip_image_y(self.image)
                self.flip_y = True
        elif self.flip_y:
            self.image = flip_image_y(self.image)
            self.flip_y = False

        # rotate to face cursor (aim at target)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.rect.centerx
        dy = mouse_y - self.rect.centery
        angle = math.degrees(math.atan2(-dy, dx))
        self.rotated_image = pygame.transform.rotate(self.image, angle)
        self.rotated_rect = self.rotated_image.get_rect(center=self.rect.center)

    def render(self, screen):
        screen.blit(self.rotated_image, self.rotated_rect)
        # draw hitbox
        pygame.draw.rect(screen, 'orange', self.rect, 4)
        pygame.draw.rect(screen, 'yellow', self.rotated_rect, 4)