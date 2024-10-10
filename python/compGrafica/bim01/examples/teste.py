import pygame
from pygame.locals import *
from OpenGL.GL import *

def main():
    # Inicializa o Pygame
    pygame.init()

    # Define o tamanho da janela
    width, height = 800, 600
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        # Limpa a tela
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # Troca os buffers
        pygame.display.flip()

if __name__ == "__main__":
    main()
