'''
Prova P1 Computação Gráfica
Guilherme Cavenaghi - 109317
Movimentação - A W S D ou SETINHAS
Seleção de Peça - F1
'''

from OpenGL.GL import *
from OpenGL.GLUT import *

W, H = 500, 500
x_pos, y_pos,  = 128, 128

dama_azul_posicaox = [116, 180, 244, 308]
dama_azul_posicaoy = 340

dama_vermelha_posicaox = [148, 212, 276, 340]
dama_vermelha_posicaoy = 116

corBlue = (0, 0, 1)
corRed = (1, 0, 0)

blue_1 = [148, 116, corBlue]
blue_2 = [212 , 116, corBlue]
blue_3 = [276, 116, corBlue]
blue_4 = [340, 116, corBlue]
blue_5 = [116, 148, corBlue]
blue_6 = [180, 148, corBlue]
blue_7 = [244, 148, corBlue]
blue_8 = [308, 148, corBlue]
blue_9 = [148, 180, corBlue]
blue_10 =[212, 180, corBlue] 
blue_11 =[276, 180, corBlue] 
blue_12 =[340, 180, corBlue]

red_1 = [116, 276, corRed]
red_2 =[180, 276, corRed]
red_3 =[244, 276, corRed]
red_4 =[308, 276, corRed]
red_5 =[148, 308, corRed]
red_6 =[212, 308, corRed]
red_7 =[276, 308, corRed]
red_8 =[340, 308, corRed]
red_9 =[116, 340, corRed]
red_10 =[180, 340, corRed]
red_11 =[244, 340, corRed]
red_12 =[308, 340, corRed]

todasPecas = [blue_1,
             blue_2,
             blue_3,
             blue_4,
             blue_5,
             blue_6,
             blue_7,
             blue_8,
             blue_9,
             blue_10,
             blue_11,
             blue_12,
             red_1,
             red_2,
             red_3,
             red_4,
             red_5,
             red_6,
             red_7,
             red_8,
             red_9,
             red_10,
             red_11,
             red_12
             ]
pecaSelecionada = []

# Tabuleiro
def tabuleiro():
    posy = 0
    posx1, posx2 = 0, 0
    glColor3f(0.5, 0.50, 0.5)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(W, 0)
    glVertex2f(W, H)
    glVertex2f(0, H)
    glEnd()
    for e in range(8):
        if e % 2 == 1:
            posx1 = 32
        if e % 2 == 0:
            posx2 = 32
        for i in range(4):
            
            glColor3f(1, 1, 1)
            glBegin(GL_QUADS)
            glVertex2f(100 + posx1, 100 + posy)
            glVertex2f(132 + posx1, 100 + posy)
            glVertex2f(132 + posx1, 132 + posy)
            glVertex2f(100 + posx1, 132 + posy)
            glEnd()
            posx1 += 64
        for i in range(4):
            
            glColor3f(0, 0, 0)
            glBegin(GL_QUADS)
            glVertex2f(100 + posx2, 100 + posy)
            glVertex2f(132 + posx2, 100 + posy)
            glVertex2f(132 + posx2, 132 + posy)
            glVertex2f(100 + posx2, 132 + posy)
            glEnd()
            posx2 += 64
        posx1, posx2 = 0, 0
        posy += 32
    
# Peças
def quadrado(posX, posY, color=(1, 1, 1)):
    glColor3f(*color)
    glBegin(GL_QUADS)

    half_size = 12
    glVertex2f(posX - half_size, posY - half_size)
    glVertex2f(posX - half_size, posY + half_size)
    glVertex2f(posX + half_size, posY + half_size)
    glVertex2f(posX + half_size, posY - half_size)
    glEnd()

def pecasAzuis():
    quadrado(blue_1[0], blue_1[1], color=blue_1[2])

    quadrado(blue_2[0], blue_2[1], color=blue_2[2])
    quadrado(blue_3[0], blue_3[1], color=blue_3[2])
    quadrado(blue_4[0], blue_4[1], color=blue_4[2])
    quadrado(blue_5[0], blue_5[1], color=blue_5[2])

    quadrado(blue_6[0], blue_6[1], color=blue_6[2])
    quadrado(blue_7[0], blue_7[1], color=blue_7[2])
    quadrado(blue_8[0], blue_8[1], color=blue_8[2])

    quadrado(blue_9[0], blue_9[1], color=blue_9[2])
    quadrado(blue_10[0], blue_10[1], color=blue_10[2])
    quadrado(blue_11[0], blue_11[1], color=blue_11[2])
    quadrado(blue_12[0], blue_12[1], color=blue_12[2])

