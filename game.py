import pygame
import sys
import os
from utils import remove_extention
from screens.startScreen import StartScreen
from screens.background import Background
from screens.gameScreen import GameScreen
from screens.gameOverScreen import GameOver
from objects.bird import Bird
import json


class Game():
    def __init__(self):
        pygame.init()
        self.game_state = None
        self.max_score = self.load_score()
        self.score = 0
        self.time_since_defeat = 0
        icon = pygame.image.load("graphics/favicon.ico")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Flappy bird")
        self.font = {
            "big": pygame.font.Font("fonts/regular_font.ttf", 70),
            "regular": pygame.font.Font("fonts/regular_font.ttf", 50),
            "small": pygame.font.Font("fonts/regular_font.ttf", 30)
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
        self.game_over_screen = GameOver(self)
        self.background = Background(self)

        self.spawn_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.spawn_event, 1000)

        self.audio_die = pygame.mixer.Sound("audio/die.wav")
        self.theme = pygame.mixer.Sound("audio/theme.mp3")
        self.is_theme = True
        self.theme.play(-1)

    def load_score(self):
        try:
            with open("save_data.json") as file:
                data = json.load(file)
                return data["score"]
        except:
            with open("save_data.json", "w") as file:
                file.write(json.dumps({"score": 0}))
            return 0

    def run(self):
        while True:
            self.user_input()
            self.background.animate()
            self.bird_group.update()
            self.background.render()
            self.bird_group.draw(self.screen)

            if self.game_state == None:
                self.start_screen.run()
                self.start_screen.render()
            elif self.game_state == False:
                self.game_over_screen.render()
            else:
                self.game_screen.run()
                self.game_screen.render()

            pygame.display.update()
            self.clock.tick(60)

    def user_input(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    if self.is_theme:
                        self.theme.stop()
                    else:
                        self.theme.play(-1)
                    self.is_theme = not self.is_theme
            if not self.game_state:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and (self.game_state == None or pygame.time.get_ticks() - self.time_since_defeat > 1000):
                        self.game_state = True
                        self.bird_group.sprite.set_physics(True)
                        self.bird_group.sprite.set_controls(True)
                        self.bird_group.sprite.reset_pos()

            if self.game_state:
                if event.type == self.spawn_event:
                    self.game_screen.spawn()

    def end_game(self, new_score):
        if self.max_score < new_score:
            self.max_score = new_score
            with open("save_data.json", "w") as file:
                file.write(json.dumps({"score": new_score}))

        self.score = new_score
        self.game_state = False
        self.bird_group.sprite.set_controls(False)
        self.time_since_defeat = pygame.time.get_ticks()

    def load_data(self, path):
        data = {}
        alpha_images = ["yellowbird-downflap",
                        "yellowbird-midflap", "yellowbird-upflap", "gameover"]
        for item in os.listdir(path):
            no_extention_name = remove_extention(item)
            if no_extention_name in alpha_images:
                data[no_extention_name] = pygame.image.load(
                    f"{path}/{item}").convert_alpha()
            else:
                data[no_extention_name] = pygame.image.load(
                    f"{path}/{item}").convert()
        return data


Game().run()