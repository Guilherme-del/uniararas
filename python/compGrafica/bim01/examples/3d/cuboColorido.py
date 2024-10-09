import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Definindo os vértices e arestas do cubo
vertices = [
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
]

arestas = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 7), (3, 6)
]

faces = [
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
]

cores = [
    (1, 0, 0),  # Vermelho
    (0, 1, 0),  # Verde
    (0, 0, 1),  # Azul
    (1, 1, 0),  # Amarelo
    (1, 0, 1),  # Magenta
    (0, 1, 1)   # Ciano
]

angulo_x = 0
angulo_y = 0
escala = 1

def desenhar_cubo():
    for i, face in enumerate(faces):
        glBegin(GL_QUADS)
        for vertice in face:
            glColor3fv(cores[i])  # Definindo a cor da face
            glVertex3fv(vertices[vertice])
        glEnd()
    
    glBegin(GL_LINES)
    for aresta in arestas:
        for vertice in aresta:
            glVertex3fv(vertices[vertice])
    glEnd()

def main():
    global angulo_x, angulo_y, escala
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    angulo_y -= 5
                if event.key == K_RIGHT:
                    angulo_y += 5
                if event.key == K_UP:
                    escala += 0.01  # Aumento mais lento
                if event.key == K_DOWN:
                    escala = max(0.1, escala - 0.01)  # Diminuição mais lenta

        glRotatef(angulo_x, 1, 0, 0)
        glRotatef(angulo_y, 0, 1, 0)
        glScalef(escala, escala, escala)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        desenhar_cubo()
        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()