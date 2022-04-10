"""
Exercício 6: Crie um código em que dado um valor x não negativo, ele imprime na tela se este valor é par ou ímpar. 
"""

x = float(input('Digite um número para saber se é par ou impar:'))
resto = x % 2

if resto == 0:
    print('Número é par')
else:
    print('Número é impar')
