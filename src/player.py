import json

import pygame

from config import *
from debug import console

def load_character_anim_data():
    ''' Parses the json data generated by aseprite and returns a dict of 
        anim data with lists of frame surfs loaded from the spritesheet. '''
    spritesheet = pygame.image.load('data/character_anim.png').convert_alpha()
    anim_dict = {}  # key = anim name, value = list of pygame.Surface() objects

    with open('data/character_anim.json') as infile:
        json_data = json.load(infile)
        for key in json_data['frames'].keys():
            anim_name = ''  # key for anim_dict
            i = 0
            while key[i].isalpha():
                anim_name += key[i]
                i += 1

            if anim_name not in anim_dict:
                anim_dict[anim_name] = []
            
            frame_size = (json_data['frames'][key]['sourceSize']['w'],
                          json_data['frames'][key]['sourceSize']['h'])
            frame = pygame.Surface(frame_size, pygame.SRCALPHA)
            frame_data = json_data['frames'][key]['frame']
            area = (frame_data['x'], frame_data['y'],
                    frame_data['w'], frame_data['h'])
            frame.blit(spritesheet, (0,0), area)
            frame = pygame.transform.scale_by(frame, SCALE_FACTOR)
            anim_dict[anim_name].append(frame)
    
    console.add_message('Loaded extra player animations: ')
    # msg = ''
    # for anim in anim_dict.keys():
    #     msg += anim + ', '
    console.add_message(''.join(f'{anim}, ' for anim in anim_dict.keys() 
                                if anim != 'walk' and anim != 'idle'))

    return anim_dict


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # movement
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(SCREEN_CENTER)
        self.speed = PLAYER_SPEED

        # setup graphics and anim data
        self.anim_db = load_character_anim_data()  # get dict of anim frames
        self.flip_x = False                        # true if facing left
        self.state = 'idle' 
        self.frame_index = 0                        
        self.frame_timer = 0
        self.frame_duration = 0.075  # in seconds (75 ms per frame)

        # setup sprite data
        self.image = self.anim_db[self.state][self.frame_index]
        self.rect = self.image.get_rect(center = SCREEN_CENTER)
    
    def update(self, delta_time):
        self.input()

        # hack
        if self.state == 'attack':
            self.animate(delta_time)
            return

        # update player state
        if self.direction.magnitude() == 0:
            self.update_state('idle')
        else: # magnitude > 0
            self.update_state('walk')
            self.move(delta_time)

        self.animate(delta_time)
    
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
            if not self.flip_x:
                self.flip_x = True  # flip animation
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            if self.flip_x:
                self.flip_x = False  # re-flip animation
        else:
            self.direction.x = 0
        
        # attack
        if keys[pygame.K_SPACE]:
            self.update_state('attack')
    
    def update_state(self, state):
        if self.state != state:
            self.state = state
            self.frame_index = 0
    
    def move(self, dt):
        # normalize direction for const speed with diagonal movement
        # if self.direction.magnitude() > 0:
        self.direction = self.direction.normalize()

		# horizontal & vertical movement
        self.position.x += self.direction.x * self.speed * dt
        self.rect.centerx = round(self.position.x)
        self.position.y += self.direction.y * self.speed * dt
        self.rect.centery = round(self.position.y)
    
    def animate(self, dt):
        self.frame_timer += dt
        if self.frame_timer >= self.frame_duration:
            self.frame_index += 1
            self.frame_timer -= self.frame_duration
        if self.frame_index >= len(self.anim_db[self.state]):
            # hack
            if self.state != 'idle':
                self.state = 'idle'
            self.frame_index = 0
        
        # flip image
        self.image = pygame.transform.flip(
            self.anim_db[self.state][self.frame_index], self.flip_x, False)
        