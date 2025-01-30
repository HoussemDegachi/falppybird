import pygame
from utils import get_rect_border


class GameOver():
    def __init__(self, game):
        self.game = game
        self.game_over_image = pygame.transform.rotozoom(self.game.graphics_data["gameover"], 0, 1.25)
        self.game_over_rect = self.game_over_image.get_rect(center=(250, 80))
        self.score_box = pygame.Surface((130, 180))
        self.score_box.set_alpha(0)
        self.score_box_rect = self.score_box.get_rect(midtop=(250, 170))
        self.header1 = self.game.font["small"].render("BestScore", False, "#ff9a00")
        self.header1_rect = self.header1.get_rect(midtop=(250, 190))
        self.header2 = self.game.font["small"].render("Score", False, "#ff9a00")
        self.header2_rect = self.header2.get_rect(midtop=(250, 255))
    
    def render(self):
        self.game.screen.blit(self.game_over_image, self.game_over_rect)
        self.game.screen.blit(self.score_box, self.score_box_rect)
        radius = 8
        pygame.draw.rect(self.game.screen, "#F8DE7E",self.score_box_rect, 0, radius - 1)
        pygame.draw.rect(self.game.screen, "black", get_rect_border(self.score_box_rect, 1, 1), 1, radius)
        self.game.screen.blit(self.header1, self.header1_rect)
        self.game.screen.blit(self.header2, self.header2_rect)
        
        best_score = self.game.font["regular"].render(f"{self.game.max_score}", False, "white")
        best_score_rect = best_score.get_rect(midtop=(250, 213))
        self.game.screen.blit(best_score, best_score_rect)

        score = self.game.font["regular"].render(f"{self.game.score}", False, "white")
        score_rect = score.get_rect(midtop=(250, 276))
        self.game.screen.blit(score, score_rect)
