'''
Roberto Antunes de Souza Junior 
RA: 102489
Guilherme Cavenaghi
RA: 109317
João Pedro Ramos silva
RA : 110748
Luis Rodrigo da Silva 
RA: 109506
------------------------------------------------
C)
Faça um algoritmo em Python que pegue o sistema triangular superior, resolva e imprima a
solução.
'''
print('\t \t SOLUCAO')
X3 = (3.14285714 / 1.57142857)
print('\n \t \t x3=', X3)

X2 = (11.5 - 0.5*X3) / 3.5
print('\t \t x2 =', X2)

X1 = ((3*X3)-X2-1) / 2
print('\t \t x1 = ', X1)


solution1 = (2*X1) + (1*X2) - (3*X3)
print('\n \t 2*1 + 1*3 - 3*2 =', solution1)

solution2 = (3.5*X2) + (0.5*X3)
print('\t 3.5*3 + 0.5*2 =', solution2)

solution3 = (1.57142857*X3)
print('\t 1,57142857*2 =', solution3)
