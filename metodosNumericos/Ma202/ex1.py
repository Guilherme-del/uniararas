import numpy as np
import matplotlib.pylab as plt
import scipy.sparse as sps

def sistemaTrid(h):
  n = int(1/h)
  A = np.zeros((n-1,n-1))
  b = np.zeros((n-1))

  for i in range(0,n-1):
    for j in range(0,n-1):
      if (i == j): # di = (h^2 - 2)
        A[i,j] = (h**2 - 2)
      if ((j-1) == i): # ci = (1+h)  
        A[i,j] = (1 + h)
      if ((i-1) == j): # ai = (1-h)
        A[i,j] = (1 - h)

    b[i] = (i+1)*(h**3)
    if (i == (n-2)):
      b[i] = b[i] + (h+1)
             
  return A, b

h = 0.05
A,b = sistemaTrid(h)
print("A = ",A)
print("b = ",b)
M = sps.csr_matrix(A)
plt.spy(M)
plt.show()
y = np.linalg.solve(A,b)
print("y = ",y)