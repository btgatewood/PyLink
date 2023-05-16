import pygame

from config import *

def flip_image_x(image):  # flip image on the x-axis
    return pygame.transform.flip(image, True, False)

class Weapon(pygame.sprite.Sprite):
    def __init__(self, position: pygame.Vector2):
        super().__init__()
        # TODO: load animations if we need them
        self.image = pygame.image.load('data/weaponR2.png')
        self.rect = self.image.get_rect(center=position)
        self.rect.y += 48       # align weapon with player sprite
        self.flipped = False    # flag, facing left if true

    def update(self):
        # flip image based on mouse pos
        if pygame.mouse.get_pos()[0] < self.rect.centerx:
            if not self.flipped:
                self.image = flip_image_x(self.image)
                self.flipped = True
        elif self.flipped:
            self.image = flip_image_x(self.image)
            self.flipped = False

        # TODO: rotate to face cursor (aim at target)

    def render(self, screen):
        screen.blit(self.image, self.rect)