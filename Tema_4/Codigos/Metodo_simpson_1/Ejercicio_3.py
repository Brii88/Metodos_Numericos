import numpy as np
def f(x):
    return np.tan(x)
a, b = 0, 2
m = (a + b)/2
I = (b - a)/6 * (f(a) + 4*f(m) + f(b))
print("Resultado:", I)