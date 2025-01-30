import pygame
import sys
import os
from utils import remove_extention
from screens.startScreen import StartScreen
from screens.background import Background
from screens.gameScreen import GameScreen
from objects.bird import Bird


class Game():
    def __init__(self):
        pygame.init()
        self.game_state = None
        self.max_score = 0
        pygame.display.set_caption("Flappy bird")
        self.font = {
            "big": pygame.font.Font("fonts/regular_font.ttf", 70),
            "regular": pygame.font.Font("fonts/regular_font.ttf", 50)
        }
        self.screen = pygame.display.set_mode((500, 640))
        self.clock = pygame.time.Clock()
        self.graphics_data = self.load_data("graphics")

        bird_frames = [self.graphics_data["yellowbird-downflap"],
                       self.graphics_data["yellowbird-midflap"], self.graphics_data["yellowbird-upflap"]]
        self.bird_group = pygame.sprite.GroupSingle()
        self.bird_group.add(Bird(bird_frames))

        self.start_screen = StartScreen(self)
        self.game_screen = GameScreen(self, self.bird_group)
        self.background = Background(self)

    def run(self):
        while True:
            self.user_input()
            self.background.animate()
            self.background.render()
            self.bird_group.update()
            self.bird_group.draw(self.screen)

            if self.game_state == None:
                self.start_screen.run()
                self.start_screen.render()
            elif self.game_state:
                self.game_screen.run()
                self.game_screen.render()

            pygame.display.update()
            self.clock.tick(60)

    def user_input(self):
        spawn_event = pygame.USEREVENT + 1
        pygame.time.set_timer(spawn_event, 800)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not self.game_state:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_state = True
                        self.bird_group.sprite.set_physics(True)

            if self.game_state:
                if event.type == spawn_event:
                    self.game_screen.spawn()

    def load_data(self, path):
        data = {}
        for item in os.listdir(path):
            data[remove_extention(item)] = pygame.image.load(
                f"{path}/{item}").convert_alpha()
        return data


Game().run()
