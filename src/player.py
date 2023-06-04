import json

import pygame

SCREEN_CENTER = (1280 // 2, 720 // 2)  # NOTE: hack, TODO: use constants
SCALE_FACTOR = 3  # 16x16 -> 48x48  (96x64 * 3 for character sprites)
SPRITE_WIDTH = 80
SPRITE_HEIGHT = 64


def load_graphics():
    spritesheet = pygame.image.load('data/character_anim.png').convert_alpha()
    anim_dict = {}  # keys = anim name, values = lists of frames

    with open('data/character_anim.json') as infile:
        data = json.load(infile)
        for key in data['frames'].keys():
            anim_name = ''  # key for anim_dict
            i = 0
            while key[i].isalpha():
                anim_name += key[i]
                i += 1

            if anim_name not in anim_dict:
                anim_dict[anim_name] = []
            
            frame_size = (data['frames'][key]['sourceSize']['w'],
                          data['frames'][key]['sourceSize']['h'])
            frame = pygame.Surface(frame_size)
            frame_rect = data['frames'][key]['frame']
            area = (frame_rect['x'], frame_rect['y'],
                    frame_rect['w'], frame_rect['h'])
            frame.blit(spritesheet, (0,0), area)
            frame = pygame.transform.scale_by(frame, SCALE_FACTOR)
            anim_dict[anim_name].append(frame)

    for k, v in anim_dict.items():
        print(k + ', ' + str(len(v)))
    
    return anim_dict


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.anim_dict = load_graphics()
       
        # setup anim data
        self.anim = self.anim_dict['attack']
        self.frame = 0
        self.frame_timer = 0
        self.frame_duration = 75  # milliseconds

        # setup sprite data
        self.image = self.anim[self.frame]
        self.rect = self.image.get_rect(center = SCREEN_CENTER)

        # TODO: Draw image and hitbox rects for testing.
    
    def update(self, delta_time):
        self.frame_timer += delta_time
        if self.frame_timer >= self.frame_duration:
            self.frame_timer -= self.frame_duration
            self.frame += 1
        if self.frame == len(self.anim):
            self.frame = 0
        self.image = self.anim[self.frame]
