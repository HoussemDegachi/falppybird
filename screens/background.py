import pygame

class Background():
    def __init__(self, game):
        self.game = game
        self.sky = game.graphics_data["background-day"]
        self.floor = pygame.transform.scale(game.graphics_data["base"], (700, 110))
        self.floor_rect = self.floor.get_rect(bottomleft=(0, 646))
    
    def animate(self):
        if self.floor_rect.left <= -200:
            self.floor_rect.left = 0
        self.floor_rect.x -= 2

    def render(self):
        self.game.screen.blit(pygame.transform.scale(self.sky, self.game.screen.get_size()))
        self.game.screen.blit(self.floor, self.floor_rect)