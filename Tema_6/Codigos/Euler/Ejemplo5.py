v, h = 0, 0.1
for _ in range(2):
    v = v + h * (9.8 - 0.2 * v)
print(f"Velocidad: {v} m/s")