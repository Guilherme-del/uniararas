import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

# Desenhar o corpo principal da nave como um disco simples
def draw_ship_body():
    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)  # Cor vermelha para o corpo principal
    glutSolidCylinder(1.5, 0.2, 50, 10)  # Base da nave em formato de cilindro achatado
    glPopMatrix()

# Desenhar naceles de dobra como cubos simples
def draw_nacelles():
    glPushMatrix()
    glColor3f(0.0, 1.0, 0.0)  # Cor verde para naceles
    glTranslatef(-2.0, 0.0, -1.0)
    glScalef(0.2, 0.7, 0.2)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2.0, 0.0, -1.0)
    glScalef(0.2, 0.7, 0.2)
    glutSolidCube(1)
    glPopMatrix()

# Desenhar estrelas no fundo
def draw_stars():
    glBegin(GL_POINTS)
    glColor3f(1.0, 1.0, 1.0)  # Cor branca para as estrelas
    for _ in range(100):
        glVertex3f(random.uniform(-15, 15), random.uniform(-10, 10), random.uniform(-20, -5))
    glEnd()

# Inicializar a cena e a perspectiva
def init_scene():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.2, 1.0)  # Fundo espacial escuro
    gluPerspective(45, (800/600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)  # Ajuste a posição da câmera mais próxima

# Função principal
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    init_scene()
    glutInit()  # Inicializar GLUT

    running = True
    while running:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Desenhar elementos diretamente, sem rotação ou inclinação
        draw_stars()
        draw_ship_body()
        draw_nacelles()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
