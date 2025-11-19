import pygame
from ball import Ball
from paddle import Paddle
from brick import Brick

pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Clone")

FPS = 60

# Colors
BLACK = (0, 0, 0)

def main():
    clock = pygame.time.Clock()

    paddle = Paddle(WIDTH // 2 - 50, HEIGHT - 40)
    ball = Ball(WIDTH // 2, HEIGHT // 2)

    # Create some bricks
    bricks = []
    rows = 5
    cols = 10
    brick_width = WIDTH // cols
    brick_height = 30

    for row in range(rows):
        for col in range(cols):
            brick = Brick(col * brick_width, row * brick_height + 40, brick_width, brick_height)
            bricks.append(brick)

    run = True
    while run:
        clock.tick(FPS)
        WIN.fill(BLACK)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and ball.attached:
                    ball.launch()

        # Paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move(-8)
        if keys[pygame.K_RIGHT]:
            paddle.move(8)

        # Ball follows paddle until launched
        if ball.attached:
            ball.update_position_on_paddle(paddle)
        else:
            ball.move()

        # Reset if ball goes off bottom of screen
        if ball.rect.top > HEIGHT:
            ball.reset(paddle)

        # Paddle collision
        if paddle.rect.colliderect(ball.rect) and not ball.attached:
            ball.y_vel *= -1

        # Brick collision
        for brick in bricks[:]:
            if brick.rect.colliderect(ball.rect):
                bricks.remove(brick)
                ball.y_vel *= -1

        # Draw everything
        paddle.draw(WIN)
        ball.draw(WIN)
        for brick in bricks:
            brick.draw(WIN)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
