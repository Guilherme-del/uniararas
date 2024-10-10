import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

# Função para desenhar um retângulo
def draw_rect(x, y, width, height, color):
    glBegin(GL_QUADS)
    glColor3f(*color)  # Define a cor
    glVertex2f(x, y)  # Inferior esquerdo
    glVertex2f(x + width, y)  # Inferior direito
    glVertex2f(x + width, y + height)  # Superior direito
    glVertex2f(x, y + height)  # Superior esquerdo
    glEnd()

# Função para desenhar um triângulo
def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    glBegin(GL_TRIANGLES)
    glColor3f(*color)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

# Função para desenhar um círculo
def draw_circle(x, y, radius, color, num_segments=100):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(*color)
    glVertex2f(x, y)  # Centro do círculo
    for i in range(num_segments + 1):
        theta = 2.0 * math.pi * i / num_segments
        dx = radius * math.cos(theta)
        dy = radius * math.sin(theta)
        glVertex2f(x + dx, y + dy)
    glEnd()

# Função para desenhar um quadrado (equivalente a um retângulo)
def draw_square(x, y, size, color):
    draw_rect(x, y, size, size, color)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Desenhar formas
        draw_rect(-1, -1, 0.5, 0.5, (1, 0, 0))  # Retângulo vermelho
        draw_triangle(-0.5, 0, 0.5, 0, 0, 1, (1, 0, 1))  # Triângulo verde
        draw_circle(0, 0, 0.3, (0, 0, 1))  # Círculo azul
        draw_square(0.5, -1, 0.5, (1, 1, 0))  # Quadrado amarelo

        pygame.display.flip()
        pygame.time.wait(10)

main()