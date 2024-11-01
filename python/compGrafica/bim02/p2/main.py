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

# Propellers
cor_propulsor = 0.5  # Initial intensity of the propeller

# Color palette
COR_CORPO = (0.5, 0.5, 0.6)
COR_PAINEL = (0.4, 0.4, 0.5)
COR_DETALHES = (0.3, 0.3, 0.4)
COR_COCKPIT = (0.2, 0.2, 0.2)
COR_ASAS = (0.4, 0.4, 0.5)
COR_ESTRELAS = (1, 1, 1)
COR_VERMELHA = (1.0, 0.0, 0.0)

# Variables for controlling camera angles
angle_x, angle_y = 0, 0
rotation_speed = 2

# Movement speed variables
velocidade_normal = 0.02
velocidade_dash = 0.5
velocidade_fundo = velocidade_normal  # Velocidade inicial do movimento do fundo

def desenhar_corpo_central_unico(raio_x, raio_y, profundidade, n_lados):
    """Draw the main body of the ship with additional layers and details."""
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

    for j in range(6):
        angle = 2 * math.pi * j / 6
        glBegin(GL_LINES)
        glVertex3f(0, 0, profundidade / 6)
        glVertex3f(raio_x * math.cos(angle), raio_y * math.sin(angle), -profundidade / 6)
        glEnd()

def desenhar_cauda():
    """Draws a detailed tail with additional layers and a red square at the end."""
    glColor3f(*COR_PAINEL)
    glBegin(GL_QUADS)
    altura_conexao = 0.01

    glVertex3f(-0.05, -0.02 + altura_conexao, -0.05)
    glVertex3f(0.05, -0.02 + altura_conexao, -0.05)
    glVertex3f(0.05, -0.02 + altura_conexao, -0.3)
    glVertex3f(-0.05, -0.02 + altura_conexao, -0.3)

    glVertex3f(-0.03, -0.02 + altura_conexao, -0.3)
    glVertex3f(0.03, -0.02 + altura_conexao, -0.3)
    glVertex3f(0.03, -0.02 + altura_conexao, -0.6)
    glVertex3f(-0.03, -0.02 + altura_conexao, -0.6)
    glEnd()

    glColor3f(*COR_DETALHES)
    glBegin(GL_LINES)
    for i in range(1, 5):
        glVertex3f(-0.05 + i * 0.02, altura_conexao, -0.05)
        glVertex3f(-0.05 + i * 0.02, altura_conexao, -0.6)
    glEnd()

    glColor3f(*COR_VERMELHA)
    glBegin(GL_QUADS)
    glVertex3f(-0.03, altura_conexao, -0.6)
    glVertex3f(0.03, altura_conexao, -0.6)
    glVertex3f(0.03, -0.5 + altura_conexao, -0.6)
    glVertex3f(-0.03, -0.5 + altura_conexao, -0.6)
    glEnd()

def gerar_estrelas(qtd_estrelas, raio_min=30, raio_max=60):
    estrelas = []
    for _ in range(qtd_estrelas):
        theta = random.uniform(0, 2 * math.pi)
        phi = random.uniform(0, math.pi)
        r = random.uniform(raio_min, raio_max)  # Mantém as estrelas mais distantes do centro

        x = r * math.sin(phi) * math.cos(theta)
        y = r * math.sin(phi) * math.sin(theta)
        z = r * math.cos(phi)

        estrelas.append([x, y, z])
    return estrelas

def atualizar_estrelas(estrelas, velocidade):
    """Move as estrelas e reposiciona aquelas que saem do campo de visão."""
    for estrela in estrelas:
        # Move as estrelas ao longo do eixo Z
        estrela[2] += velocidade

        # Reposiciona as estrelas fora do campo de visão para uma nova posição distante do centro
        if estrela[2] > 0:
            theta = random.uniform(0, 2 * math.pi)
            phi = random.uniform(0, math.pi)
            r = random.uniform(30, 60)  # Manter a distância mínima do centro

            estrela[0] = r * math.sin(phi) * math.cos(theta)
            estrela[1] = r * math.sin(phi) * math.sin(theta)
            estrela[2] = r * math.cos(phi)

def desenhar_estrelas(estrelas):
    """Desenha as estrelas ao redor da nave com rotação da câmera."""
    glPushMatrix()
    glRotatef(angle_x, 1, 0, 0)
    glRotatef(angle_y, 0, 1, 0)

    glBegin(GL_POINTS)
    glColor3f(*COR_ESTRELAS)
    for estrela in estrelas:
        glVertex3f(*estrela)
    glEnd()

    glPopMatrix()

def main():
    global dash_iniciado, dash_completado, dash_permitido, angle_x, angle_y, velocidade_fundo, posicao_nave_z

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -10)  # Inicialização da posição da câmera

    estrelas = gerar_estrelas(2000)  # Aumenta a quantidade inicial de estrelas

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if (evento.key == pygame.K_SPACE or evento.key == pygame.K_RETURN) and dash_permitido:
                    dash_iniciado = True  # Inicia o dash
                    dash_completado = False  # Reinicia o estado do dash

        # Checa o estado atual das teclas para rotacionar a nave
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            angle_x += rotation_speed  # Rotação para cima
        if keys[pygame.K_s]:
            angle_x -= rotation_speed  # Rotação para baixo
        if keys[pygame.K_a]:
            angle_y += rotation_speed  # Rotação para a esquerda
        if keys[pygame.K_d]:
            angle_y -= rotation_speed  # Rotação para a direita

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        # A câmera permanece fixa

        # Desenha as estrelas e atualiza sua posição conforme o movimento
        desenhar_estrelas(estrelas)
        atualizar_estrelas(estrelas, velocidade_fundo)

        # Exibe a nave enquanto o dash não foi completado
        if not dash_completado:
            glPushMatrix()
            # Aplica rotação da nave em torno dos eixos X e Y
            glTranslatef(0.0, 0.0, posicao_nave_z)  # Posição da nave
            glRotatef(-90, 1, 0, 0)  # Rotação inicial da nave para a posição correta
            glRotatef(angle_x, 1, 0, 0)  # Rotação pelo eixo X (para cima e para baixo)
            glRotatef(angle_y, 0, 1, 0)  # Rotação pelo eixo Y (para esquerda e direita)

            desenhar_corpo_central_unico(1.5, 1.5, 0.2, 50)
            desenhar_cauda()

            glPopMatrix()

        glPopMatrix()

        # Movimento da nave durante o dash
        if dash_iniciado:
            posicao_nave_z += velocidade_dash
            if posicao_nave_z > 5:  # Aproxima a nave bem perto da tela antes de sumir
                dash_completado = True  # Marca o dash como concluído
                dash_iniciado = False
                dash_permitido = False  # Impede que o dash seja reiniciado
                posicao_nave_z = -5  # Reseta a posição da nave para uma próxima vez
        else:
            velocidade_fundo = velocidade_normal

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()