import pygame


class StartScreen():
    def __init__(self, game):
        self.game = game

        self.header = game.font["big"].render("FlappyBird", False, "white")
        self.note = game.font["regular"].render("Tap space to start", False, "white")
        self.note_rect = self.note.get_rect(center=(240, 450))
        self.header_rect = self.header.get_rect(center=(250, 80))

        self.gravity = -1
        self.bird = self.game.bird_group.sprite

    def run(self):
        if self.bird.rect.y < 300:
            self.gravity += 0.2
        elif self.bird.rect.y > 320:
            self.gravity -= 0.2
        self.bird.move((0, self.gravity))

    def render(self):
        self.game.screen.blit(self.note, self.note_rect)
        self.game.screen.blit(self.header, self.header_rect)
    