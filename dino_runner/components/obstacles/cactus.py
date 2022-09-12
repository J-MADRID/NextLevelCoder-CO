from dino_runner.components.obstacles.obstacle import Obstacle
import random

class Cactus(Obstacle):
    def __init__(self, image):
        type = random.randint(0,2)
        super().__init__(image, type)
        self.rect.y = 325
        