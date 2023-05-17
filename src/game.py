import pygame

from config import *
from player import Player
from weapon import Weapon

class Game:
    # TODO:  Draw and move background.

    def __init__(self):
        self.background = pygame.image.load('data/background.png').convert()

        # set up actors (sprites)
        # TODO: Start at (1000, 1000)
        screen_center_pos = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.player = Player(screen_center_pos)
        self.weapon = Weapon(screen_center_pos)

        self.cursor = pygame.image.load('data/crosshair32.png').convert_alpha()

    def update(self):
        self.player.update(self.weapon)
        self.weapon.update()
    
    def render(self, screen):
        # TODO: STUDY THIS CODE!!!
        # TODO: What is the offset value?
        offset = pygame.math.Vector2()
        offset.x = self.player.rect.centerx - (SCREEN_WIDTH / 2)
        offset.y = self.player.rect.centery - (SCREEN_HEIGHT / 2)
        print(offset)

        background_offset_pos = self.background.get_rect().topleft - offset
        screen.blit(self.background, background_offset_pos)

        offset_pos = self.player.rect.topleft - offset
        self.player.render(screen, offset_pos)
        self.weapon.render(screen)

        # TODO: Tint crosshair.
        screen.blit(self.cursor, 
                    self.cursor.get_rect(topleft=pygame.mouse.get_pos()))
