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

        # setup anim data
        self.anim_dict = load_graphics()
        self.anim = self.anim_dict['walk']
        self.frame = 0
        self.frame_timer = 0
        self.frame_duration = 0.075  # in seconds (75 ms per frame)

        # setup sprite data
        self.image = self.anim[self.frame]
        self.rect = self.image.get_rect(center = SCREEN_CENTER)

        # movement
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)
        self.speed = 250  # pixels per second  # TODO: Use config var.
    
    def update(self, delta_time):
        # input
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
        
        # normalizing a vector 
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # NOTE: Why do we separate movement for each axis?
		# horizontal movement
        self.position.x += self.direction.x * self.speed * delta_time
        self.rect.centerx = round(self.position.x)

		# vertical movement
        self.position.y += self.direction.y * self.speed * delta_time
        self.rect.centery = round(self.position.y)

        # update animation
        self.frame_timer += delta_time
        if self.frame_timer >= self.frame_duration:
            self.frame_timer -= self.frame_duration
            self.frame += 1
        if self.frame == len(self.anim):
            self.frame = 0
        self.image = self.anim[self.frame]
