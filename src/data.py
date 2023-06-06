import json

import pygame

from config import *


def load_character_anim_data():
    ''' Parses the json data generated by aseprite and returns a dict of 
        animations with lists of frames (surfaces) loaded from the spritesheet.
    '''
    spritesheet = pygame.image.load('data/character_anim.png').convert_alpha()
    gfx_data = {}  # keys = anim name, values = lists of pygame.Surface() objs

    with open('data/character_anim.json') as infile:
        json_data = json.load(infile)
        for key in json_data['frames'].keys():
            anim_name = ''  # key for anim_dict
            i = 0
            while key[i].isalpha():
                anim_name += key[i]
                i += 1

            if anim_name not in gfx_data:
                gfx_data[anim_name] = []
            
            frame_size = (json_data['frames'][key]['sourceSize']['w'],
                          json_data['frames'][key]['sourceSize']['h'])
            frame = pygame.Surface(frame_size)
            frame.set_colorkey((0,0,0))
            frame_data = json_data['frames'][key]['frame']
            area = (frame_data['x'], frame_data['y'],
                    frame_data['w'], frame_data['h'])
            frame.blit(spritesheet, (0,0), area)
            frame = pygame.transform.scale_by(frame, SCALE_FACTOR)
            gfx_data[anim_name].append(frame)

    for key, value in gfx_data.items():
        print(key + ', ' + str(len(value)))
    
    return gfx_data

def load_twf_character_data():
    spritesheet = pygame.image.load('data/walk and idle.png').convert_alpha()
    anim_dict = {'idle': [],
                 'left': [],
                 'right': [] }  # TODO: Make values lists of frame surfaces.
    
    sz_t = 24  # tile size, anim frames are 24x24
    idle1 = pygame.Rect((sz_t * 0,0), (sz_t,sz_t))
    idle2 = pygame.Rect((sz_t * 1,0), (sz_t,sz_t))
    idle3 = pygame.Rect((sz_t * 2,0), (sz_t,sz_t))
    idle4 = pygame.Rect((sz_t * 3,0), (sz_t,sz_t))

    # load idle animation
    for i in range(4):
        frame = pygame.Surface((sz_t,sz_t))
        frame_area = pygame.Rect((sz_t * i, 0), (sz_t,sz_t))
        frame.blit(spritesheet, (0,0), frame_area)
        frame = pygame.transform.scale_by(frame, SCALE_FACTOR)
        anim_dict['idle'].append(frame)
    
    return anim_dict