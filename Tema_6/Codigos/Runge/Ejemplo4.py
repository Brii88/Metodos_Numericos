y, h = 0, 0.1
f = 1 - y
df = y - 1
y = y + h * f + (h**2 / 2) * df
print(f"Carga: {y}")