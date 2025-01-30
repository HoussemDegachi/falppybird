import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, image, side, height):
        super().__init__()
        spawn_pos = 840
        self.image = pygame.transform.scale(image, (90, height))
        if side == 'bottom':
            self.rect = image.get_rect(topleft=(spawn_pos, 640 - 104 - height))
        else:
            self.image = pygame.transform.rotate(self.image, 180)
            self.rect = self.image.get_rect(topleft=(spawn_pos, 0))

    def translate(self):
        self.rect.x -= 4
        if self.rect.right < -100:
            self.kill()

    def update(self):
        self.translate()