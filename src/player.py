import pygame

from resources import load_animation_data

SCREEN_CENTER = (1280 // 2, 720 // 2)  # NOTE: hack, TODO: use constants
SCALE_FACTOR = 3  # 16x16 -> 48x48  (96x64 * 3 for character sprites)
SPRITE_WIDTH = 80
SPRITE_HEIGHT = 64

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # TODO: Load animations from json data.
        self.animations = load_animation_data()

        NUM_WALK_FRAMES = 8
        spritesheet = pygame.image.load('data/character_anim.png').convert_alpha()
        self.frames = []
        for i in range(NUM_WALK_FRAMES):
            frame = pygame.Surface((96,64))
            frame.blit(spritesheet, (0,0), (96 * i, 0, 96, 64))
            frame = pygame.transform.scale_by(frame, SCALE_FACTOR)
            self.frames.append(frame)
        
        # NUM_IDLE_FRAMES = 9
        # self.frames: pygame.Surface = []
        # for i in range(NUM_IDLE_FRAMES):
        #     frame = pygame.Surface((96,64))
        #     frame.blit(spritesheet, (0,0), (96 * i, 64 * 2, 96, 64))  # NOTE: y += 1
        #     frame = pygame.transform.scale_by(frame, SCALE_FACTOR)
        #     self.frames.append(frame)
        
        # setup anim data
        self.frame_timer = 0
        self.frame_duration = 75  # milliseconds
        self.current_frame = 0

        # setup sprite data
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center = SCREEN_CENTER)

        # TODO: Draw image and hitbox rects for testing.
    
    def update(self, delta_time):
        self.frame_timer += delta_time
        if self.frame_timer >= self.frame_duration:
            self.frame_timer -= self.frame_duration
            self.current_frame += 1
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.image = self.frames[self.current_frame]
