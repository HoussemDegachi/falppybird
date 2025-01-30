import pygame
from objects.pipe import Pipe
from objects.space import Space
from random import randint
from utils import get_rect_border


class GameScreen():
    def __init__(self, game, bird_group):
        self.game = game
        self.bird = bird_group.sprite
        self.obstacles = pygame.sprite.Group()
        self.spaces = pygame.sprite.Group()
        self.score = 0
        self.hit_voice = pygame.mixer.Sound("audio/hit.wav")
        self.point_voice = pygame.mixer.Sound("audio/point.wav")

    def run(self):
        if pygame.sprite.spritecollide(self.bird, self.spaces, True):
            self.point_voice.play()
            self.score += 1
            if self.score % 20 == 0 and self.score != 0:
                self.game.background.switch_time()
        
        if pygame.sprite.spritecollide(self.bird, self.obstacles, True):
            self.hit_voice.play()
            self.terminate()

        if self.bird.rect.bottom >= 530:
            self.terminate()

    def terminate(self):
        self.game.audio_die.play()
        self.obstacles.empty()
        self.spaces.empty()
        self.game.end_game(self.score)
        self.score = 0
        if not self.game.background.is_day:
            self.game.background.switch_time()


    def render(self):
        self.obstacles.update()
        self.spaces.update()
        self.obstacles.draw(self.game.screen)
        self.spaces.draw(self.game.screen)
        score_display = self.game.font["big"].render(f"{self.score}", False, "white")
        score_display_rect = score_display.get_rect(center=(250, 80))
        # pygame.draw.rect(self.game.screen, (128,128,128, 10), score_display_rect)
        # pygame.draw.rect(self.game.screen, (128,128,128, 10), get_rect_border(score_display_rect, 8, 4))
        self.game.screen.blit(score_display, score_display_rect)

    def spawn(self):
        first_pipe_height = randint(100, 256)
        self.obstacles.add(
            Pipe(self.game.graphics_data["pipe-green"], 'top', first_pipe_height))
        self.spaces.add(Space(first_pipe_height))
        self.obstacles.add(
            Pipe(self.game.graphics_data["pipe-green"], 'bottom', 356 - first_pipe_height))
