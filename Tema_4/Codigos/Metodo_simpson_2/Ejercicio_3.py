def f(x):
    return 1/(x - 1.5)
a, b = 0, 3
h = (b - a) / 3
x0 = a
x1 = a + h
x2 = a + 2*h
x3 = b
I = (3*h/8) * (f(x0) + 3*f(x1) + 3*f(x2) + f(x3))
print("Resultado:", I) # puede fallar o dar infinito