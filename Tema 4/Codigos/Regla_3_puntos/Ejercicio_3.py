import numpy as np

def f(x):
    if x == 2:
        return float('inf')  # o float('nan')
    return 1/(x-2)

a, b = 0, 4
h = (b - a) / 4

x1 = a + h
x2 = a + 2*h
x3 = a + 3*h

print(f"x1={x1}, x2={x2}, x3={x3}")  # para ver los puntos

I = (3*h/2) * (f(x1) + f(x2) + f(x3))
print("Resultado:", I)