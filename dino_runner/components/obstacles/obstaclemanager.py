import pygame
import random
from dino_runner.components.obstacles.catus import Cactus
from dino_runner.components.obstacles.largecactus import Largecactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
           listcactus = [Cactus(SMALL_CACTUS), Largecactus(LARGE_CACTUS)]
           self.obstacles.append(listcactus[random.randint(0, 1)])

        for obstacle in self.obstacles:
            obstacle.updates(game.game_speed, self.obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
            
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)