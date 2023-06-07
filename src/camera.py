import pygame

class YSortCameraGroup(pygame.sprite.Group):
    ''' Sorts sprites based on y-position with lower y-positions (higher
        vertical positions) being drawn behind (before) others.  '''
    def __init__(self):
        super().__init__()