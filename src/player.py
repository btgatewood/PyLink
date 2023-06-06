import pygame

from config import *
from data import load_character_anim_data, load_twf_character_data


class Player(pygame.sprite.Sprite):
    def __init__(self, console):
        super().__init__()

        # movement
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(SCREEN_CENTER)
        self.speed = PLAYER_SPEED

        # setup graphics and anim data
        # self.anim_frames = load_character_anim_data()
        self.anim_frames = load_twf_character_data()
        self.anim = self.anim_frames['idle']  # NOTE: Change animation.
        self.frame = 0                        # NOTE: Reset animation.
        self.frame_timer = 0
        self.frame_duration = 0.075  # in seconds (75 ms per frame)

        # setup sprite data
        self.image = self.anim[self.frame]
        self.rect = self.image.get_rect(center = SCREEN_CENTER)
    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
    
    def move(self, dt):
        # normalize direction for const speed with diagonal movement
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

		# horizontal & vertical movement
        self.position.x += self.direction.x * self.speed * dt
        self.rect.centerx = round(self.position.x)
        self.position.y += self.direction.y * self.speed * dt
        self.rect.centery = round(self.position.y)

    def update(self, delta_time):
        self.input()
        self.move(delta_time)

        # animate
        self.frame_timer += delta_time
        if self.frame_timer >= self.frame_duration:
            self.frame_timer -= self.frame_duration
            self.frame += 1
        if self.frame == len(self.anim):
            self.frame = 0
        self.image = self.anim[self.frame]
