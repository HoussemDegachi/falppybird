import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, frames):
        super().__init__()
        self.gravity = 0
        self.physics = False
        self.controls = False
        self.frames = [pygame.transform.rotozoom(frame, 0, 1.5) for frame in frames]
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.original_pos = (240, 310)
        self.rect = self.image.get_rect(center=self.original_pos)
        self.rotation_degree = 0
        self.wing_voice = pygame.mixer.Sound("audio/wing.wav")
        self.wing_voice.set_volume(0.4)
    
    def animate(self):
        self.frame_index += 0.3
        if self.frame_index > len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

        step = 2
        max_angle = 35
        if self.gravity < 0:
            if self.rotation_degree < max_angle:
                self.rotation_degree += step
        elif self.gravity == 0:
            if self.rotation_degree > 0:
                self.rotation_degree -= step
            elif self.rotation_degree < 0:
                self.rotation_degree += step
        else:
            if self.rotation_degree > -max_angle:
                self.rotation_degree -= step
        self.image = pygame.transform.rotate(self.image, self.rotation_degree)

    
    def move(self, moveBy):
        self.rect.x += moveBy[0]
        self.rect.y += moveBy[1]

    def set_physics(self, new_physics_state):
        self.physics = new_physics_state

    def set_controls(self, new_controls_state):
        self.controls = new_controls_state

    def apply_physics(self):
        self.gravity += 1
        if self.rect.bottom >= 530:
            self.gravity = 0
        self.rect.y += self.gravity

    def user_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.gravity > -2:
            self.gravity = -13
            self.wing_voice.play()
        
    def reset_pos(self):
        self.rect.center = self.original_pos
        self.rotation_degree = 0

    def update(self):
        self.animate()
        if self.physics:
            self.apply_physics()
        if self.controls:
            self.user_inputs()