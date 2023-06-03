import pygame

SCREEN_CENTER = (1280 // 2, 720 // 2)  # hack, TODO: use constants
SCALE_FACTOR = 3  # 16x16 -> 48x48  (96x64 * 3 for character sprites)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # load animation frames
        NUM_FRAMES = 8
        spritesheet = pygame.image.load('data/player_walk.png').convert_alpha()
        self.frames: pygame.Surface = []
        for i in range(NUM_FRAMES):
            frame = pygame.Surface((96,64))
            frame.blit(spritesheet, (0,0), (80 * i, 0, 80, 64))
            frame = pygame.transform.scale_by(frame, SCALE_FACTOR)
            self.frames.append(frame)
        
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
