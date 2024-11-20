"""
USS Firebrand (NCC-68723)
Autor: 
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import random

# Control variables for ship movement
posicao_nave_z = -5
dash_iniciado = False
dash_completado = False  # Indica se o dash terminou
dash_permitido = True    # Indica se o dash pode ser feito
dash_tempo = 0           # Controla o tempo de duração do dash
dash_duracao = 30        # Duração do dash

# Color palette
COR_CORPO = (0.5, 0.5, 0.6)
COR_PAINEL = (0.4, 0.4, 0.5)
COR_DETALHES = (0.3, 0.3, 0.4)
COR_COCKPIT = (0.2, 0.2, 0.2)
COR_ASAS = (0.4, 0.4, 0.5)
COR_ESTRELAS = (1, 1, 1)
COR_VERMELHA = (1.0, 0.0, 0.0)

# Variables for controlling angles
angle_x, angle_y = 0, 0
rotation_speed = 2

# Movement speed variables
velocidade_normal = 0.02
velocidade_dash = 0.5
velocidade_fundo = velocidade_normal  # Velocidade inicial do movimento do fundo

def desenhar_corpo_central_unico(raio_x, raio_y, profundidade, n_lados):
    """Desenha o corpo principal da nave"""
    glColor3f(*COR_CORPO)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, 0)
    for i in range(n_lados + 1):
        angle = 2 * math.pi * i / n_lados
        x = raio_x * math.cos(angle)
        y = raio_y * math.sin(angle)
        glVertex3f(x, y, profundidade / 6)
    glEnd()

    for j in range(12):
        angle1 = 2 * math.pi * j / 12
        angle2 = 2 * math.pi * (j + 1) / 12
        glColor3f(*COR_PAINEL)
        glBegin(GL_QUADS)
        glVertex3f(raio_x * math.cos(angle1), raio_y * math.sin(angle1), profundidade / 6)
        glVertex3f(raio_x * math.cos(angle2), raio_y * math.sin(angle2), profundidade / 6)
        glVertex3f(raio_x * math.cos(angle2), raio_y * math.sin(angle2), -profundidade / 6)
        glVertex3f(raio_x * math.cos(angle1), raio_y * math.sin(angle1), -profundidade / 6)
        glEnd()

def desenhar_cauda():
    """Desenha a cauda da nave"""
    glColor3f(*COR_PAINEL)
    glBegin(GL_QUADS)
    glVertex3f(-0.05, 0.01, -0.05)
    glVertex3f(0.05, 0.01, -0.05)
    glVertex3f(0.05, 0.01, -0.3)
    glVertex3f(-0.05, 0.01, -0.3)
    glVertex3f(-0.03, 0.01, -0.3)
    glVertex3f(0.03, 0.01, -0.3)
    glVertex3f(0.03, 0.01, -0.6)
    glVertex3f(-0.03, 0.01, -0.6)
    glEnd()

def gerar_estrelas(qtd_estrelas, raio_min=5, raio_max=30):
    """Gera estrelas ao redor da nave"""
    estrelas = []
    for _ in range(qtd_estrelas):
        theta = random.uniform(0, 2 * math.pi)
        phi = random.uniform(0, math.pi)
        r = random.uniform(raio_min, raio_max)

        x = r * math.sin(phi) * math.cos(theta)
        y = r * math.sin(phi) * math.sin(theta)
        z = r * math.cos(phi)

        estrelas.append([x, y, z])
    return estrelas

def atualizar_estrelas(estrelas, velocidade):
    """Atualiza a posição das estrelas"""
    for estrela in estrelas:
        estrela[2] += velocidade  # Move ao longo do eixo Z

        # Reposiciona as estrelas que saem do campo de visão
        if estrela[2] > 5:  # Ajuste de distância para as estrelas
            estrela[2] = -30
            estrela[0] = random.uniform(-30, 30)
            estrela[1] = random.uniform(-30, 30)

def desenhar_estrelas(estrelas):
    """Desenha as estrelas no fundo"""
    glBegin(GL_POINTS)
    glColor3f(*COR_ESTRELAS)
    for estrela in estrelas:
        glVertex3f(*estrela)
    glEnd()

def main():
    global dash_iniciado, dash_completado, dash_permitido, angle_x, angle_y, velocidade_fundo, posicao_nave_z, dash_tempo

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)

    estrelas = gerar_estrelas(2000)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if (evento.key == pygame.K_SPACE or evento.key == pygame.K_RETURN) and dash_permitido:
                    dash_iniciado = True
                    dash_completado = False
                    dash_tempo = 0  # Resetando o tempo do dash

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            angle_x += rotation_speed
        if keys[pygame.K_s]:
            angle_x -= rotation_speed
        if keys[pygame.K_a]:
            angle_y += rotation_speed
        if keys[pygame.K_d]:
            angle_y -= rotation_speed

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        desenhar_estrelas(estrelas)
        atualizar_estrelas(estrelas, velocidade_fundo)

        if not dash_completado:
            glPushMatrix()
            glTranslatef(0.0, 0.0, posicao_nave_z)
            glRotatef(-90, 1, 0, 0)
            glRotatef(angle_x, 1, 0, 0)
            glRotatef(angle_y, 0, 1, 0)

            desenhar_corpo_central_unico(1.5, 1.5, 0.3, 40)
            desenhar_cauda()

            glPopMatrix()

        glPopMatrix()

        if dash_iniciado:
            dash_tempo += 1
            posicao_nave_z += velocidade_dash
            if posicao_nave_z > 5 or dash_tempo > dash_duracao:
                dash_completado = True
                dash_iniciado = False
                dash_permitido = False
                posicao_nave_z = -5
                # Resetando a nave após o dash
        else:
            velocidade_fundo = velocidade_normal

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
