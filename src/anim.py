import pygame

class Animation:
    def __init__(self, anim_name, num_frames):
        # load images
        self.frames = []                            # surface list
        for i in range(num_frames):
            file = f'data/player/{anim_name}_{i}.png'
            surface = pygame.image.load(file).convert_alpha()
            self.frames.append(surface)
            print('loaded image: ' + file)
        
        # setup animation
        self.prev_time = pygame.time.get_ticks()    # get time in milliseconds
        self.ms_per_frame = 100                     # animation speed
        self.frame_index = 0                        # current frame

    def update(self):
        # update animation
        if (pygame.time.get_ticks() - self.prev_time) > self.ms_per_frame:
            if self.frame_index < len(self.frames) - 1:
                self.frame_index += 1
            else:
                self.frame_index = 0
            # prev_time -= ms_per_frame             # NOTE: interesting bug?
            self.prev_time = pygame.time.get_ticks()
    
    def get_frame(self):
        return self.frames[self.frame_index]


"""
class TestPlayerAnimations:  # use this class as Game object in main
    
    anim_data = [  # how do static class members work in python?
        # ('anim_name', num_frames)
        ('death', 10),
        ('fall', 5),
        ('hit', 3),
        ('idle', 6),
        # ('jumpEnd', 3),
        # ('jumpStart', 2),
        ('roll', 5),
        ('walk', 8)
    ]

    def __init__(self):
        self.animations = []
        y = 0
        for data in self.anim_data:
            self.animations.append(Animation(data[1], data[0], (0, y)))
            y += 128
    
    def update(self):
        for anim in self.animations:
            anim.update()
    
    def render(self, screen):
        for anim in self.animations:
            anim.render(screen)
"""