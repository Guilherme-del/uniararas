import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define o labirinto como uma matriz de 0s e 1s
maze = [
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

def draw_maze():
    rows = len(maze)
    cols = len(maze[0])
    for y in range(rows):
        for x in range(cols):
            if maze[y][x] == 1:  # Se houver uma parede
                glBegin(GL_QUADS)
                glVertex3f(x - cols // 2, y - rows // 2, 0)         # Inferior esquerdo
                glVertex3f(x - cols // 2 + 1, y - rows // 2, 0)     # Inferior direito
                glVertex3f(x - cols // 2 + 1, y - rows // 2 + 1, 0) # Superior direito
                glVertex3f(x - cols // 2, y - rows // 2 + 1, 0)     # Superior esquerdo
                glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_maze()
        pygame.display.flip()
        pygame.time.wait(10)

main()
