import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Função para desenhar um retângulo
def draw_rect(x, y, width, height, color):
    glBegin(GL_QUADS)
    glColor3f(*color)  # Define a cor
    glVertex2f(x, y)  # Inferior esquerdo
    glVertex2f(x + width, y)  # Inferior direito
    glVertex2f(x + width, y + height)  # Superior direito
    glVertex2f(x, y + height)  # Superior esquerdo
    glEnd()

# Função para desenhar Mario
def draw_mario():
    # Corpo
    draw_rect(-0.1, -0.3, 0.2, 0.3, (1, 0, 0))  # Vermelho

    # Cabeça
    draw_rect(-0.1, 0, 0.2, 0.2, (1, 0.8, 0))  # Pele

    # Olhos
    draw_rect(-0.07, 0.1, 0.03, 0.05, (1, 1, 1))  # Branco
    draw_rect(0.04, 0.1, 0.03, 0.05, (1, 1, 1))  # Branco
    draw_rect(-0.06, 0.1, 0.01, 0.03, (0, 0, 0))  # Olho esquerdo
    draw_rect(0.05, 0.1, 0.01, 0.03, (0, 0, 0))  # Olho direito

    # Chapéu
    draw_rect(-0.1, 0.15, 0.2, 0.05, (1, 0, 0))  # Vermelho

    # Braços
    draw_rect(-0.15, -0.3, 0.05, 0.2, (1, 0, 0))  # Braço esquerdo
    draw_rect(0.1, -0.3, 0.05, 0.2, (1, 0, 0))  # Braço direito
    draw_rect(0.1, -0.3, 0.05, 0.2, (1, 0, 0))  # Braço direito

    # Pernas
    draw_rect(-0.1, -0.6, 0.05, 0.3, (0, 0, 1))  # Perna esquerda
    draw_rect(0.05, -0.6, 0.05, 0.3, (0, 0, 1))  # Perna direita

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
        draw_mario()  # Desenha Mario
        pygame.display.flip()
        pygame.time.wait(10)

main()
