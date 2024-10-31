import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random

# Variáveis de controle para o movimento da nave
posicao_nave = -5
dash_iniciado = False

def desenhar_corpo_central_unico(raio_x, raio_y, profundidade, n_lados):
    """Desenha um único disco sólido e convexo para o corpo central da nave."""
    glColor3f(0.7, 0.7, 0.7)  # Cor cinza metálico

    # Disco único com formato convexo
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0)  # Centro do disco
    for i in range(n_lados + 1):
        angle = 2 * math.pi * i / n_lados
        x = raio_x * math.cos(angle)
        y = raio_y * math.sin(angle)
        glVertex3f(x, y, profundidade / 2)  # Superfície superior convexa
    glEnd()

def desenhar_cauda():
    """Desenha a cauda conectada ao corpo central da nave."""
    glColor3f(0.7, 0.7, 0.7)  # Cor cinza metálico para a cauda
    glBegin(GL_QUADS)
    altura_conexao = 0.15  # Ajuste para conectar a cauda diretamente ao corpo

    # Parte da cauda conectada ao corpo
    glVertex3f(-0.05, -0.02 + altura_conexao, -0.05)
    glVertex3f(0.05, -0.02 + altura_conexao, -0.05)
    glVertex3f(0.05, -0.02 + altura_conexao, -0.5)
    glVertex3f(-0.05, -0.02 + altura_conexao, -0.5)

    # Parte traseira da cauda mais estreita
    glVertex3f(-0.03, -0.02 + altura_conexao, -0.5)
    glVertex3f(0.03, -0.02 + altura_conexao, -0.5)
    glVertex3f(0.03, -0.02 + altura_conexao, -1.0)
    glVertex3f(-0.03, -0.02 + altura_conexao, -1.0)
    glEnd()

def desenhar_detalhes():
    """Adiciona pequenos detalhes como linhas de divisão no corpo central."""
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_LINES)
    for i in range(-5, 6):
        glVertex3f(i * 0.1, 0, 0.15)
        glVertex3f(i * 0.1, 0, -0.15)
    glEnd()

def gerar_estrelas(qtd_estrelas):
    """Gera uma lista de posições de estrelas no fundo."""
    estrelas = []
    for _ in range(qtd_estrelas):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        z = random.uniform(-20, -5)
        estrelas.append((x, y, z))
    return estrelas

def desenhar_estrelas(estrelas):
    """Desenha as estrelas no fundo."""
    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)
    for estrela in estrelas:
        glVertex3f(*estrela)
    glEnd()

def main():
    global posicao_nave, dash_iniciado

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    estrelas = gerar_estrelas(100)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        desenhar_estrelas(estrelas)

        glPushMatrix()
        glTranslatef(0.0, 0.0, posicao_nave)
        glRotatef(-90, 1, 0, 0)  # Inverte a nave para visualizar de baixo para cima
        desenhar_corpo_central_unico(1.2, 1.2, 0.2, 50)  # Disco único central
        desenhar_detalhes()
        desenhar_cauda()
        glPopMatrix()

        if not dash_iniciado:
            posicao_nave += 0.02
            if posicao_nave >= -2:
                dash_iniciado = True
        else:
            posicao_nave += 0.5

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
