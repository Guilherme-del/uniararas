"""
USS Firebrand (NCC-68723)
Autor: 
Guilherme Cavenaghi
109317
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import random

# Control variables for ship movement
pos_inicial_x = 50
pos_final_x = -20
pos_inicial_y = -80
pos_final_y = -160
viajem = 0 
escala = 1.0

# Color palette
COR_CORPO = (0.5, 0.5, 0.6)
COR_DETALHES = (0.3, 0.3, 0.4)
COR_COCKPIT = (0.2, 0.2, 0.2)
COR_ESTRELAS = (1, 1, 1)
COR_LARANJA = (1, 0.5, 0)
COR_FAIXAS = (0.3, 0.3, 1)

# Movement speed variables
velocidade_fundo = 0.02  # Velocidade inicial do movimento do fundo

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

def desenha_nave():
    glutInit()
    glPushMatrix()
    glTranslatef(0, -1, -40)
    glRotatef(90, 1, 0, 0)
    glColor3f(*COR_CORPO)
    gluCylinder(gluNewQuadric(), 0, 10, 1, 40, 40)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, -0.2, -40)
    glRotatef(90, 1, 0, 0)
    glColor3f(*COR_CORPO)
    gluCylinder(gluNewQuadric(), 0, 2, 1, 40, 40)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0, -0.8, -40)
    glRotatef(90, 1, 0, 0)
    glColor3f(*COR_CORPO)
    gluCylinder(gluNewQuadric(), 2, 4, 1, 40, 40)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, -1, -40)
    glRotatef(90, 1, 0, 0)
    glColor3f(*COR_COCKPIT)
    gluSphere(gluNewQuadric(), 1, 50, 50)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, -2, -40)
    glRotatef(90, 1, 0, 0)
    glColor3f(*COR_CORPO)
    gluCylinder(gluNewQuadric(), 10, 0, 1, 40, 40)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(9, -9, -40)
    glRotatef(-45,0,0,1)
    glColor3f(*COR_CORPO)
    glBegin(GL_QUADS)
    glVertex3f(-10, 0.0, 0.5)
    glVertex3f(0, 0.0, 0.5)
    glVertex3f(5, 5.0, 0.5)
    glVertex3f(-5, 5.0, 0.5)
    glVertex3f(-10, 0.0, -0.5)
    glVertex3f(0, 0.0, -0.5)
    glVertex3f(5, 5.0, -0.5)
    glVertex3f(-5, 5.0, -0.5)
    glEnd()
    glBegin(GL_QUADS)
    glVertex3f(-5, 5.0, -0.7)
    glVertex3f(5, 5.0, -0.7)
    glVertex3f(5, 5, 0.7)
    glVertex3f(-5, 5, 0.7)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(9, -13, -40)
    glColor3f(*COR_CORPO)
    glBegin(GL_QUADS)
    glVertex3f(-6, 0.0, 0)
    glVertex3f(0, 0.0, 0)
    glVertex3f(6, 5, 0)
    glVertex3f(-0, 5, 0)
    glEnd()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(5, -9, -40)
    glRotatef(90,0,1,0)
    glColor3f(*COR_CORPO)
    gluCylinder(gluNewQuadric(), 2.5, 3, 35, 35, 35)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(6, -9, -40)
    glRotatef(90,0,1,0)
    glColor3f(*COR_LARANJA)
    gluCylinder(gluNewQuadric(), 2.55, 2.55, 1, 40, 40)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(4.5, -9, -39)
    glRotatef(90,0,1,0)
    glColor3f(*COR_FAIXAS)
    gluCylinder(gluNewQuadric(), 1.5, 2, 35, 35, 35)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(4.5, -9, -41)
    glRotatef(90,0,1,0)
    glColor3f(*COR_FAIXAS)
    gluCylinder(gluNewQuadric(), 1.5, 2, 35, 35, 35)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(5, -9, -40)
    glRotatef(90,0,1,0)
    glColor3f(*COR_CORPO)
    gluSphere(gluNewQuadric(), 2.5, 50, 50)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(40, -9, -40)
    glRotatef(90,0,1,0)
    glColor3f(*COR_CORPO)
    gluSphere(gluNewQuadric(), 3, 50, 50)
    glPopMatrix()

def main():
    global velocidade_fundo, posicao_nave_z, dash_tempo
    global pos_inicial_x, pos_final_x, pos_inicial_y, pos_final_y, viajem, escala

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    glTranslatef(0, 0, -50)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, display[0] / display[1], 0.1, 200.0)
    glMatrixMode(GL_MODELVIEW)
    estrelas = gerar_estrelas(200)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Limpar buffers
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Desenhar estrelas e atualizar posições
        desenhar_estrelas(estrelas)
        atualizar_estrelas(estrelas, velocidade_fundo)

        # Aplica as movimentações da nave
        glPushMatrix()
        if (pos_inicial_x !=  pos_final_x):
            pos_inicial_x -= 0.5
        
        if (pos_inicial_x == pos_final_x and pos_inicial_y != pos_final_y):
            pos_final_y += 0.5

        glRotatef(pos_final_y,0,1,0)
        glTranslatef(pos_inicial_x,0,20)

        if (pos_inicial_x == pos_final_x and pos_inicial_y == pos_final_y):
            if (viajem >= -10): 
                viajem -= 0.1
                glTranslatef(viajem,0,0)
            else: 
                viajem -= 1
                if (escala > 0):
                   escala -= 0.09
                glTranslatef(viajem,0,0)
                glScalef(escala, escala, escala)
        if (not escala < 0):
            desenha_nave()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
