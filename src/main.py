import os
import time

import pygame

from console import Console
from game import ClearviewFarm

# config
UPDATES_PER_SECOND = 100.0
SECONDS_PER_UPDATE = 1.0 / UPDATES_PER_SECOND          # 0.01 @ 100 ticks

MAX_RENDERS_PER_SECOND = 1000.0
MIN_SECONDS_PER_RENDER = 1.0 / MAX_RENDERS_PER_SECOND  # 0.001 @ 1000 fps

# init app
os.environ['SDL_VIDEO_WINDOW_POS'] = '1, 32'  # set window position

pygame.init()
pygame.display.set_caption('PyLink v0.0.1')
screen = pygame.display.set_mode((1280, 720))

console = Console()
console.add_message('PyLink v0.0.1')

game = ClearviewFarm(console)

# init clock
update_timer = 0
update_count = 0
render_timer = 0
render_count = 0
main_timer = 0

previous_time = time.perf_counter()
running = True

while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # the user clicked X to close the window
            running = False
    
    # input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    
    # time
    current_time = time.perf_counter()
    elapsed_time = current_time - previous_time # "in fractional seconds"
    previous_time = current_time

    # update
    update_timer += elapsed_time
    while update_timer >= SECONDS_PER_UPDATE:
        update_timer -= SECONDS_PER_UPDATE
        update_count += 1
        game.update()
    
    # render
    render_timer += elapsed_time
    if render_timer >= MIN_SECONDS_PER_RENDER:
        render_timer -= MIN_SECONDS_PER_RENDER
        render_count += 1
        screen.fill('black')   # clear the last frame
        game.render()          # RENDER YOUR GAME HERE
        console.render(screen)
        pygame.display.flip()  # display the next frame

    # core data
    main_timer += elapsed_time
    if main_timer > 1.0:
        main_timer -= 1.0
        console.set_fps_text(f'{update_count} hz, {render_count} fps')
        update_count = 0
        render_count = 0

# TODO: game.quit()?
pygame.quit()