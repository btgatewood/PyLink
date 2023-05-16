import pygame

from config import *

# TODO:  Add weapon member to game or player class.
# TODO:  Render weapon.
# TODO:  Rotate weapon to aim at cursor (target).

def flip_image_x(image):  # unused utility function
    return pygame.transform.flip(image, True, False)

class Weapon(pygame.sprite.Sprite):
    def __init__(self, position: pygame.Vector2):
        super().__init__()
        self.image = pygame.image.load('data/weaponR1.png')
        self.rect = self.image.get_rect(center = position)
        self.flipped = False  # flag for facing left

        # TODO: load animations if we need them

    def update(self):
        # TODO?: flip if cursor is left of screen center (weapon & player position)
        #        - must clamp player (& weapon) to screen center
        # TODO?: self.center_x = self.rect.x + PLAYER_HALF_SIZE
        if pygame.mouse.get_pos()[0] < self.rect.centerx:
            if not self.flipped:
                self.image = pygame.transform.flip(self.image, True, False)
                self.flipped = True
        elif self.flipped:
            self.image = pygame.transform.flip(self.image, True, False)
            self.flipped = False
        # TODO: rotate to face cursor (aim)

    def render(self, screen):
        screen.blit(self.image, self.rect)