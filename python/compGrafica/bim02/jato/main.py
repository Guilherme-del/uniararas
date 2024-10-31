from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

name = 'F-35'
especularidade = [1.0,1.0,1.0,1.0]
especMaterial = 60
px = 30
py = -30
pz = 0
direcao = 0
faixa1 = 40
faixa2 = -40
rotacaoy = 0
subir = 0

def drawF35():

    glRotatef(px, 1, 0, 0) # Rotaciona em relação ao eixo X (Setas cima e baixo)
    glRotatef(py, 0, 1, 0) # Rotaciona em relação ao eixo Y (Setas direita e esquerda)
    glRotatef(pz, 0, 0, 1) # Rotaciona em relação ao eixo Z (teclas PgUp e PgDn)
    glTranslatef(0, subir, 0)
#----------------------------------------------------------------------------------------------

    glTranslatef(0, 0, -7)
    glColor3f(0.38,0.38,0.38)
    glTranslatef(0, 1.25, -1)
    gluCylinder(gluNewQuadric(), 1.25, 1.25, 14, 16, 16)
    glTranslatef(0, -1.25, 1)
    glTranslatef(0, 1.25, 13)
    gluCylinder(gluNewQuadric(), 1.25, 0.75, 2, 16, 16)
    glTranslatef(0, -1.25, -13)
    glTranslatef(0, 1.25, 15)
    gluCylinder(gluNewQuadric(), 0.75, 0.2, 1, 16, 16)
    glTranslatef(0, -1.25, -15)
    glTranslatef(0, 1.25, 16)
    gluCylinder(gluNewQuadric(), 0.2, 0, 0.25, 16, 16)
    glTranslatef(0, -1.25, -15)
    glColor3f(0.15,0.15,0.15)
    glTranslatef(0, 1.25, -3)
    gluCylinder(gluNewQuadric(), 0.5, 1.25, 1, 16, 16)
    glTranslatef(0, -1.25, 3)
    glColor3f(1,0.6,0.3)
    glTranslatef(0, 1.25, -1)
    gluSphere(gluNewQuadric(), 1.25, 8, 8)
    glTranslatef(0, -1.25, 1)
    #janela
    glColor3f(0.8,0.8,1)
    glTranslatef(0, 2.2, 13)
    gluSphere(gluNewQuadric(), 0.6, 8, 8)
    glTranslatef(0, -2.2, -13)
    glTranslatef(0, 2.5, 11)
    gluSphere(gluNewQuadric(), 0.6, 8, 8)
    glTranslatef(0, -2.5, -11)
    glTranslatef(0, 2.5, 11)
    glRotatef(8, 1, 0, 0)
    gluCylinder(gluNewQuadric(), 0.57, 0.57, 2.1, 16, 16)
    glRotatef(-8, 1, 0, 0)
    glTranslatef(0, -2.5, -11)
    #asa direita
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_POLYGON)
    glVertex3f(-2.36, 1.32, 6.72),
    glVertex3f(-2.36, 1.32, 0.0),
    glVertex3f(-7.44, 1.29, 1.26),
    glVertex3f(-7.44, 1.29, 3.36),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-2.32, 1.05, 0.0),
    glVertex3f(-2.32, 1.05, 6.72),
    glVertex3f(-7.44, 1.05, 3.36),
    glVertex3f(-7.44, 1.05, 1.26),
    glEnd()
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex3f(-2.32, 1.05, 6.72),
    glVertex3f(-2.36, 1.32, 6.72),
    glVertex3f(-7.44, 1.29, 3.36),
    glVertex3f(-7.44, 1.05, 3.36),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-7.44, 1.05, 1.26),
    glVertex3f(-7.44, 1.05, 3.36),
    glVertex3f(-7.44, 1.29, 3.36),
    glVertex3f(-7.44, 1.29, 1.26),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-7.44, 1.05, 1.26),
    glVertex3f(-7.44, 1.29, 1.26),
    glVertex3f(-2.36, 1.32, 0.0),
    glVertex3f(-2.32, 1.05, 0.0),
    glEnd()
    #Asa esquerda
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_POLYGON)
    glVertex3f(2.36, 1.32, 6.72),
    glVertex3f(7.44, 1.29, 3.36),
    glVertex3f(7.44, 1.29, 1.26),
    glVertex3f(2.36, 1.32, 0.0),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(2.32, 1.05, 0.0),
    glVertex3f(7.44, 1.05, 1.26),
    glVertex3f(7.44, 1.05, 3.36),
    glVertex3f(2.32, 1.05, 6.72),
    glEnd()
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex3f(2.32, 1.05, 6.72),
    glVertex3f(7.44, 1.05, 3.36),
    glVertex3f(7.44, 1.29, 3.36),
    glVertex3f(2.36, 1.32, 6.72),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(7.44, 1.05, 1.26),
    glVertex3f(7.44, 1.29, 1.26),
    glVertex3f(7.44, 1.29, 3.36),
    glVertex3f(7.44, 1.05, 3.36),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(7.44, 1.05, 1.26),
    glVertex3f(2.32, 1.05, 0.0),
    glVertex3f(2.36, 1.32, 0.0),
    glVertex3f(7.44, 1.29, 1.26),
    glEnd()
    #base
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex3f(-1.4, 1.32, 11.4),
    glVertex3f(-1.16, 1.61, 12.04),
    glVertex3f(-1.16, 1.61, -1.7),
    glVertex3f(-1.4, 1.32, -1.7),
    glEnd()
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    glVertex3f(-1.4, 1.32, 11.4),
    glVertex3f(-1.16, 1.61, 12.04),
    glVertex3f(-1.16, 1.32, 11.4),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(1.4, 1.32, 11.4),
    glVertex3f(1.16, 1.61, 12.04),
    glVertex3f(1.16, 1.32, 11.4),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-2.36, 1.32, -1.7),
    glVertex3f(-2.36, 1.12, -1.7),
    glVertex3f(-1.4, 1.12, -1.7),
    glVertex3f(-1.4, 1.32, -1.7),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(2.36, 1.32, -1.7),
    glVertex3f(2.36, 1.12, -1.7),
    glVertex3f(1.4, 1.12, -1.7),
    glVertex3f(1.4, 1.32, -1.7),
    glEnd()
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex3f(1.4, 1.32, 11.4),
    glVertex3f(1.4, 1.32, -1.7),
    glVertex3f(1.16, 1.61, -1.7),
    glVertex3f(1.16, 1.61, 12.04),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-1.4, 1.32, -1.7),
    glVertex3f(-1.16, 1.61, -1.7),
    glVertex3f(-0.92, 1.12, -1.7),
    glVertex3f(-1.4, 1.12, -1.7),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-1.4, 1.32, -1.7),
    glVertex3f(-1.16, 1.61, -1.7),
    glVertex3f(-0.92, 1.12, -1.7),
    glVertex3f(-1.4, 1.12, -1.7),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(1.4, 1.32, -1.7),
    glVertex3f(1.4, 1.12, -1.7),
    glVertex3f(0.92, 1.12, -1.7),
    glVertex3f(1.16, 1.61, -1.7),
    glEnd()
    glColor3f(0.35,0.35,0.35)
    glBegin(GL_POLYGON)
    glVertex3f(-1.4, 1.32, 11.4),
    glVertex3f(-1.4, 1.32, -1.7),
    glVertex3f(-2.36, 1.32, -1.7),
    glVertex3f(-2.36, 1.32, 11.4),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(1.4, 1.32, 11.4),
    glVertex3f(2.36, 1.32, 11.4),
    glVertex3f(2.36, 1.32, -1.7),
    glVertex3f(1.4, 1.32, -1.7),
    glEnd()
    glColor3f(0.3,0.3,0.3)
    glBegin(GL_POLYGON)
    glVertex3f(-2.0, 0.0, 0.0),
    glVertex3f(-2.32, 1.12, -1.7),
    glVertex3f(-0.92, 1.12, -1.7),
    glVertex3f(-0.6, 0.0, 0.0),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-2.36, 1.32, 0.0),
    glVertex3f(-2.36, 1.32, -1.7),
    glVertex3f(-2.32, 1.12, -1.7),
    glVertex3f(-2.0, 0.0, 0.0),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(2.0, 0.0, 0.0),
    glVertex3f(0.6, 0.0, 0.0),
    glVertex3f(0.92, 1.12, -1.7),
    glVertex3f(2.32, 1.12, -1.7),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(2.36, 1.32, 0.0),
    glVertex3f(2.0, 0.0, 0.0),
    glVertex3f(2.32, 1.12, -1.7),
    glVertex3f(2.36, 1.32, -1.7),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-2.36, 1.32, 11.4),
    glVertex3f(-2.36, 1.32, 0.0),
    glVertex3f(-2.0, 0.0, 0.0),
    glVertex3f(-2.0, 0.0, 10.5),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(2.36, 1.32, 11.4),
    glVertex3f(2.0, 0.0, 10.5),
    glVertex3f(2.0, 0.0, 0.0),
    glVertex3f(2.36, 1.32, 0.0),
    glEnd()
    glColor3f(0.2,0.2,0.2)
    glBegin(GL_POLYGON)
    glVertex3f(-2.0, 0.0, 10.5),
    glVertex3f(2.0, 0.0, 10.5),
    glVertex3f(2.0, 0.0, 0.0),
    glVertex3f(-2.0, 0.0, 0.0),
    glEnd()
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_POLYGON)
    glVertex3f(2.36, 1.32, 11.4),
    glVertex3f(-2.36, 1.32, 11.4),
    glVertex3f(-2.0, 0.0, 10.5),
    glVertex3f(2.0, 0.0, 10.5),
    glEnd()  
    #asa traseira direita
    glTranslatef(0, 1.22, -1.7)
    glRotate(rotacaoy, 1, 0, 0)
    glTranslatef(0, -1.22, 1.7)
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_POLYGON)
    glVertex3f(-1.4, 1.12, -1.7),
    glVertex3f(-1.4, 1.12, -3.84),
    glVertex3f(-4.45, 1.12, -3.84),
    glVertex3f(-4.45, 1.12, -2.64),
    glVertex3f(-2.36, 1.12, -1.7),  
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-1.4, 1.32, -1.7),
    glVertex3f(-1.4, 1.32, -3.84),
    glVertex3f(-4.45, 1.32, -3.84),
    glVertex3f(-4.45, 1.32, -2.64),
    glVertex3f(-2.36, 1.32, -1.7),  
    glEnd()
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex3f(-2.36, 1.32, -1.7),
    glVertex3f(-2.36, 1.12, -1.7),
    glVertex3f(-1.4, 1.12, -1.7),
    glVertex3f(-1.4, 1.32, -1.7),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-2.36, 1.32, -1.7),
    glVertex3f(-4.45, 1.32, -2.64),
    glVertex3f(-4.45, 1.12, -2.64),
    glVertex3f(-2.36, 1.12, -1.7),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-4.45, 1.12, -3.84),
    glVertex3f(-4.45, 1.12, -2.64),
    glVertex3f(-4.45, 1.32, -2.64),
    glVertex3f(-4.45, 1.32, -3.84),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-4.45, 1.12, -3.84),
    glVertex3f(-4.45, 1.32, -3.84),
    glVertex3f(-1.4, 1.32, -3.84),
    glVertex3f(-1.4, 1.12, -3.84),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-1.4, 1.12, -3.84),
    glVertex3f(-1.4, 1.32, -3.84),
    glVertex3f(-1.4, 1.32, -1.7),
    glVertex3f(-1.4, 1.12, -1.7),
    glEnd()
    glTranslatef(0, 1.22, -1.7)
    glRotate(-rotacaoy, 1, 0, 0)
    glTranslatef(0, -1.22, 1.7)
    #asa traseira esquerda
    glTranslatef(0, 1.22, -1.7)
    glRotate(rotacaoy, 1, 0, 0)
    glTranslatef(0, -1.22, 1.7)
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_POLYGON)
    glVertex3f(1.4, 1.12, -1.7),
    glVertex3f(1.4, 1.12, -3.84),
    glVertex3f(4.45, 1.12, -3.84),
    glVertex3f(4.45, 1.12, -2.64),
    glVertex3f(2.36, 1.12, -1.7),  
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(1.4, 1.32, -1.7),
    glVertex3f(1.4, 1.32, -3.84),
    glVertex3f(4.45, 1.32, -3.84),
    glVertex3f(4.45, 1.32, -2.64),
    glVertex3f(2.36, 1.32, -1.7),  
    glEnd()
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex3f(2.36, 1.32, -1.7),
    glVertex3f(2.36, 1.12, -1.7),
    glVertex3f(1.4, 1.12, -1.7),
    glVertex3f(1.4, 1.32, -1.7),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(2.36, 1.32, -1.7),
    glVertex3f(4.45, 1.32, -2.64),
    glVertex3f(4.45, 1.12, -2.64),
    glVertex3f(2.36, 1.12, -1.7),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(4.45, 1.12, -3.84),
    glVertex3f(4.45, 1.12, -2.64),
    glVertex3f(4.45, 1.32, -2.64),
    glVertex3f(4.45, 1.32, -3.84),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(4.45, 1.12, -3.84),
    glVertex3f(4.45, 1.32, -3.84),
    glVertex3f(1.4, 1.32, -3.84),
    glVertex3f(1.4, 1.12, -3.84),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(1.4, 1.12, -3.84),
    glVertex3f(1.4, 1.32, -3.84),
    glVertex3f(1.4, 1.32, -1.7),
    glVertex3f(1.4, 1.12, -1.7),
    glEnd()
    glTranslatef(0, 1.22, -1.7)
    glRotate(-rotacaoy, 1, 0, 0)
    glTranslatef(0, -1.22, 1.7)
    #asa traseira vertical esquerda
    glTranslatef(1.85, 1.25, 0)
    glRotatef(-10, 0, 0, 1)
    glRotatef(direcao, 0, 1, 0)
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_POLYGON)
    glVertex3f(0.1, 0, 1.5),
    glVertex3f(0.1, 0, -1.5),
    glVertex3f(0.1, 3, -2),
    glVertex3f(0.1, 3, -0.5),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-0.1, 0, 1.5),
    glVertex3f(-0.1, 0, -1.5),
    glVertex3f(-0.1, 3, -2),
    glVertex3f(-0.1, 3, -0.5),
    glEnd()
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex3f(-0.1, 0, 1.5),
    glVertex3f(-0.1, 3, -0.5),
    glVertex3f(0.1, 3, -0.5),
    glVertex3f(0.1, 0, 1.5),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-0.1, 3, -0.5),
    glVertex3f(0.1, 3, -0.5),
    glVertex3f(0.1, 3, -2),
    glVertex3f(-0.1, 3, -2),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-0.1, 0, -1.5),
    glVertex3f(-0.1, 3, -2),
    glVertex3f(0.1, 3, -2),
    glVertex3f(0.1, 0, -1.5),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-0.1, 0, 1.5),
    glVertex3f(0.1, 0, 1.5),
    glVertex3f(0.1, 0, -1.5),
    glVertex3f(-0.1, 0, -1.5),
    glEnd()
    glRotatef(-direcao, 0, 1, 0)
    glRotatef(10, 0, 0, 1)
    glTranslatef(-1.85, -1.25, 0)
    #asa traseira vertical direita
    glTranslatef(-1.85, 1.25, 0)
    glRotatef(10, 0, 0, 1)
    glRotatef(direcao, 0, 1, 0)
    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_POLYGON)
    glVertex3f(0.1, 0, 1.5),
    glVertex3f(0.1, 0, -1.5),
    glVertex3f(0.1, 3, -2),
    glVertex3f(0.1, 3, -0.5),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-0.1, 0, 1.5),
    glVertex3f(-0.1, 0, -1.5),
    glVertex3f(-0.1, 3, -2),
    glVertex3f(-0.1, 3, -0.5),
    glEnd()
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_POLYGON)
    glVertex3f(-0.1, 0, 1.5),
    glVertex3f(-0.1, 3, -0.5),
    glVertex3f(0.1, 3, -0.5),
    glVertex3f(0.1, 0, 1.5),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-0.1, 3, -0.5),
    glVertex3f(0.1, 3, -0.5),
    glVertex3f(0.1, 3, -2),
    glVertex3f(-0.1, 3, -2),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-0.1, 0, -1.5),
    glVertex3f(-0.1, 3, -2),
    glVertex3f(0.1, 3, -2),
    glVertex3f(0.1, 0, -1.5),
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-0.1, 0, 1.5),
    glVertex3f(0.1, 0, 1.5),
    glVertex3f(0.1, 0, -1.5),
    glVertex3f(-0.1, 0, -1.5),
    glEnd()
    glRotatef(-direcao, 0, 1, 0)
    glRotatef(-10, 0, 0, 1)
    glTranslatef(1.85, -1.25, 0)

    glTranslatef(0, 0, 7)

    glTranslatef(0, -subir, 0)
    

    
     #----------------------------------------------------------------------------------------------
    
    # Cenário > #pista
    glColor3f(0.13, 0.13, 0.14)
    glBegin(GL_POLYGON)
    glVertex3f(-20, -4.7, -130)
    glVertex3f(-20, -4.7, 100)
    glVertex3f(20, -4.7, 100)
    glVertex3f(20, -4.7, -130)
    glEnd()
    
    glColor3f(0.9, 0.9, 0.9)
    glBegin(GL_POLYGON)
    glVertex3f(20, -4.7, 100)
    glVertex3f(20, -4.2, 100)
    glVertex3f(20, -4.2, -130)
    glVertex3f(20, -4.7, -130)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(20, -4.2, 100)
    glVertex3f(22, -4.2, 100)
    glVertex3f(22, -4.2, -130)
    glVertex3f(20, -4.2, -130)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-20, -4.7, 100)
    glVertex3f(-20, -4.2, 100)
    glVertex3f(-20, -4.2, -130)
    glVertex3f(-20, -4.7, -130)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-20, -4.2, 100)
    glVertex3f(-22, -4.2, 100)
    glVertex3f(-22, -4.2, -130)
    glVertex3f(-20, -4.2, -130)
    glEnd()

    glColor3f(0.8, 0.8, 0.8)
    glBegin(GL_POLYGON)
    glVertex3f(-1, -4.699, (faixa1-24))
    glVertex3f(-1, -4.699, faixa1)
    glVertex3f(1, -4.699, faixa1)
    glVertex3f(1, -4.699, (faixa1-24))
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-1, -4.699, (faixa2-24))
    glVertex3f(-1, -4.699, faixa2)
    glVertex3f(1, -4.699, faixa2)
    glVertex3f(1, -4.699, (faixa2-24))
    glEnd()
    
    # < Cenário
    
    #----------------------------------------------------------------------------------------------
    glRotatef(-px, 1, 0, 0)
    glRotatef(-py, 0, 1, 0)
    glRotatef(-pz, 0, 0, 1)
    
    glFlush()

