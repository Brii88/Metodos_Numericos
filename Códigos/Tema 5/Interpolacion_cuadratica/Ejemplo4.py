# Datos
x0, y0 = 0, 1
x1, y1 = 1, 3
x2, y2 = 2, 2


# Valor a interpolar
x = 1.5


# Polinomios de Lagrange
L0 = ((x - x1)*(x - x2))/((x0 - x1)*(x0 - x2))


L1 = ((x - x0)*(x - x2))/((x1 - x0)*(x1 - x2))


L2 = ((x - x0)*(x - x1))/((x2 - x0)*(x2 - x1))


# Interpolación
y = y0*L0 + y1*L1 + y2*L2


# Resultado
print("Resultado:", y)
