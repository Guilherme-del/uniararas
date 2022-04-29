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
(B) Faça um algoritmo em Python que dada a matriz de coeficientes A e o vetor constante b,
imprima o sistema equivalente triangular superior.
'''
import numpy as np

A = np.array([[2.0, 1.0, -3.0], [-1.0, 3.0, 2.0], [3.0, 1.0, -3.0]])
B = np.array([[-1.0], [12.0], [0.0]])
C = 0
M = A[1, C]/A[C, C]
print('\t', 'multiPlicador:', M,
      '---[linha,coluna]:', A[1, C], '----PIVO:', A[C, C])

A[1, :] = A[1, :]-M*A[0, :]
B[1, 0] = B[1, 0]-M*B[0, 0]
print('\n', A)
print('\n', B)
print('*'*50)

M = A[2, C]/A[C, C]
print('\t', 'multiPlicador:', M,
      '---[linha,coluna]:', A[2, C], '----PIVO:', A[C, C])

A[2, :] = A[2, :]-M*A[0, :]
B[2, 0] = B[2, 0]-M*B[0, 0]
print('\n', A)
print('\n', B)
print('*'*50)
c2 = 1

M = A[2, c2]/A[c2, c2]
print('\t', 'multiPlicador:', M,
      '---[linha,coluna]:', A[2, c2], '----PIVO:', A[c2, c2])
A[2, :] = A[2, :]-M*A[1, :]
B[2, 0] = B[2, 0]-M*B[1, 0]
print('\n', A)
print('\n', B)
print('*'*50)
