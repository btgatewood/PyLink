import pygame

from console import Console

SCREEN_CENTER = (1280 // 2, 720 // 2)  # hack

class ClearviewFarmGame:
    def __init__(self, console: Console):
        # basic game setup
        super().__init__()
        self.console = console
        self.console.add_message('Clearview Farm v0.0.1')
        self.screen = pygame.display.get_surface()

        # self.sprites = pygame.sprite.Group()
        # self.sprites.add(self.player)

        self.image = pygame.image.load('data/SunnysideWorld/player_walk.png')
        self.image = pygame.transform.scale_by(self.image, 3)  # 48x48
        self.image = self.image.convert_alpha()  # do we need to reassign?
        self.rect = self.image.get_rect(center = SCREEN_CENTER)

    def update(self):
        pass

    def render(self):
        # self.sprites.draw(self.screen)
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':  # hack for vscode
    import main