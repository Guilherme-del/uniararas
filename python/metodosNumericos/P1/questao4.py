#########################################################################
#######           METODOS NUMERICOS PARA ENGENHARIA              ########
##################### SEMESTRE 1 - ANO 2022 #############################
######################### AVALIACAO P1 ##################################
#########################   QUESTAO 4  #################################
# NOME: Guilherme Cavenaghi
## RA: 109317
# CURSO: Eng. da Computação
#########################################################################

from math import *
import numpy as np
import sympy as sp

def newton(f, df, x0, eps, itmax):
    L = range(1, itmax+1)
    iteracao = 0
    a = x0
    for i in L:
        raiz = a
        if df(raiz) != 0:  # se a derivada for ele finaliza
            raiz = raiz-f(raiz)/df(raiz)
            erro = raiz-a
            a = raiz
            iteracao = i
        else:
            iteracao = itmax+1
            break
        if abs(erro) <= eps:
            break
    if iteracao > itmax:
        iteracao = 0.25
    elif iteracao == itmax:
        iteracao = 0.75
    return [raiz, erro, iteracao]

# teste :
x = sp.symbols('x')
e = lambda x: np.exp(x) 
log = lambda x:  log(x)

f= e - log - 2
df = e - log

L = newton(f, df, 1.0, 0.0000001, 10000)
print(L)
