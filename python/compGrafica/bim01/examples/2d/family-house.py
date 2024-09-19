import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Initialize Pygame and OpenGL
pygame.init()
pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
gluOrtho2D(0, 800, 0, 600)

# Function to draw the sky and grass
def draw_background():
    # Draw the sky
    glColor3f(0.53, 0.81, 0.98)  # Light blue for the sky
    glBegin(GL_QUADS)
    glVertex2f(0, 200)  # Adjusted to make sky start lower
    glVertex2f(800, 200)
    glVertex2f(800, 600)
    glVertex2f(0, 600)
    glEnd()

    # Draw the grass
    glColor3f(0.0, 0.8, 0.0)  # Green for the grass
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(800, 0)
    glVertex2f(800, 200)  # Adjusted to lower the grass height
    glVertex2f(0, 200)
    glEnd()

# Function to draw the house
def draw_house():
    glColor3f(1.0, 0.0, 0.0)  # Red color for the house body
    glBegin(GL_QUADS)
    glVertex2f(300, 200)
    glVertex2f(500, 200)
    glVertex2f(500, 350)
    glVertex2f(300, 350)
    glEnd()

    glColor3f(0.5, 0.35, 0.05)  # Brown color for the door
    glBegin(GL_QUADS)
    glVertex2f(370, 200)
    glVertex2f(430, 200)
    glVertex2f(430, 280)
    glVertex2f(370, 280)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)  # Blue color for the roof
    glBegin(GL_TRIANGLES)
    glVertex2f(280, 350)
    glVertex2f(520, 350)
    glVertex2f(400, 450)
    glEnd()

def draw_butterfly():
    # Butterfly wings (left side)
    glColor3f(1.0, 0.0, 1.0)  # Pink color for the wings
    draw_circle(185, 495, 7)  # Left wing as a circle
    draw_circle(185, 505, 7)  # Left wing as a circle
    draw_circle(195, 495, 7)  # Right wing as a circle
    draw_circle(195, 505, 7)  # Right wing as a circle

    # Butterfly body
    glColor3f(0.0, 0.0, 0.0)  # Black butterfly body
    glBegin(GL_LINES)
    glVertex2f(190, 490)
    glVertex2f(190, 510)
    glEnd()

    # Butterfly antennae (ears)
    glColor3f(0.0, 0.0, 0.0)  # Black for the antennae
    glBegin(GL_LINES)
    glVertex2f(190, 510)  # Starting at the top of the body
    glVertex2f(185, 520)  # Left antenna going up and left
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(190, 510)  # Starting at the top of the body
    glVertex2f(195, 520)  # Right antenna going up and right
    glEnd()

# Function to draw a circle (used for wings and other features)
def draw_circle(x, y, radius):
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = i * math.pi / 180
        glVertex2f(x + radius * math.cos(theta), y + radius * math.sin(theta))
    glEnd()

# Function to draw a circle (used for faces)
def draw_circle(x, y, radius):
    glBegin(GL_POLYGON)
    for i in range(360):
        theta = i * math.pi / 180
        glVertex2f(x + radius * math.cos(theta), y + radius * math.sin(theta))
    glEnd()

# Function to draw the family (stick figures)
def draw_stick_figure(x, y):
    glColor3f(0.0, 0.0, 0.0)  # Black for stick figures

    # Body
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x, y + 40)
    glEnd()

    # Legs
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(x - 10, y - 20)
    glVertex2f(x, y)
    glVertex2f(x + 10, y - 20)
    glEnd()

    # Arms
    glBegin(GL_LINES)
    glVertex2f(x, y + 30)
    glVertex2f(x - 20, y + 20)
    glVertex2f(x, y + 30)
    glVertex2f(x + 20, y + 20)
    glEnd()

    # Head (circle)
    glColor3f(1.0, 0.8, 0.6)  # Skin color
    draw_circle(x, y + 50, 10)

    # Facial features
    glColor3f(0.0, 0.0, 0.0)  # Black for features
    # Eyes
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x - 3, y + 53)
    glVertex2f(x + 3, y + 53)
    glEnd()

    # Mouth
    glBegin(GL_LINES)
    glVertex2f(x - 3, y + 47)
    glVertex2f(x + 3, y + 47)
    glEnd()

# Function to draw a tree
def draw_tree(x, y):
    # Draw the trunk
    glColor3f(0.55, 0.27, 0.07)  # Brown color for the trunk
    glBegin(GL_QUADS)
    glVertex2f(x - 20, y)  # Increased the trunk width
    glVertex2f(x + 20, y)
    glVertex2f(x + 20, y + 100)  # Increased the trunk height
    glVertex2f(x - 20, y + 100)
    glEnd()

    # Draw the leaves
    glColor3f(0.0, 0.5, 0.0)  # Dark green for the leaves
    glBegin(GL_TRIANGLES)
    glVertex2f(x - 80, y + 100)  # Increased the leaves width
    glVertex2f(x + 80, y + 100)
    glVertex2f(x, y + 200)  # Increased the height of the leaves
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(x - 70, y + 150)
    glVertex2f(x + 70, y + 150)
    glVertex2f(x, y + 250)  # Made the top of the tree taller
    glEnd()

# Function to draw the full scene
def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw the sky and grass
    draw_background()

    # Draw the house
    draw_house()

    # Draw the butterfly
    draw_butterfly()

    # Draw the family (stick figures)
    draw_stick_figure(100, 200)  # Father
    draw_stick_figure(150, 200)  # Mother
    draw_stick_figure(200, 200)  # Child

    # Draw trees
    draw_tree(600, 200)
    draw_tree(700, 200)

    pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_scene()
    pygame.time.wait(10)

pygame.quit()
