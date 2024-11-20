import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Variáveis para controlar a rotação do cubo
rotation_x = 0
rotation_y = 0
rotation_speed = 2  # Velocidade de rotação do cubo

# Variáveis para controlar a translação do cubo
cube_position_x = 0.0  # Posição inicial do cubo no eixo X
cube_position_z = -5.0  # Posição inicial do cubo no eixo Z
cube_speed_x = 0.015  # Velocidade do movimento do cubo no eixo X
cube_speed_z = 0.025  # Velocidade do movimento do cubo no eixo Z
multiplier = 2000
px = 30
py = -30
pz = 0
direcao = 0
faixa1 = 40
faixa2 = -40
rotacaoy = 0
subir = 0
last_x = 0
last_y = 0
zoom = -30  # Para controlar o zoom


especularidade = [1.0, 1.0, 1.0, 1.0]
especMaterial = 60

# Visibilidade do cubo
cube_visible = True

# Número de estrelasa
num_stars = 20000

# Função para desenhar um cubo
def draw_cube():
    glutInit()

    glColor3f(0.5, 0.5, 0.5)

    glRotatef(px, 0, 0, 0)  # Rotaciona em relação ao eixo X
    glRotatef(py, 0, 0, 0)  # Rotaciona em relação ao eixo Y
    glTranslatef(0, subir, zoom)  # Aplica o zoom


    glPushMatrix()
    glTranslatef(0, 0.2, 0)
    glRotatef(90, 1, 0, 0)
    gluSphere(gluNewQuadric(), 13, 50, 50)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, -3, 0)
    glRotatef(90, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 2.5, 2.5, 35, 35, 35)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(35, -7.5, 0)
    glRotatef(90, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 7, 7, 40, 40, 40)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(32, -7.5, 0)
    glRotatef(90, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 4, 7, 10, 40, 40)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(29, -7.5, 0)
    glRotatef(90, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 4, 4, 5, 40, 40)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(30, 4, 10)  # Posiciona a coluna na traseira e abaixo da esfera central
    glRotatef(-35, 1, 0, 0)       # Inclina a coluna na diagonal
    glRotatef(90, 0, 0, 1)       # Inclina a coluna na diagonal
    glScalef(0.65, 2.0, 20)      # Torna a coluna mais larga e em forma de cuboide
    glColor3f(0.5, 0.5, 0.5)  # Cor cinza para a coluna
    glutSolidCube(1)  # Cria um cubo sólido com tamanho 1 para representar a coluna
    glPopMatrix()

    glPushMatrix()
    glTranslatef(25, 11, 20)
    glRotatef(90, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 2, 2, 40, 40, 40)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(30, 4, -10)  # Posiciona a coluna na traseira e abaixo da esfera central
    glRotatef(35, 1, 0, 0)       # Inclina a coluna na diagonal
    glRotatef(90, 0, 0, 1)       # Inclina a coluna na diagonal
    glScalef(0.65, 2.0, 20)      # Torna a coluna mais larga e em forma de cuboide
    glColor3f(0.5, 0.5, 0.5)  # Cor cinza para a coluna
    glutSolidCube(1)  # Cria um cubo sólido com tamanho 1 para representar a coluna
    glPopMatrix()

    glPushMatrix()
    glTranslatef(25, 11, -20)
    glRotatef(90, 0, 1, 0)
    gluCylinder(gluNewQuadric(), 2, 2, 40, 40, 40)
    glPopMatrix()




# Função para gerar estrelas aleatórias
def generate_stars():
    stars = []
    for _ in range(num_stars):
        # Estrelas em uma faixa aleatória de coordenadas 3D
        x = random.uniform(-300, 300)
        y = random.uniform(-300, 300)
        z = random.uniform(-300, 300)
        stars.append((x, y, z))
    return stars

# Função para desenhar as estrelas
def draw_stars(stars):
    glPointSize(2)  # Define o tamanho dos pontos
    glBegin(GL_POINTS)
    for star in stars:
        glVertex3f(star[0], star[1], star[2])
    glEnd()

def setupLighting():
    # Configura a luz e os parâmetros de material para o efeito 3D
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, [10.0, 10.0, 10.0, 1.0])  # Posição da luz
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])       # Luz ambiente fraca
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])       # Luz difusa
    glMaterialfv(GL_FRONT, GL_SPECULAR, especularidade)          # Material especular
    glMateriali(GL_FRONT, GL_SHININESS, especMaterial)           # Brilho do material

# Função de inicialização do OpenGL
def init_opengl(width, height):
    glEnable(GL_DEPTH_TEST)  # Habilita o teste de profundidade
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Define a cor de fundo (preto)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, width / height, 0.1, 200.0)  # Configura perspectiva
    glMatrixMode(GL_MODELVIEW)

# Função para renderizar a cena
def render_scene(stars):
    global cube_visible, cube_position_x, cube_position_z

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Limpa a tela e o buffer de profundidade
    glLoadIdentity()
    
    # Desenha as estrelas
    glColor3f(1, 1, 1)  # Cor branca para as estrelas

    draw_stars(stars)

    # Translação do cubo ao longo dos eixos X e Z
    glTranslatef(cube_position_x, 0.0, cube_position_z)  # Move o cubo ao longo dos eixos X e Z

    # Aplica a rotação do cubo
    glRotatef(rotation_x, 1, 0, 0)  # Rotação no eixo X
    glRotatef(rotation_y, 0, 1, 0)  # Rotação no eixo Y
    
    # Desenha o cubo
    if cube_visible:
        glTranslatef(-40, -20, -150)
        glRotatef(90, 0, 1, 0)
        glRotatef(140, 0, 1, 0)
        draw_cube()
    
    pygame.display.flip()  # Atualiza a tela

# Função principal
def main():
    global rotation_x, rotation_y, cube_position_x, cube_position_z, cube_speed_x, cube_speed_z, cube_visible, multiplier

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)  # Cria a janela com OpenGL
    init_opengl(display[0], display[1])  # Inicializa OpenGL
    setupLighting()

    # Gera as estrelas
    stars = generate_stars()
    clock = pygame.time.Clock()

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # Captura as teclas pressionadas para rotação do cubo
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:  # Tecla W (rotação no eixo X)
            rotation_x += rotation_speed
        if keys[pygame.K_s]:  # Tecla S (rotação no eixo X)
            rotation_x -= rotation_speed
        if keys[pygame.K_a]:  # Tecla A (rotação no eixo Y)
            rotation_y += rotation_speed
        if keys[pygame.K_d]:  # Tecla D (rotação no eixo Y)
            rotation_y -= rotation_speed

        # print("Posição z", cube_position_z)
        if (cube_position_x <= 7 and cube_position_z >= -15):
            cube_position_x += cube_speed_x  # Movendo o cubo ao longo do eixo X
            cube_position_z -= cube_speed_z  # Movendo o cubo para o fundo ao longo do eixo Z
        else:
            cube_position_x += cube_speed_x * multiplier # Simula a velocidade de salto
            cube_position_z -= cube_speed_z * multiplier # Simula a velocidade de salto
            if (cube_position_x >= 50 and cube_position_z <= -100):
                # Depois de um avanço deixa a velocidade lenta     para manter o movimento das estrelas
                cube_speed_x = 0.01 
                cube_speed_z = 0.01
                multiplier = 1
                # Apaga a nave da cena
                cube_visible = False

        render_scene(stars)  # Desenha a cena com as estrelas
        clock.tick(60)  # Limita o FPS para 60

main()