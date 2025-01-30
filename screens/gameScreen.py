import pygame

class GameScreen():
    def __init__(self, game, bird_group):
        self.game = game
        self.bird = bird_group.sprite
        self.obstacles = pygame.sprite.Group()
    def run(self):
        ...
    def render(self):
        ...
    def spawn(self):
        ...