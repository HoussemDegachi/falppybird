import pygame

class Space(pygame.sprite.Sprite):
    def __init__(self, spawn_y):
        super().__init__()
        self.image = pygame.Surface((90, 180))
        self.image.set_alpha(0)
        spawn_pos = 840
        self.rect = self.image.get_rect(topleft=(spawn_pos, spawn_y)) 
    
    def translate(self):
        self.rect.x -= 4
        if self.rect.right < -100:
            self.kill()
    
    def update(self):
        self.translate()