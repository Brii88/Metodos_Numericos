import math
x, y, h = 0, 4, 0.2
f = -math.sqrt(y)
df = 0.5 # Derivada calculada analíticamente
y = y + h * f + (h**2 / 2) * df
print(f"Nivel del tanque: {y}")