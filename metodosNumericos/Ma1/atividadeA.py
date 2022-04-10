'''
A)
Dada a matriz de coeficientes A e o vetor constante b, resolva o sistema com o comando
interno Python definido por
'''
import numpy as np

a = np.array([[2.0, 1, -3], [-1.0, 3, 2], [3.0, 1, -3]])
b = np.array([[-1.0],[12],[0]])

result = np.linalg.solve(a,b)

print(result)




