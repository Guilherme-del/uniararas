import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define o caminho da imagem
imagem = './img/texture2.jpg'

# Define os vértices do cubo
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

# Define as faces do cubo
surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

# Coordenadas da textura
texture_coords = (
    (0, 0),
    (1, 0),
    (1, 1),
    (0, 1)
)

# Carrega a textura
def load_texture():
    superficieTextura = pygame.image.load(imagem)
    infoTextura = pygame.image.tostring(superficieTextura, 'RGB', 1)
    largura = superficieTextura.get_width()
    altura = superficieTextura.get_height()
    
    # Cria a textura
    glEnable(GL_TEXTURE_2D)
    idTextura = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, idTextura)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, largura, altura, 0, GL_RGB, GL_UNSIGNED_BYTE, infoTextura)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    return idTextura

# Desenha o cubo com a textura
def Cube(idTextura):
    glBindTexture(GL_TEXTURE_2D, idTextura)
    glBegin(GL_QUADS)
    for surface in surfaces:
        for i, vertex in enumerate(surface):
            glTexCoord2fv(texture_coords[i])
            glVertex3fv(vertices[vertex])
    glEnd()

# Função principal
if __name__ == '__main__':
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    fatorEscala = [1.0, 1.0, 1.0]
    idTextura = load_texture()

    # Variáveis para física
    posX = 0.0  # Início na horizontal
    posY = 2.0  # Início na borda superior
    posZ = 0.0
    posYMax = -1.0  # Posição do "chão"
    parede_direita = 2.0  # Posição da parede à direita
    altura_maxima = 0.5  # Altura máxima do pingo
    batendo = False
    pingo_contador = 0  # Contador de pingos
    caindo = False  # Indica se o cubo está caindo

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        # Atualiza a física
        if pingo_contador < 3:
            posY -= 0.05  # Mover para baixo

            if posY <= 1.5:  # Quando atinge a borda direita
                posX += 0.05  # Mover para a direita

                if posX >= parede_direita:
                    posX = parede_direita
                    batendo = True  # Começa a pingar

                if batendo:
                    # Pingar para cima
                    posY += altura_maxima * 0.1  
                    if posY >= posYMax + altura_maxima:
                        posY = posYMax + altura_maxima
                    
                    # Simular a queda
                    if posY >= posYMax + altura_maxima: 
                        posY -= 0.01  # Leve movimento para baixo
                    else:
                        batendo = False  # Para de pingar
                        pingo_contador += 1  # Incrementa o contador
                        # Agora o cubo vai voltar um pouco para a esquerda
                        posX -= 0.02  # Movimento menor para a esquerda
                        caindo = True  # Começa a cair

        # Se o cubo estiver caindo
        if caindo:
            posY -= 0.02  # Movimento para baixo
            if posY <= posYMax:  # Quando atinge o chão
                posY = posYMax
                caindo = False  # Para de cair

        # Limpa o buffer de cor e o buffer de profundidade
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        # Desenha o cubo na tela
        glPushMatrix()  # Salva a matriz atual
        glTranslatef(posX, posY, posZ)  # Atualiza a posição do cubo
        glScalef(fatorEscala[0], fatorEscala[1], fatorEscala[2])
        
        Cube(idTextura)
        
        glPopMatrix()  # Restaura a matriz salva
        
        pygame.display.flip()
        pygame.time.wait(10)
