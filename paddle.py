import pygame

class Paddle:
    def __init__(self, x, y, width=120, height=20):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 8

    def move(self, dx):
        self.rect.x += dx
        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))

    def draw(self, window):
        pygame.draw.rect(window, (200, 200, 200), self.rect)
