import pygame

from resources import load_animation_data

SCREEN_CENTER = (1280 // 2, 720 // 2)  # NOTE: hack, TODO: use constants
SCALE_FACTOR = 3  # 16x16 -> 48x48  (96x64 * 3 for character sprites)
SPRITE_WIDTH = 80
SPRITE_HEIGHT = 64

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.animations = load_animation_data()  # TODO: Create a dict of anims.
       
        # setup anim data
        self.frame_timer = 0
        self.frame_duration = 75  # milliseconds
        self.current_frame = 0

        self.current_animation = self.animations['attack']

        # setup sprite data
        self.image = self.current_animation[self.current_frame]
        self.rect = self.image.get_rect(center = SCREEN_CENTER)

        # TODO: Draw image and hitbox rects for testing.
    
    def update(self, delta_time):
        self.frame_timer += delta_time
        if self.frame_timer >= self.frame_duration:
            self.frame_timer -= self.frame_duration
        if self.current_frame == len(self.current_animation):
            self.current_frame = 0
        self.image = self.current_animation[self.current_frame]
