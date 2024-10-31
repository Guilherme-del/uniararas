import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import math

# Variáveis de controle para o movimento da nave
posicao_nave = -5
dash_iniciado = False

def desenhar_corpo_principal(raio_x, raio_y, profundidade, n_lados, n_camadas):
    """Desenha uma cúpula convexa mais grossa para o corpo principal da nave."""
    for i in range(n_camadas + 1):
        camada_profundidade = profundidade * (1 - (i / n_camadas) ** 2)  # Aumentando a profundidade
        raio_atual_x = raio_x * (1 - i / n_camadas)
        raio_atual_y = raio_y * (1 - i / n_camadas)
        
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.6, 0.6, 1)
        glVertex3f(0, 0, camada_profundidade / 2)
        for j in range(n_lados + 1):
            angle = 2 * math.pi * j / n_lados
            x = raio_atual_x * math.cos(angle)
            y = raio_atual_y * math.sin(angle)
            glVertex3f(x, y, camada_profundidade / 2)
        glEnd()

def desenhar_cauda():
    """Desenha uma cauda conectada ao corpo principal da nave."""
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.2, 0.2)  # Vermelho escuro para a cauda

    # Ajustando a posição da cauda para que fique conectada ao corpo principal
    altura_conexao = 0  # Valor aumentado para conectar mais a cauda ao corpo

    # Parte da cauda conectada ao corpo
    glVertex3f(-0.05,altura_conexao, -0.05)
    glVertex3f(0.05, altura_conexao, -0.05)
    glVertex3f(0.5,  altura_conexao, -0.5)
    glVertex3f(-0.05,  altura_conexao, -0.5)

    # Parte traseira da cauda mais estreita
    glVertex3f(-0.03, altura_conexao, -0.5)
    glVertex3f(0.03,  altura_conexao, -0.5)
    glVertex3f(0.03, altura_conexao, -1.0)
    glVertex3f(-0.03,  altura_conexao, -1.0)

    # Laterais da cauda para um visual mais detalhado
    glVertex3f(-0.05,  altura_conexao, -0.05)
    glVertex3f(-0.05, 0.02 + altura_conexao, -0.05)
    glVertex3f(-0.03, 0.02 + altura_conexao, -0.5)
    glVertex3f(-0.03,  altura_conexao, -0.5)

    glVertex3f(0.05, altura_conexao, -0.05)
    glVertex3f(0.05, 0.02 + altura_conexao, -0.05)
    glVertex3f(0.03, 0.02 + altura_conexao, -0.5)
    glVertex3f(0.03, altura_conexao, -0.5)

    glEnd()

def gerar_estrelas(qtd_estrelas):
    """Gera uma lista de posições de estrelas no fundo."""
    estrelas = []
    for _ in range(qtd_estrelas):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        z = random.uniform(-20, -5)  # Fundo mais distante
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

    # Gerar estrelas para o fundo
    estrelas = gerar_estrelas(100)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Desenha as estrelas ao fundo
        desenhar_estrelas(estrelas)

        # Posiciona e desenha a nave
        glPushMatrix()
        glTranslatef(0.0, 0.0, posicao_nave)  # Controla a posição da nave
        glRotatef(90, 1, 0, 0)  # Deita o corpo principal
        glRotatef(180, 0, 1, 0)  # Inverte a nave para deixar a cauda para baixo
        desenhar_corpo_principal(raio_x=0.8, raio_y=0.8, profundidade=0.3, n_lados=50, n_camadas=10)  # Aumentei a profundidade
        desenhar_cauda()
        glPopMatrix()

        # Atualiza a posição da nave
        if not dash_iniciado:
            posicao_nave += 0.02  # Movimento lento da nave
            if posicao_nave >= -2:  # Inicia o dash quando atinge um ponto
                dash_iniciado = True
        else:
            posicao_nave += 0.5  # Dash rápido para fora da tela

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