def pecasVermelhas():
    quadrado(red_1[0], red_1[1], color=red_1[2]) 
    quadrado(red_2[0], red_2[1], color=red_2[2])
    quadrado(red_3[0], red_3[1], color=red_3[2])
    quadrado(red_4[0], red_4[1], color=red_4[2])

    quadrado(red_5[0], red_5[1], color=red_5[2])
    quadrado(red_6[0], red_6[1], color=red_6[2])
    quadrado(red_7[0], red_7[1], color=red_7[2])
    quadrado(red_8[0], red_8[1], color=red_8[2])

    quadrado(red_9[0], red_9[1], color=red_9[2])
    quadrado(red_10[0], red_10[1], color=red_10[2])
    quadrado(red_11[0], red_11[1], color=red_11[2])
    quadrado(red_12[0], red_12[1], color=red_12[2])




# Seleção Peças
def selecionarPeca():
    glColor3f(0, 1, 0)
    glBegin(GL_QUADS)
    glVertex2f(104 + x_pos, 104 + y_pos)
    glVertex2f(128 + x_pos, 104 + y_pos)
    glVertex2f(128 + x_pos, 128 + y_pos)
    glVertex2f(104 + x_pos, 128 + y_pos)
    glEnd()
    


def key_callback(key, x, y):
    global x_pos, y_pos
    if (key == GLUT_KEY_LEFT or key == b'a') and x_pos > 0:
        x_pos = x_pos-32
    elif (key == GLUT_KEY_RIGHT or key == b'd') and x_pos < 224:
        x_pos = x_pos+32
    elif (key == GLUT_KEY_UP or key == b'w') and y_pos < 224:
        y_pos = y_pos+32
    elif (key == GLUT_KEY_DOWN or key == b's') and y_pos > 0:
        y_pos = y_pos-32
    elif (key == GLUT_KEY_F1):
            # SÓ SELECIONA SE NÃO HOUVER NENHUMA SELECIONADA
        if(len(pecaSelecionada) == 0):
            for peca in todasPecas:
                if(x_pos + 116 == peca[0] and y_pos + 116 == peca[1]):
                    print("Selecionado peça: ", peca)
                    pecaSelecionada.append(peca)
                    print(pecaSelecionada)
    elif (key == GLUT_KEY_F2):
        print("Entrei na etapa de posicionar")
        if(len(pecaSelecionada) == 0):
            print("Selecione uma peça para mover.")
        else:
            for peca in todasPecas:
                if(len(pecaSelecionada) > 0): 
                    if(pecaSelecionada[0][0] == peca[0] and pecaSelecionada[0][1] == peca[1]):
                        print("Posição OLD")
                        print("[OLD] piece[0]: ", peca[0])
                        print("[OLD] piece[1]: ", peca[1])

                        peca[0], peca[1] = x_pos + 116, y_pos + 116

                        print("Posição NEW")
                        print("[NEW] piece[0]: ", peca[0])
                        print("[NEW] piece[1]: ", peca[1])
                        
                        if (peca[1] == dama_azul_posicaoy and peca[0] in dama_azul_posicaox):
                            print("F3 agora é uma dama")
                            peca[2] = (0, 1, 1)
                        if (peca[1] == dama_vermelha_posicaoy and peca[0] in dama_vermelha_posicaox):
                            print("F3 agora é uma dama")
                            peca[2] = (1, 1, 0)
                        # Limpa seleção de peça
                        pecaSelecionada.pop(0)
                               
def iterate():
    glViewport(0, 0, W, H)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, W, 0.0, H, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    tabuleiro()
    pecasAzuis()
    pecasVermelhas()
    selecionarPeca()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(W, H)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Jogo Damas - P1")
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutSpecialFunc(key_callback)
    glutKeyboardFunc(key_callback)
    glutMainLoop()

if __name__ == "__main__":
    main()