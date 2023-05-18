import pygame

from anim import Animation
from config import *


player_anim_data = [  
    # (anim_name, num_frames)
    ('death', 10),
    ('fall', 5),
    ('hit', 3),
    ('idle', 6),
    ('jumpEnd', 3),
    ('jumpStart', 2),
    ('roll', 5),
    ('walk', 8)
]

class Player(pygame.sprite.Sprite):
    def __init__(self, position: pygame.Vector2):
        super().__init__()

        # load images
        self.animations = {}
        for data in player_anim_data:
            self.animations[data[0]] = Animation(data[0], data[1])
        self.anim = self.animations['idle']
        
        # setup pygame sprite properties
        self.image = self.anim.get_frame()
        self.rect = self.image.get_rect(center=position)
        
        # set up physics-related data
        self.hitbox = self.rect.inflate(-192,-160)
        self.hitbox.y += 48
        self.dx = 0
        self.dy = 0
    
    def input(self):
        keys = pygame.key.get_pressed()

        # horizontal movement
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.dx = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.dx = 1
        else:
            self.dx = 0
        
        # vertical movement
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.dy = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.dy = 1
        else:
            self.dy = 0

    def update(self, weapon):
        self.input()

        # set animation & update current frame
        if self.dx == 0 and self.dy == 0:
            self.anim = self.animations['idle']
        else:
            self.anim = self.animations['walk']
        self.anim.update()

        # movement
        self.dx *= PLAYER_SPEED
        self.dy *= PLAYER_SPEED
        self.hitbox.x += self.dx
        self.hitbox.y += self.dy
        self.rect.center = self.hitbox.midtop

        # move weapon
        weapon.rect.x += self.dx
        weapon.rect.y += self.dy

        # flip image based on mouse's screen position
        if pygame.mouse.get_pos()[0] < SCREEN_CENTER[0]:
            self.image = pygame.transform.flip(
                self.anim.get_frame(), True, False)
        else:
            self.image = self.anim.get_frame()
    
    def _draw_rect_offset(self, screen, rect, offset, color='black', width=2):
        tmp_rect = rect.copy()
        tmp_rect.topleft = tmp_rect.topleft - offset
        pygame.draw.rect(screen, color, tmp_rect, width)

    def render(self, screen, offset_pos):
        screen.blit(self.image, offset_pos)

        offset = pygame.math.Vector2()
        offset.x = self.rect.centerx - SCREEN_CENTER[0]
        offset.y = self.rect.centery - SCREEN_CENTER[1]

        # apply offset then draw player hitbox, image rect
        self._draw_rect_offset(screen, self.hitbox, offset, 'red', 4)
        self._draw_rect_offset(screen, self.rect, offset) # use default params
        