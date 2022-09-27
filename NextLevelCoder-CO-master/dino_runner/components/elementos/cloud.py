from ast import Import
from email.mime import image
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH, CLOUD
import random

class Cloud(Sprite):
    def __init__(self):
        self.x = SCREEN_WIDTH 
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()
    def update(self, game):
        self.x -= game.game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH
            self.y = random.randint(50, 100)
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))

