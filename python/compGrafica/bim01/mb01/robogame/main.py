import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import cos, sin, atan2, degrees

# Função para desenhar a grade do campo de batalha
def draw_grid():
    glColor3f(0.1, 0.1, 0.5)  # Cor azul escura para a grade
    glBegin(GL_LINES)
    for i in range(-5, 6):
        glVertex3f(i, -5, 0)
        glVertex3f(i, 5, 0)
        glVertex3f(-5, i, 0)
        glVertex3f(5, i, 0)
    glEnd()

# Função para desenhar um tanque
def draw_tank(x, y, color, angle=0):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glRotatef(angle, 0, 0, 1)  # Rotacionar o tanque
    glColor3f(*color)  # Definir a cor do tanque
    glBegin(GL_QUADS)
    # Corpo do tanque
    glVertex3f(-0.3, -0.3, 0)
    glVertex3f(0.3, -0.3, 0)
    glVertex3f(0.3, 0.3, 0)
    glVertex3f(-0.3, 0.3, 0)
    
    # Torre do tanque
    glVertex3f(-0.1, 0.3, 0)
    glVertex3f(0.1, 0.3, 0)
    glVertex3f(0.1, 0.6, 0)
    glVertex3f(-0.1, 0.6, 0)
    glEnd()
    glPopMatrix()

# Função para desenhar uma explosão
def draw_explosion(x, y, size=0.2):
    glPushMatrix()
    glTranslatef(x, y, 0)
    glColor3f(1, 0.5, 0)  # Cor laranja para a explosão
    glBegin(GL_TRIANGLE_FAN)
    for angle in range(0, 360, 10):
        rad = angle * 3.14159 / 180
        glVertex3f(size * cos(rad), size * sin(rad), 0)
    glEnd()
    glPopMatrix()

# Função para calcular o ângulo entre dois pontos (tanques)
def calculate_angle(x1, y1, x2, y2):
    return degrees(atan2(y2 - y1, x2 - x1)) - 90  # Subtrair 90 graus para ajustar para a direita

# Função principal
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -7)

    # Posições dos tanques e explosões
    tanks = [
        {"pos": (-2, -2), "color": (1, 0, 0)},  # Vermelho
        {"pos": (2, 2), "color": (0, 1, 0)},   # Verde
        {"pos": (-3, 1), "color": (0, 0, 1)},  # Azul
    ]
    
    explosions = [{"pos": (-2, -2), "size": 0.2}]  # A explosão começa na posição do tanque vermelho
    explosion_velocity = [0.02, 0.02]  # Velocidade da explosão

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Desenha a grade do campo de batalha
        draw_grid()

        # Calcula o ângulo para o tanque vermelho apontar para o tanque verde
        if len(tanks) > 1:  # Certifica que o tanque verde ainda existe
            red_tank_pos = tanks[0]["pos"]
            green_tank_pos = tanks[1]["pos"]
            red_angle = calculate_angle(red_tank_pos[0], red_tank_pos[1], green_tank_pos[0], green_tank_pos[1])
        else:
            red_angle = 0  # Se o tanque verde for destruído, resetar o ângulo

        # Atualiza a posição da explosão, movendo-a em direção ao tanque verde
        if len(tanks) > 1:  # Certifica que o tanque verde ainda existe
            explosion = explosions[0]
            explosion["pos"] = (explosion["pos"][0] + explosion_velocity[0], explosion["pos"][1] + explosion_velocity[1])
            draw_explosion(explosion["pos"][0], explosion["pos"][1], explosion["size"])

            # Verifica se a explosão atingiu o tanque verde
            if abs(explosion["pos"][0] - green_tank_pos[0]) < 0.2 and abs(explosion["pos"][1] - green_tank_pos[1]) < 0.2:
                tanks.pop(1)  # Remove o tanque verde da lista

        # Desenha os tanques
        draw_tank(tanks[0]["pos"][0], tanks[0]["pos"][1], tanks[0]["color"], angle=red_angle)  # Tanque vermelho apontando para o verde
        
        if len(tanks) > 1:  # Só desenha o tanque verde se ele ainda existir
            draw_tank(tanks[1]["pos"][0], tanks[1]["pos"][1], tanks[1]["color"])  # Tanque verde
            
        if len(tanks) > 2:  # Certifica que o tanque azul ainda existe na lista
            draw_tank(tanks[-1]["pos"][0], tanks[-1]["pos"][1], tanks[-1]["color"], angle=45)  # Tanque azul inclinado

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()
