
import random
from dino_runner.components.obstacles.obstacle_bird import ObstacleBird

class Bird(ObstacleBird):
    BIRD_HEIGHTS = [70, 250, 40]
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.choice(self.BIRD_HEIGHTS)
        self.index = 0
    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1