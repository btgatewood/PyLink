import pygame

from console import Console
from player import Player

class ClearviewFarmGame:
    def __init__(self, console: Console):
        super().__init__()
        self.console = console
        self.console.add_message('Clearview Farm v0.0.1')
        self.screen = pygame.display.get_surface()

        self.player = Player(console)

        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)

    def update(self, delta_time):
        self.sprites.update(delta_time)

    def render(self):
        self.sprites.draw(self.screen)


if __name__ == '__main__':  # hack for vscode
    import main