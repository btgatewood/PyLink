import pygame

from config import *
from player import Player
from weapon import Weapon

class Game:
    # TODO:  Draw and move background.
    # TODO:  Draw and animate weapon.

    def __init__(self):
        # NOTE:  Using 32x32 crosshair image as cursor.
        self.cursor = pygame.image.load('data/crosshair32.png').convert_alpha()

        pos = pygame.Vector2(SCREEN_WIDTH / 2 - PLAYER_HALF_SIZE, 
                                    SCREEN_HEIGHT / 2 - PLAYER_HALF_SIZE * 1.5)
        self.player = Player(pos)
        self.weapon = Weapon(pos)

        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)

    def update(self):
        self.player.update()
        self.weapon.update()
    
    def render(self, screen):
        self.player.render(screen)
        self.weapon.render(screen)

        # draw crosshair  # TODO: resize cursor, hide windows cursor
        pos = (pygame.mouse.get_pos()[0] - 16, pygame.mouse.get_pos()[1] - 16)
        screen.blit(self.cursor, pos)
