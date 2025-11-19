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

# Game state constants
PLAYING = 0
GAME_OVER = 1
WON = 2


def build_bricks(rows, cols, brick_width, brick_height):
    bricks = []
    for row in range(rows):
        for col in range(cols):
            brick = Brick(col * brick_width,
                          row * brick_height + 40,
                          brick_width,
                          brick_height)
            bricks.append(brick)
    return bricks



def main():
    clock = pygame.time.Clock()

    paddle = Paddle(WIDTH // 2 - 50, HEIGHT - 40)
    ball = Ball(WIDTH // 2, HEIGHT // 2)

    # Create some bricks
    rows = 5
    cols = 10
    brick_width = WIDTH // cols
    brick_height = 30
    bricks = build_bricks(rows, cols, brick_width, brick_height)

    # Account for player lives
    lives = 3
    font = pygame.font.SysFont("arial", 28)

    game_state = PLAYING

    def draw_lives(window, lives):
        text = font.render(f"Lives: {lives}", True, (255, 255, 255))
        window.blit(text, (10, 10))

    def draw_center_text(text, size, y_offset=0, color=(255, 255, 255)):
        font_obj = pygame.font.SysFont("arial", size)
        surface = font_obj.render(text, True, color)
        rect = surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
        WIN.blit(surface, rect)

    run = True
    while run:
        clock.tick(FPS)
        WIN.fill(BLACK)

        # --- GAME OVER SCREEN ---
        if game_state == GAME_OVER:
            for event in pygame.event.get():  # <<< REQUIRED
                if event.type == pygame.QUIT:
                    run = False

            draw_center_text("GAME OVER", 60, color=(255, 0, 0))
            draw_center_text("Press SPACE to restart", 28, y_offset=40, color=(255, 255, 255))
            pygame.display.update()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                lives = 3
                bricks = build_bricks(rows, cols, brick_width, brick_height)
                ball.reset(paddle)
                game_state = PLAYING

            continue

        # --- WIN SCREEN ---
        if game_state == WON:

            for event in pygame.event.get():  # <<< REQUIRED
                if event.type == pygame.QUIT:
                    run = False

            draw_center_text("YOU WIN!", 60, y_offset=-40, color=(0, 255, 0))
            draw_center_text("Press SPACE to play again", 28, y_offset=40, color=(255, 255, 255))
            pygame.display.update()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                lives = 3
                bricks = build_bricks(rows, cols, brick_width, brick_height)
                ball.reset(paddle)
                game_state = PLAYING

            continue

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
            lives -= 1

            if lives > 0:
                ball.reset(paddle)  # place ball back on paddle
            else:
                game_state = GAME_OVER

        # Paddle collision
        if paddle.rect.colliderect(ball.rect) and not ball.attached:
            # Calculate where the ball hit the paddle
            paddle_center = paddle.rect.centerx
            ball_center = ball.rect.centerx
            distance_from_center = ball_center - paddle_center

            # Normalize value to range [-1, 1]
            normalized = distance_from_center / (paddle.rect.width / 2)

            # Set max angle from center (in degrees)
            max_angle = 60
            angle = normalized * max_angle

            # Convert angle to velocity components
            import math
            speed = (ball.x_vel ** 2 + ball.y_vel ** 2) ** 0.5  # keep same speed

            # Angle is measured from vertical, so rotate velocity
            rad = math.radians(angle)
            ball.x_vel = speed * math.sin(rad)
            ball.y_vel = -abs(speed * math.cos(rad))  # always bounce upward

            ball.rect.bottom = paddle.rect.top -1

        # Brick collision
        for brick in bricks[:]:
            if brick.rect.colliderect(ball.rect):
                bricks.remove(brick)
                ball.y_vel *= -1

        if len(bricks) == 0:
            game_state = WON

        # Draw everything
        paddle.draw(WIN)
        ball.draw(WIN)
        for brick in bricks:
            brick.draw(WIN)

        draw_lives(WIN, lives)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
