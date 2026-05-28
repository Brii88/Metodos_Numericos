v, h = 5, 0.1
for _ in range(2):
    v = v + h * (-v / 2)
print(f"Voltaje: {v} V")