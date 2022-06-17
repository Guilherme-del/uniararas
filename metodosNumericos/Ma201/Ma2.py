# -*- coding: utf-8 -*-
"""
Luis Rodrigo da Silva - 109506
Rafael Mendonça de Godoy - 110453
Mateus hypolito Silva - 109459
Guilherme Cavenaghi - 109317
João Pedro Ramos Silva - 110748

"""

import numpy as np
import matplotlib.pyplot as plt

n = 4
x = np.array([1.15, 2.0, 3.045, 4.0])
y = ([4.01, 8.11, 10.2111, 12.0541])

xQuad = np.square((x))
xQuadSoma = sum(xQuad)
xSoma = sum(x)
xy = x*y
xySoma = sum(xy)
ySoma = sum(y)

c = ([[xQuadSoma, xSoma],[xSoma , n]])
d = ([[xySoma],[ySoma]])

z = np.linalg.solve(c,d)
a = z[0][0]
b = z[1][0]

def f (x):
    return a*x+b

plt.title("Gráfico de f(x) = a*x+b = ")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

dom = np.linspace(0, 5)
img = f(dom)
plt.plot(dom ,img)

plt.title("Gráfico de disperção")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

plt.scatter(x,y,color = 'red')