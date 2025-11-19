# Breakout Clone (Python + Pygame)

A classic **Breakout-style arcade game** built in Python using the Pygame library.  
This project demonstrates core game development concepts such as:

- Real-time animation
- Collision detection
- Input handling
- Object-oriented game design
- Game state management
- Paddle hit-angle physics
- Level and lives system

---

## 🕹️ Features

### ✔ Smooth Paddle Controls  
Move left and right with the arrow keys.

### ✔ Ball Physics  
The ball starts attached to the paddle and launches when the player presses **SPACE**.  
Bounce angle changes based on where the ball hits the paddle (like real Breakout).

### ✔ Lives System  
The player starts with 3 lives.  
If the ball falls below the paddle, a life is lost.

### ✔ Brick Layout  
Rows of bricks appear at the top of the screen.  
Break them all to win.

### ✔ Game States  
- **PLAYING**
- **GAME OVER**
- **YOU WIN**

Each state displays a centered message and waits for the player to press **SPACE** to restart.

---

## 🚀 Getting Started

### 1. Install Dependencies
Make sure you have Python installed.

```bash
pip install pygame