import pygame

from config import *
from player import Player
from weapon import Weapon

class Game:
    # TODO:  Draw and move background.

    def __init__(self):
        # NOTE:  Using 32x32 crosshair image as cursor.
        self.cursor = pygame.image.load('data/crosshair32.png').convert_alpha()

        # set up actors
        screen_center = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.player = Player(screen_center)
        self.weapon = Weapon(screen_center)

        # set up sprite group
        self.sprites = pygame.sprite.Group()
        self.sprites.add([self.player, self.weapon])

    def update(self):
        # for sprite in self.sprites:
        #     sprite.update()
        self.player.update(self.weapon)
        self.weapon.update()
    
    def render(self, screen):
        for sprite in self.sprites:
            sprite.render(screen)

        # draw crosshair  # TODO: resize cursor?
        pos = (pygame.mouse.get_pos()[0] - 16, pygame.mouse.get_pos()[1] - 16)
        screen.blit(self.cursor, pos)
