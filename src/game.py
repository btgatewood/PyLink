import pygame

from config import *
from player import Player

class Game:
    # TODO:  Draw and move background.
    # TODO:  Draw and animate weapon.

    def __init__(self):
        # TODO: 24 or 32px crosshair?
        self.cursor = pygame.image.load('data/crosshair32.png').convert_alpha()

        # PLAYER_HALF_SIZE = 128
        pos = pygame.Vector2(SCREEN_WIDTH / 2 - 128, SCREEN_HEIGHT / 2 - 192)
        self.player = Player(pos)

        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)

    def update(self):
        self.player.update()
    
    def render(self, screen):
        self.player.render(screen)

        # draw crosshair  # TODO: resize cursor, hide windows cursor
        pos = (pygame.mouse.get_pos()[0] - 16, pygame.mouse.get_pos()[1] - 16)
        screen.blit(self.cursor, pos)
