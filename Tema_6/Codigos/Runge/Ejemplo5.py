y, h = 1, 0.1
f = -0.5 * y**2
df = 0.5 * y**3
y = y + h * f + (h**2 / 2) * df
print(f"Velocidad: {y}")