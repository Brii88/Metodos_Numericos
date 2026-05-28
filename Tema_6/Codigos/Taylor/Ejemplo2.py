f = lambda x, y: (10 - 2 * y) / 0.5
x, y, h = 0, 0, 0.1

k1 = h * f(x, y)
k2 = h * f(x + h / 2, y + k1 / 2)
k3 = h * f(x + h / 2, y + k2 / 2)
k4 = h * f(x + h, y + k3)

y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
print(f"Carga RK4: {y}")