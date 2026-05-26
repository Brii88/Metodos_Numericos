import numpy as np
def f(x):
    return np.exp(x)
a, b = 0, 2
I = (b - a)/2 * (f(a) + f(b))
print("Resultado:", I)