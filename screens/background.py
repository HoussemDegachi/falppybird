import pygame

class Background():
    def __init__(self, game):
        self.game = game
        self.day_sky = game.graphics_data["background-day"]
        self.night_sky = game.graphics_data["background-night"]
        self.night_sky.set_alpha(0)
        self.floor = pygame.transform.scale(game.graphics_data["base"], (700, 110))
        self.floor_rect = self.floor.get_rect(bottomleft=(0, 646))
        self.is_day = True
        self.night_alpha = 0
        self.day_alpha = 255
    
    def animate(self):
        if self.floor_rect.left <= -200:
            self.floor_rect.left = 0
        self.floor_rect.x -= 2

        if self.is_day and self.day_alpha < 255:
            self.day_alpha += 1
            self.night_alpha -= 1
        elif not self.is_day and self.night_alpha < 255:
            self.night_alpha += 1
            self.day_alpha -= 1
        self.day_sky.set_alpha(self.day_alpha)
        self.night_sky.set_alpha(self.night_alpha)

    def render(self):
        self.game.screen.blit(pygame.transform.scale(self.day_sky, self.game.screen.get_size()))
        self.game.screen.blit(pygame.transform.scale(self.night_sky, self.game.screen.get_size()))
        self.game.screen.blit(self.floor, self.floor_rect)
    
    def switch_time(self):
        self.is_day = not self.is_day