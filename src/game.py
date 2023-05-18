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
        screen_center_pos = pygame.Vector2(SCREEN_CENTER)
        self.player = Player(screen_center_pos)
        self.weapon = Weapon(screen_center_pos)

        self.cursor = pygame.image.load('data/crosshair32.png').convert_alpha()

    def update(self):
        self.player.update(self.weapon)
        self.weapon.update()
    
    def render(self, screen):
        # TODO: Study. This. Code!  What IS the offset value?!
        # NOTE: The offset is the player's distance from the screen's center.
        offset = pygame.math.Vector2()
        offset.x = self.player.rect.centerx - SCREEN_CENTER[0]
        offset.y = self.player.rect.centery - SCREEN_CENTER[1]

        background_offset_pos = self.background.get_rect().topleft - offset
        screen.blit(self.background, background_offset_pos)

        offset_pos = self.player.rect.topleft - offset
        self.player.render(screen, offset_pos)
        offset_pos = self.weapon.rot_rect.topleft - offset
        self.weapon.render(screen, offset_pos)

        # NOTE: Tints crosshair. Is this how to tint the base white textures?
        surf = self.cursor.copy()
        surf.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
        # surf.fill((255, 0, 0, 0), None, pygame.BLEND_RGBA_ADD)
        screen.blit(surf, self.cursor.get_rect(topleft=pygame.mouse.get_pos()))
