from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

# Tamanho do labirinto
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

posicao_jogador = [1, 1]  # Posição inicial do jogador
posicao_destino = [9, 8]  # Posição do destino (bloco verde)
largura_celula = 50
altura_celula = 50
venceu = False  # Variável para controlar a exibição da mensagem de vitória

# Função para desenhar texto na tela
def desenhar_texto(string, x, y):
    glColor3f(1.0, 0.0, 0.0)  # Cor do texto (vermelho)
    glRasterPos2f(x, y)
    for char in string:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

# Função para desenhar o labirinto
def desenhar_labirinto():
    glClear(GL_COLOR_BUFFER_BIT)
    for i in range(len(labirinto)):
        for j in range(len(labirinto[i])):
            x = j * largura_celula
            y = i * altura_celula
            
            # Desenhar paredes (1)
            if labirinto[i][j] == 1:
                glColor3f(0.5, 0.5, 0.5)
            # Desenhar caminho (0)
            else:
                glColor3f(1.0, 1.0, 1.0)
                
            # Desenhar retângulo
            glBegin(GL_QUADS)
            glVertex2f(x, y)
            glVertex2f(x + largura_celula, y)
            glVertex2f(x + largura_celula, y + altura_celula)
            glVertex2f(x, y + altura_celula)
            glEnd()
    
    # Desenhar jogador
    glColor3f(0.0, 0.0, 1.0)  # Azul para o jogador
    x_jogador = posicao_jogador[1] * largura_celula
    y_jogador = posicao_jogador[0] * altura_celula
    glBegin(GL_QUADS)
    glVertex2f(x_jogador, y_jogador)
    glVertex2f(x_jogador + largura_celula, y_jogador)
    glVertex2f(x_jogador + largura_celula, y_jogador + altura_celula)
    glVertex2f(x_jogador, y_jogador + altura_celula)
    glEnd()

    # Desenhar destino (sem bloquear)
    glColor3f(0.0, 1.0, 0.0)  # Verde para o destino
    x_destino = posicao_destino[1] * largura_celula
    y_destino = posicao_destino[0] * altura_celula
    glBegin(GL_QUADS)
    glVertex2f(x_destino, y_destino)
    glVertex2f(x_destino + largura_celula, y_destino)
    glVertex2f(x_destino + largura_celula, y_destino + altura_celula)
    glVertex2f(x_destino, y_destino + altura_celula)
    glEnd()

    # Verificar se o jogador venceu
    if venceu:
        desenhar_texto("Parabéns! Você venceu!", 150, 275)
        glutSwapBuffers()
        time.sleep(2)
        glutLeaveMainLoop()

    glutSwapBuffers()

# Função para mover o jogador
def mover_jogador(key, x, y):
    global posicao_jogador, venceu
    i, j = posicao_jogador
    
    if key == b'w' and labirinto[i+1][j] == 0:  # Baixo
        posicao_jogador[0] += 1
    elif key == b's' and labirinto[i-1][j] == 0:  # Cima
        posicao_jogador[0] -= 1
    elif key == b'a' and labirinto[i][j-1] == 0:  # Esquerda
        posicao_jogador[1] -= 1
    elif key == b'd' and (labirinto[i][j+1] == 0 or [i, j+1] == posicao_destino):  # Direita
        posicao_jogador[1] += 1

    # Verifica se o jogador chegou ao destino após o movimento
    if posicao_jogador == posicao_destino:
        venceu = True

    glutPostRedisplay()

# Inicialização do OpenGL
def inicializar():
    glClearColor(0.8, 0.8, 0.8, 1.0)  # Cor de fundo cinza claro
    gluOrtho2D(0, 10 * largura_celula, 0, 11 * altura_celula)

# Main
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 550)
glutCreateWindow("Labirinto OpenGL")
glutDisplayFunc(desenhar_labirinto)
glutKeyboardFunc(mover_jogador)
inicializar()
glutMainLoop()