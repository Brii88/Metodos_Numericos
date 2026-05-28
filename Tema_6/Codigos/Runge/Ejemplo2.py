x, y, h = 0, 1, 0.1
f = x + y
df = 1 + x + y # Segunda derivada
y = y + h * f + (h**2 / 2) * df
print(f"Resultado Taylor: {y}")