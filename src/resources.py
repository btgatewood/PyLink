import json

import pygame

SCALE_FACTOR = 3  # 16x16 -> 48x48  (96x64 * 3 for character sprites)

class Animation:
    def __init__(self, name):
        self.name = name
        self.frames = []
    
    def add_frame(self, frame):
        self.frames.append(frame)


def load_animation_data():
    spritesheet = pygame.image.load('data/character_anim.png').convert_alpha()
    animations = []

    with open('data/character_anim.json') as infile:
        data = json.load(infile)
        animation = None
        for key in data['frames'].keys():
            anim_name = ''
            frame_num = ''
            for ch in key:
                if not ch.isdigit():
                    anim_name += ch
                else:
                    frame_num += ch

            if animation == None:
                animation = Animation(anim_name)
            elif animation.name != anim_name:
                animations.append(animation)
                animation = Animation(anim_name)
            
            frame_size = (data['frames'][key]['sourceSize']['w'],
                          data['frames'][key]['sourceSize']['h'])
            frame = pygame.Surface(frame_size)
            frame_rect = data['frames'][key]['frame']
            area = (frame_rect['x'], frame_rect['y'],
                    frame_rect['w'], frame_rect['h'])
            frame.blit(spritesheet, (0,0), area)
            frame = pygame.transform.scale_by(frame, SCALE_FACTOR)
            animation.add_frame(frame)

    for anim in animations:
        print(anim.name + ', ' + str(len(anim.frames)))
