import pygame

from config import *
from player import Player
from weapon import Weapon

def init_background_surface():
    """ Draws a grid or "prototype texture" with alternating tiles. """
    map_size = 1280                 # grid, surf, bg size
    tile_size = 64                  # cell, rect size
    WHITE = pygame.Color('white')   # color 1
    GREY = pygame.Color('gray')     # color 2

    bg_surf = pygame.Surface((map_size, map_size))  # 1280 = 64 * 20
    for x in range(0, map_size, tile_size):
        for y in range(0, map_size, tile_size):
            rect = pygame.Rect(x, y, tile_size, tile_size)
            if (x // tile_size) % 2 == 0:
                if (y // tile_size) % 2:
                    pygame.draw.rect(bg_surf, GREY, rect)
                else:
                    pygame.draw.rect(bg_surf, WHITE, rect)
            else:
                if (y // tile_size) % 2:
                    pygame.draw.rect(bg_surf, WHITE, rect)
                else:
                    pygame.draw.rect(bg_surf, GREY, rect)
    return bg_surf

# TODO: Draw player hands.
# TODO: Adjust render order for player, weapon, & hands.
    # Draw weapon first when player is aiming at top-half of screen.
    # Determine draw order for hands.

class Game:
    def __init__(self):
        self.background = init_background_surface()
        self.cursor = pygame.image.load('data/crosshair32.png').convert_alpha()

        world_center = pygame.Vector2(640, 640)
        self.player = Player(world_center)
        self.weapon = Weapon(world_center)

    def update(self):
        self.player.update(self.weapon)
        self.weapon.update()
    
    def render(self, screen):
        # TODO: move offset and rendering to custom pygame sprite group
        # get the player's current distance from the screen's center
        offset = pygame.math.Vector2()
        offset.x = self.player.rect.centerx - SCREEN_CENTER[0]
        offset.y = self.player.rect.centery - SCREEN_CENTER[1]

        # subtract offset from each sprite's position to get render position
        offset_pos = self.background.get_rect().topleft - offset
        screen.blit(self.background, offset_pos)

        offset_pos = self.player.rect.topleft - offset
        self.player.render(screen, offset_pos)

        offset_pos = self.weapon.rot_rect.topleft - offset
        self.weapon.render(screen, offset_pos)

        # tint crosshair sprite
        surf = self.cursor.copy()
        surf.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)  # fill black?
        surf.fill((255, 0, 0, 0), None, pygame.BLEND_RGBA_ADD)   # tint red?
        screen.blit(surf, self.cursor.get_rect(topleft=pygame.mouse.get_pos()))


"""
class TestPlayerAnimations:  # use this class as Game object in main
    
    anim_data = [  # how do static class members work in python?
        # ('anim_name', num_frames)
        ('death', 10),
        ('fall', 5),
        ('hit', 3),
        ('idle', 6),
        # ('jumpEnd', 3),
        # ('jumpStart', 2),
        ('roll', 5),
        ('walk', 8)
    ]

    def __init__(self):
        self.animations = []
        y = 0
        for data in self.anim_data:
            self.animations.append(Animation(data[1], data[0], (0, y)))
            y += 128
    
    def update(self):
        for anim in self.animations:
            anim.update()
    
    def render(self, screen):
        for anim in self.animations:
            anim.render(screen)
"""
