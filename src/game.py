from console import Console

class Game:
    def __init__(self):
        pass
    def update(self):
        pass
    def render(self):
        pass

class ClearviewFarm(Game):
    def __init__(self, console: Console):
        super().__init__()
        self.console = console
        self.console.add_message('Clearview Farm v0.0.1')

    def update(self):
        pass

    def render(self):
        pass