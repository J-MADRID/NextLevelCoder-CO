from email.mime import image
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH
import random

class ObstacleBird(Sprite):

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(2800, 3000)
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < 0:
            obstacles.pop()
    
    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)