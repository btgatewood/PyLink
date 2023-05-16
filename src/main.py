import os
import pygame

from config import *
from game import Game

os.environ['SDL_VIDEO_WINDOW_POS'] = '1, 32'  # set window position


# TODO: Fixed time steps, variable rendering.
# TODO: Debug console.

pygame.init()
pygame.display.set_caption('PyLink v0.0.1')
pygame.mouse.set_visible(False)

screen = pygame.display.set_mode((SCREEN_SIZE))
clock = pygame.time.Clock()
running = True

game = Game()  # loads images, requires set display mode first

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:  # is there a better way to check for escape key?
        running = False
    
    game.update()
    
    screen.fill('blue')
    game.render(screen)
    pygame.display.flip()

    clock.tick(120)  # set tick rate

pygame.quit()