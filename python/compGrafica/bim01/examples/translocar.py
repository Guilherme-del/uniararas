from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Função para desenhar um retângulo
def draw_rect(x, y, width, height, color):
    glBegin(GL_QUADS)
    glColor3f(*color)  # Define a cor
    glVertex2f(x, y)  # Inferior esquerdo
    glVertex2f(x + width, y)  # Inferior direito
    glVertex2f(x + width, y + height)  # Superior direito
    glVertex2f(x, y + height)  # Superior esquerdo
    glEnd()

# Função para desenhar um triângulo
def draw_triangle(x1, y1, x2, y2, x3, y3, color):
    glBegin(GL_TRIANGLES)
    glColor3f(*color)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

# Função para desenhar um círculo
def draw_circle(x, y, radius, color, num_segments=100):
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(*color)
    glVertex2f(x, y)  # Centro do círculo
    for i in range(num_segments + 1):
        theta = 2.0 * math.pi * i / num_segments
        dx = radius * math.cos(theta)
        dy = radius * math.sin(theta)
        glVertex2f(x + dx, y + dy)
    glEnd()

# Função para desenhar um quadrado (equivalente a um retângulo)
def draw_square(x, y, size, color):
    draw_rect(x, y, size, size, color)

# Função que será chamada para desenhar a cada frame
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Desenhar formas em diferentes posições
    glPushMatrix()
    glTranslatef(-1.5, 0.5, 0)  # Move para a posição desejada
    draw_rect(0, 0, 1, 0.5, (1, 0, 0))  # Retângulo vermelho
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.5, 0.5, 0)  # Move para outra posição
    draw_triangle(-0.5, 0, 0.5, 0, 0, 1, (0, 1, 0))  # Triângulo verde
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, -1, 0)  # Move para outra posição
    draw_circle(0, 0, 0.3, (0, 0, 1))  # Círculo azul
    glPopMatrix()

    glPushMatrix()
    glTranslatef(2, -1.5, 0)  # Move para outra posição
    draw_square(0, 0, 0.5, (1, 1, 0))  # Quadrado amarelo
    glPopMatrix()

    glutSwapBuffers()

# Função para configurar a janela e o OpenGL
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Define a cor de fundo como preto
    gluOrtho2D(-4, 4, -3, 3)  # Define a projeção ortográfica para coordenadas 2D

# Função principal para inicializar o OpenGL e a janela
def main():
    glutInit()  # Inicializa o GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Configura o modo de display (duplo buffer e RGB)
    glutInitWindowSize(800, 600)  # Configura o tamanho da janela
    glutCreateWindow(b"OpenGL Shapes")  # Cria a janela

    init()  # Chama a função de inicialização

    glutDisplayFunc(display)  # Define a função de display (o que será desenhado)
    glutIdleFunc(display)  # Atualiza continuamente a tela

    glutMainLoop()  # Entra no loop principal do GLUT

main()
