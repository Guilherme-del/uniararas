import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random

# Initialize Pygame and OpenGL
pygame.init()
display = (800, 600)  # Screen dimensions
window = pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
pygame.display.set_caption('Pac-Man')
glClearColor(0, 0, 0, 1)

# Class representing a ghost
class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.choice([0, 90, 180, 270])  # Initial random direction

    def move(self):
        # Implement a simple random movement for now
        self.direction = random.choice([0, 90, 180, 270])
        if self.direction == 0:
            self.x += 0.1
        elif self.direction == 180:
            self.x -= 0.1
        elif self.direction == 90:
            self.y += 0.1
        elif self.direction == 270:
            self.y -= 0.1

    def draw(self):
        glColor3f(1, 0, 0)  # Red
        draw_circle(self.x, self.y, 0.5)

# Function to draw a square
def draw_square(x, y):
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + 1, y)
    glVertex2f(x + 1, y + 1)
    glVertex2f(x, y + 1)
    glEnd()

# Function to draw a circle
def draw_circle(x, y, radius):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(360):
        angle = i * math.pi / 180
        glVertex2f(x + radius * math.cos(angle), y + radius * math.sin(angle))
    glEnd()

# Define colors
YELLOW = (1, 1, 0)  # Yellow color
BLUE = (0, 0, 1)    # Blue color
WHITE = (1, 1, 1)   # White color
GREEN = (0, 1, 0)   # Green color

# Function to draw the Pac-Man
def draw_pacman(x, y, angle):
    glColor3f(*YELLOW)
    glBegin(GL_TRIANGLE_FAN)
    for i in range(360):
        angle_rad = math.radians(i - angle)
        glVertex2f(x + 0.5 * math.cos(angle_rad), y + 0.5 * math.sin(angle_rad))
    glEnd()

# Function to draw the scene
def draw_scene():
    for y in range(len(labirinto)):
        for x in range(len(labirinto[0])):
            if labirinto[y][x] == 1:  # Wall
                glColor3f(*BLUE)
                draw_square(x, y)
            elif labirinto[y][x] == 2:  # Point
                glColor3f(*WHITE)
                draw_circle(x + 0.5, y + 0.5, 0.2)
            elif labirinto[y][x] == 3:  # Power-up (add functionality later)
                glColor3f(*GREEN)
                draw_circle(x + 0.5, y + 0.5, 0.3)

# Define your maze layout
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 2, 2, 2, 2, 2, 2, 0, 1],
    [1, 0, 2, 0, 1, 1, 1, 2, 0, 1],
    [1, 0, 2, 0, 0, 0, 0, 2, 0, 1],
    [1, 0, 2, 2, 2, 2, 2, 2, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 1, 1, 1, 1, 1, 2, 0, 1],
    [1, 2, 0, 0, 0, 0, 0, 2, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Initialize OpenGL
glEnable(GL_DEPTH_TEST)

# Set up orthographic projection
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, len(labirinto[0]), len(labirinto), 0, -1, 1)  # Adjusted orthographic projection

# Set up model view
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Game loop
def game_loop():
    pacman_x, pacman_y, pacman_angle = 3, 6, 0  # Moved Pac-Man further down
    pacman_speed = 0.1
    score = 0
    lives = 3
    ghosts = [Ghost(2, 2), Ghost(8, 2)]  # Create ghosts

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman_angle = 180
                elif event.key == pygame.K_RIGHT:
                    pacman_angle = 0
                elif event.key == pygame.K_UP:
                    pacman_angle = -90
                elif event.key == pygame.K_DOWN:
                    pacman_angle = 90

        # Update Pac-Man's position
        new_x = pacman_x + pacman_speed * math.cos(math.radians(pacman_angle))
        new_y = pacman_y + pacman_speed * math.sin(math.radians(pacman_angle))

        # Check for collisions
        if (0 <= new_x < len(labirinto[0]) and 0 <= new_y < len(labirinto) and
                labirinto[int(new_y)][int(new_x)] != 1):
            pacman_x = new_x
            pacman_y = new_y
            if labirinto[int(new_y)][int(new_x)] == 2:
                score += 10
                labirinto[int(new_y)][int(new_x)] = 0

        # Update ghosts
        for ghost in ghosts:
            ghost.move()
            if abs(pacman_x - ghost.x) < 0.5 and abs(pacman_y - ghost.y) < 0.5:
                lives -= 1
                if lives == 0:
                    print("Game Over!")
                    pygame.quit()
                    quit()
                else:
                    pacman_x, pacman_y = 3, 6  # Reset Pac-Man's position

        # Draw
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_scene()
        draw_pacman(pacman_x, pacman_y, pacman_angle)
        for ghost in ghosts:
            ghost.draw()

        # Draw score and lives
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        window.blit(score_text, (10, 10))
        window.blit(lives_text, (display[0] - 120, 10))

        pygame.display.flip()
        pygame.time.wait(10)

game_loop()
