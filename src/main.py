import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '1, 32'  # set window position

import time
import pygame
pygame.init()
pygame.display.set_caption('PyLink v0.0.1')

from config import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

from debug import console
console.add_message('PyLink v0.1')

from game import ClearviewFarmGame
game = ClearviewFarmGame()

# init clock
update_timer = 0
update_count = 0
render_timer = 0
render_count = 0
main_timer = 0

# start main game loop
previous_time = time.perf_counter()
running = True

while running:
    # pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # the user clicked X to close the window
            running = False
    
    # keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    
    # time
    current_time = time.perf_counter()  # time measured "in fractional seconds"
    elapsed_time = current_time - previous_time
    previous_time = current_time

    # update
    update_timer += elapsed_time
    while update_timer >= SECONDS_PER_UPDATE:
        update_timer -= SECONDS_PER_UPDATE
        update_count += 1
        game.update(SECONDS_PER_UPDATE)
    
    # render
    render_timer += elapsed_time
    if render_timer >= MIN_SECONDS_PER_RENDER:
        render_timer -= MIN_SECONDS_PER_RENDER
        render_count += 1
        screen.fill('black')   # clear the last frame
        game.render()          # RENDER YOUR GAME HERE
        console.render(screen)
        pygame.display.flip()  # display the next frame

    # core stats
    main_timer += elapsed_time
    if main_timer > 1.0:
        main_timer -= 1.0
        console.set_fps_text(f'{update_count}hz {render_count}fps')
        update_count = 0
        render_count = 0

# TODO: game.quit()?
pygame.quit()