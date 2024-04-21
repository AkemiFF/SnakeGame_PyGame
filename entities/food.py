import pygame
import random


class Food:
    def __init__(self, block_size, screen_width, screen_height):
        self.block_size = block_size
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x = random.randint(
            0, (screen_width - block_size) // block_size) * block_size
        self.y = random.randint(
            0, (screen_height - block_size) // block_size) * block_size

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y,
                         self.block_size, self.block_size))

    def respawn(self):
        self.x = random.randint(
            0, (self.screen_width - self.block_size) // self.block_size) * self.block_size
        self.y = random.randint(
            0, (self.screen_height - self.block_size) // self.block_size) * self.block_size
