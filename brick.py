import random

import pygame

class Brick:
    def __init__(self, x, y, width, height, color=(0, 180, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
        pygame.draw.rect(window, (255,255,255), self.rect, 2)
