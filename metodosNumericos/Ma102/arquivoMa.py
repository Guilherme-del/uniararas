'''
Guilherme Cavenaghi
RA: 109317
Luis Rodrigo da Silva 
RA: 109506
José Jorge Falasco Junior
RA: 108907
João Pedro Ramos Silva  
RA: 110748
Patrick Lucas Ferreira 
RA: 110714
------------------------------------------------
EXERCÍCIO 1 Dada a função

f(x) = x^3−x−4

faça um algoritmo em Python que calcule e imprima a sua solução utilizando o método de Newton-
Raphson.
'''

from math import *

def newton(f,df,x0,eps,itmax):
    L=range(1,itmax+1)
    iteracao=0
    a=x0
    for i in L:
        raiz=a
        if df(raiz) != 0: # se a derivada for zero sai    
            raiz=raiz-f(raiz)/df(raiz)
            erro=raiz-a
            a=raiz
            iteracao=i
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
f= lambda x: x**3 - x - 4
df= lambda x: 3*x**2 - 1

L=newton(f,df,1.5,0.0001,10000)
print(L)

