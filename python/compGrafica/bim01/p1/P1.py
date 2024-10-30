import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import time

# Define as formas das peças do Tetris
FORMAS = [
    [(0, 0), (1, 0), (0, 1), (1, 1)],  # O (não rotaciona)
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # I
    [(0, 0), (0, 1), (0, 2), (1, 2)],  # L
    [(1, 0), (1, 1), (1, 2), (0, 2)],  # J
    [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z
    [(1, 0), (2, 0), (0, 1), (1, 1)],  # S
    [(0, 0), (1, 0), (2, 0), (1, 1)]   # T
]

# Cores das peças
CORES = [
    (1.0, 0.0, 0.0),  # Vermelho
    (0.0, 1.0, 0.0),  # Verde
    (0.0, 0.0, 1.0),  # Azul
    (1.0, 1.0, 0.0),  # Amarelo
    (1.0, 0.5, 0.0),  # Laranja
    (0.5, 0.0, 1.0),  # Roxo
    (0.0, 1.0, 1.0),  # Ciano
    (1.0, 0.0, 1.0),  # Magenta
    (0.5, 0.5, 0.5),  # Cinza
    (0.8, 0.4, 0.1),  # Marrom
    (1.0, 1.0, 1.0),  # Branco
    (0.7, 0.1, 0.3),  # Rosa
]

# Tamanho do grid
LARGURA_GRADE, ALTURA_GRADE = 10, 20
TAMANHO_CELULA = 30

# Inicializa o Pygame
pygame.init()
tela = pygame.display.set_mode((LARGURA_GRADE * TAMANHO_CELULA, ALTURA_GRADE * TAMANHO_CELULA), pygame.OPENGL | pygame.DOUBLEBUF)
pygame.display.set_caption("Tetris-OpenGL")

# OpenGL
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(-1, LARGURA_GRADE + 1, ALTURA_GRADE + 1, -1)  # Eixo Y
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Peças e posições
forma_atual = random.choice(FORMAS)
cor_atual = random.choice(CORES)
pos_atual = [LARGURA_GRADE // 2 - 1, 0]

# Grid do jogo
grade = [[None for _ in range(LARGURA_GRADE)] for _ in range(ALTURA_GRADE)]

# Estado do jogo
jogo_acabou = False

# Desenha um bloco
def desenhar_bloco(x, y, cor):
    glColor3f(*cor)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(x + 1, y)
    glVertex2f(x + 1, y + 1)
    glVertex2f(x, y + 1)
    glEnd()

# Desenha a peça atual
def desenhar_peca(forma, pos, cor):
    for bloco in forma:
        desenhar_bloco(pos[0] + bloco[0], pos[1] + bloco[1], cor)

# Desenha o grid
def desenhar_grade():
    glColor3f(0.5, 0.5, 0.5)
    for y in range(ALTURA_GRADE):
        for x in range(LARGURA_GRADE):
            if grade[y][x]:
                desenhar_bloco(x, y, grade[y][x])

# Desenha muros ao redor da tela
def desenhar_paredes_externas():
    cor_parede = (0.3, 0.3, 0.3)
    for y in range(ALTURA_GRADE):
        desenhar_bloco(-1, y, cor_parede)
        desenhar_bloco(LARGURA_GRADE, y, cor_parede)
    for x in range(LARGURA_GRADE):
        desenhar_bloco(x, -1, cor_parede)
        desenhar_bloco(x, ALTURA_GRADE, cor_parede)

# Rotaciona a peça
def rotacionar_forma(forma):
    return [(-bloco[1], bloco[0]) for bloco in forma]

# Mensagem GAME OVER
def mensagem_jogo_acabado():
    fonte = pygame.font.Font('freesansbold.ttf', 32)
    texto = fonte.render("GAME OVER", True, (255, 0, 255))
    return texto

# Move a peça para baixo e checa colisão
def mover_peca_baixo():
    global pos_atual, forma_atual, cor_atual, jogo_acabou
    pos_atual[1] += 1
    if verificar_colisao(forma_atual, pos_atual):
        pos_atual[1] -= 1
        prender_peca()
        forma_atual = random.choice(FORMAS)
        cor_atual = random.choice(CORES)
        pos_atual = [LARGURA_GRADE // 2 - 1, 0]
        if verificar_colisao(forma_atual, pos_atual):
            jogo_acabou = True

# Checa colisão
def verificar_colisao(forma, pos):
    for bloco in forma:
        x, y = bloco[0] + pos[0], bloco[1] + pos[1]
        if x < 0 or x >= LARGURA_GRADE or y >= ALTURA_GRADE:
            return True
        if y >= 0 and grade[y][x]:
            return True
    return False

# Prende a peça ao grid
def prender_peca():
    for bloco in forma_atual:
        x, y = bloco[0] + pos_atual[0], bloco[1] + pos_atual[1]
        grade[y][x] = cor_atual
    limpar_linhas()

# Limpa as linhas
def limpar_linhas():
    global grade
    nova_grade = [linha for linha in grade if any(celula is None for celula in linha)]
    linhas_limpa = ALTURA_GRADE - len(nova_grade)
    grade = [[None for _ in range(LARGURA_GRADE)] for _ in range(linhas_limpa)] + nova_grade

# Loop do jogo
executando = True
tempo_queda = time.time()  # Adiciona um tempo inicial
intervalo_queda = 0.5  # Intervalo de queda

while executando:
    # Lidar com eventos principais
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                executando = False
            if not jogo_acabou:  # Apenas mover a peça se o estado do jogo for verdadeiro
                if evento.key == pygame.K_LEFT:
                    pos_atual[0] -= 1
                    if verificar_colisao(forma_atual, pos_atual):
                        pos_atual[0] += 1
                if evento.key == pygame.K_RIGHT:
                    pos_atual[0] += 1
                    if verificar_colisao(forma_atual, pos_atual):
                        pos_atual[0] -= 1
                if evento.key == pygame.K_DOWN:
                    mover_peca_baixo()
                if evento.key == pygame.K_UP:  # Rotaciona a peça
                    forma_rotacionada = rotacionar_forma(forma_atual)
                    if not verificar_colisao(forma_rotacionada, pos_atual):
                        forma_atual = forma_rotacionada

    if not jogo_acabou:
        # Limpa a tela
        glClear(GL_COLOR_BUFFER_BIT)
        # Desenha o jogo
        desenhar_grade()
        desenhar_peca(forma_atual, pos_atual, cor_atual)
        desenhar_paredes_externas()

        # Atualiza a tela
        pygame.display.flip()

        # Verifica se é hora de mover a peça para baixo
        if time.time() - tempo_queda > intervalo_queda:
            mover_peca_baixo()
            tempo_queda = time.time()  # Atualiza o tempo da última queda

    else:
        # Desenhar mensagem GAME OVER
        texto = mensagem_jogo_acabado()
        tela.blit(texto, (LARGURA_GRADE * TAMANHO_CELULA / 2 - texto.get_width() / 2, ALTURA_GRADE * TAMANHO_CELULA / 2 - texto.get_height() / 2))
        pygame.display.flip()
        executando = False

pygame.quit()