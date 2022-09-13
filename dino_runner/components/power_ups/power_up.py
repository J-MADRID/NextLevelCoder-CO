import imp
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
import random

class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_HEIGHT + random.randint(800, 1000)
        self.rect.y = random.randint(100, 150)
        self.type = type

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < 0:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
