import numpy as np

def f(x):
    return x**2 + 1  

a, b = 0, 4
h = (b - a) / 4

x1 = a + h
x2 = a + 2*h
x3 = a + 3*h

I = (3*h/2) * (f(x1) + f(x2) + f(x3))
print("Resultado:", I)