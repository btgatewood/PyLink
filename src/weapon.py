import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, position: pygame.Vector2):
        super().__init__()
        self.image = pygame.image.load('data/')

        # TODO: load animations if we need them
