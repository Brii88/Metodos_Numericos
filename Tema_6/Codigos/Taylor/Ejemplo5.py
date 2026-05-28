f = lambda x, y: y * (1 - y)
x, y, h = 0, 0.5, 0.1

k1 = h * f(x, y)
k2 = h * f(x + h / 2, y + k1 / 2)
k3 = h * f(x + h / 2, y + k2 / 2)
k4 = h * f(x + h, y + k3)

y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
print(f"Población RK4: {y}")