''' main_v3.py uses the time.perf_counter() function to limit ticks and fps '''
''' the average ticks per second and fps is exactly 60, 420 on the laptop '''

import os
import time

import pygame

from debug import Console

UPDATES_PER_SECOND = 60.0
SECONDS_PER_UPDATE = 1.0 / UPDATES_PER_SECOND

MAX_RENDERS_PER_SECOND = 420.0
MIN_SECONDS_PER_RENDER = 1.0 / MAX_RENDERS_PER_SECOND

os.environ['SDL_VIDEO_WINDOW_POS'] = '1, 32'  # set window position

pygame.init()
pygame.display.set_caption('PyLink v0.0.1')

console = Console()
console.add_text('PyLink v0.0.1')
console.add_text('Hello, World!')

screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
previous_time = time.perf_counter()  # "in fractional seconds"
update_timer = 0
render_timer = 0
app_timer = 0
running = True

update_count = 0
render_count = 0

while running:
    # events/input
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # the user clicked X to close the window
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    
    # time
    current_time = time.perf_counter()
    elapsed_time = current_time - previous_time
    previous_time = current_time

    # update
    update_timer += elapsed_time
    while update_timer >= SECONDS_PER_UPDATE:
        update_timer -= SECONDS_PER_UPDATE
        update_count += 1
        # TODO: game.update()
    
    # render
    render_timer += elapsed_time
    if render_timer >= MIN_SECONDS_PER_RENDER:
        render_timer -= MIN_SECONDS_PER_RENDER
        render_count += 1
        screen.fill('black')   # clear the last frame
        # TODO: game.render()  # RENDER YOUR GAME HERE
        console.draw_text(screen)
        pygame.display.flip()  # display the next frame

    # process data
    app_timer += elapsed_time
    if app_timer > 1.0:
        app_timer -= 1.0
        console.add_text(f'{update_count} hz, {render_count} fps')
        update_count = 0
        render_count = 0

pygame.quit()