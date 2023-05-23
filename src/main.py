import os
import pygame

from config import *
from game import Game

os.environ['SDL_VIDEO_WINDOW_POS'] = '1, 32'  # set window position

pygame.init()

""" begin debug.py """
font = pygame.font.Font(None, 30)

def debug(info, y = 10, x = 10):
    debug_surf = font.render(str(info), True, 'White')  # render text to surf
    debug_rect = debug_surf.get_rect(topleft = (x,y))   # get text rect
    bg_rect = debug_rect.inflate(8, 8)
    bg_rect.topleft = (x - 4, y - 6)                    # why 6? idk.
    display_surf = pygame.display.get_surface()         # get screen
    pygame.draw.rect(display_surf, 'Black', bg_rect)    # draw background rect
    display_surf.blit(debug_surf, debug_rect)           # draw text to screen
""" end debug.py """

pygame.display.set_caption('PyLink v0.0.1')
pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((SCREEN_SIZE))
clock = pygame.time.Clock()
running = True

game = Game()  # loads images, requires display mode set

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:  # should we quit on escape key press in main?
        running = False
    
    game.update()
    
    screen.fill('black')
    game.render(screen)
    debug('PyLink v0.0.1\nHello, World!')
    pygame.display.flip()

    clock.tick(FPS)  # set tick rate

pygame.quit()