def buttons(key,x,y):
    global px, py, pz
    if key == GLUT_KEY_LEFT:
        py -= 3
        
    elif key == GLUT_KEY_RIGHT:
        py += 3
        
    elif key == GLUT_KEY_UP:
        px += 3
        
    elif key == GLUT_KEY_DOWN:
        px -= 3
    
    elif key == GLUT_KEY_PAGE_UP:
        pz -= 3
    
    elif key == GLUT_KEY_PAGE_DOWN:
        pz += 3
    
    elif key == GLUT_KEY_HOME: # # Voltar para a vista frental (tecla Home)
        px = 0
        py = 0
        pz = 0
        
    elif key == GLUT_KEY_END: # Vista em perspectiva (tecla End)
        px = 6
        py = -30
        pz = 0
        
    glutPostRedisplay()
    
def movimento(key,x,y):
    global direcao, faixa1, faixa2, rotacaoy, subir
    
    if (key == b'w') or (key == b'W'):
        faixa1 -= 1
        faixa2 -= 1
        
        if (rotacaoy > 1) and ( subir < 8):
            subir += rotacaoy *0.005

        if (rotacaoy < 1) and ( subir > 0):
            subir -= -rotacaoy *0.005

        if faixa1 < -80:
            faixa1 = 80

        if faixa2 < -80:
            faixa2 = 80
    
    elif (key == b'4'):
        if direcao < 15:
            direcao += 3
    
    elif (key == b'6'):
        if direcao > -15:
            direcao -= 3

    elif (key == b'5'):
        if rotacaoy < 20:
            rotacaoy +=2
    
    elif (key == b'8'):
        if rotacaoy > -20:
            rotacaoy -=2
    
    glutPostRedisplay()

def main():
    global distancia
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(2000,1300)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(name)
    glClearColor(0.42, 0.42, 1, 1) #backgroundcolor
    glShadeModel(GL_SMOOTH)
    glFrontFace(GL_CCW)
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutSpecialFunc(buttons)
    glutKeyboardFunc(movimento)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(50,(1000/650),1,200)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(8.25,-12.25,20,0,0,0,-0.07,1,0)
    glPushMatrix()
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(30,1,1,0)
    drawF35()
    glPopMatrix()
    glutSwapBuffers()
    return

if __name__ == '__main__': main()