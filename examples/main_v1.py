''' main_v1.py uses the pygame.time.Clock.tick() method to limit fps '''
''' the average framerate is about 60.25 fps on the laptop & desktop '''

import os
import time

import pygame

import debug

os.environ['SDL_VIDEO_WINDOW_POS'] = '1, 32'  # set window position

pygame.init()
pygame.display.set_caption('PyLink v0.0.1')

console = debug.Console()
console.add_text('PyLink v0.0.1')
console.add_text('Hello, World!')

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

app_timer = 0
last_time = time.perf_counter()
frame_count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # the user clicked X to close the window
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    this_time = time.perf_counter()
    app_timer += this_time - last_time
    last_time = this_time
    frame_count += 1

    if app_timer > 1.0:
        app_timer -= 1.0
        console.add_text(f'{frame_count} fps')
        frame_count = 0

    screen.fill('black')  # clear the last frame
    # RENDER YOUR GAME HERE
    console.draw_text(screen)
    pygame.display.flip()  # display the next frame

    # limit FPS to 60
    # dt is delta time in seconds since last frame
    # used for framerate-independent physics
    dt = clock.tick(60) / 1000

pygame.quit()
