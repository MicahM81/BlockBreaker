import pygame

class Ball:
    def __init__(self, x, y, radius=8):
        self.radius = radius
        self.x_vel = 5
        self.y_vel = -5
        self.attached = True     # NEW: ball starts attached to paddle
        self.rect = pygame.Rect(x, y, radius * 2, radius * 2)

    def update_position_on_paddle(self, paddle):
        """Keep the ball centered on the paddle while attached."""
        self.rect.centerx = paddle.rect.centerx
        self.rect.bottom = paddle.rect.top - 1

    def launch(self):
        """Release the ball from the paddle."""
        self.attached = False

    def reset(self, paddle):
        """Reset ball back to paddle center."""
        self.attached = True
        self.x_vel = 5
        self.y_vel = -5
        self.update_position_on_paddle(paddle)

    def move(self):
        if self.attached:
            return  # do NOT move until launched

        # Normal movement
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

        # Bounce walls
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.x_vel *= -1
        if self.rect.top <= 0:
            self.y_vel *= -1

    def draw(self, window):
        pygame.draw.circle(
            window,
            (255, 255, 255),
            self.rect.center,
            self.radius
        )
