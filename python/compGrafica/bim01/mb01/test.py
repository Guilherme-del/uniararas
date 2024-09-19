import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu

def init():
    gl.glClearColor(0.53, 0.81, 0.92, 1)  # Cor de fundo: céu azul claro
    gl.glOrtho(-500, 500, -500, 500, -1, 1)  # Definir sistema de coordenadas

def desenha_grama():
    gl.glColor3f(0.0, 0.5, 0.0)  # Cor verde para a grama
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(-500, -200)
    gl.glVertex2f(500, -200)
    gl.glVertex2f(500, -500)
    gl.glVertex2f(-500, -500)
    gl.glEnd()

def desenha_sol():
    gl.glColor3f(1.0, 1.0, 0.0)  # Cor amarela para o sol
    gl.glBegin(gl.GL_POLYGON)
    for i in range(100):
        angle = 2 * 3.14159 * i / 100
        x = 80 * cos(angle)
        y = 80 * sin(angle)
        gl.glVertex2f(x + 350, y + 350)
    gl.glEnd()

def desenha_telhado():
    gl.glColor3f(0.55, 0.27, 0.07)  # Cor marrom para o telhado
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(-200, 100)
    gl.glVertex2f(0, 250)
    gl.glVertex2f(200, 100)
    gl.glEnd()

    gl.glColor3f(0.65, 0.16, 0.16)  # Cor vermelha para o segundo telhado
    gl.glBegin(gl.GL_TRIANGLES)
    gl.glVertex2f(-150, 50)
    gl.glVertex2f(0, 150)
    gl.glVertex2f(150, 50)
    gl.glEnd()

def desenha_casa():
    gl.glColor3f(0.9, 0.9, 0.9)  # Cor branca para a casa
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(-200, -100)
    gl.glVertex2f(200, -100)
    gl.glVertex2f(200, 100)
    gl.glVertex2f(-200, 100)
    gl.glEnd()

def desenha_janela():
    gl.glColor3f(0.0, 0.5, 0.8)  # Cor azul para a janela
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(-150, 0)
    gl.glVertex2f(-50, 0)
    gl.glVertex2f(-50, 50)
    gl.glVertex2f(-150, 50)
    gl.glEnd()

def desenha_porta():
    gl.glColor3f(0.6, 0.3, 0.0)  # Cor marrom para a porta
    gl.glBegin(gl.GL_QUADS)
    gl.glVertex2f(50, -100)
    gl.glVertex2f(150, -100)
    gl.glVertex2f(150, 0)
    gl.glVertex2f(50, 0)
    gl.glEnd()

def desenha_cenario():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    desenha_grama()
    desenha_sol()
    desenha_casa()
    desenha_telhado()
    desenha_janela()
    desenha_porta()
    gl.glFlush()

def main():
    glut.glutInit()
    glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
    glut.glutInitWindowSize(500, 500)
    glut.glutInitWindowPosition(100, 100)
    glut.glutCreateWindow(b"Casa 2D OpenGL")
    init()
    glut.glutDisplayFunc(desenha_cenario)
    glut.glutMainLoop()

if __name__ == "_main_":
    main()