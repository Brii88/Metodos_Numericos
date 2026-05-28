x, y = 0, 0
for i in range(1, 6):
    nx = (7 - 2*y) / 5
    ny = (5 - x) / 4
    x, y = nx, ny
    print(f"Paso {i}: x={x:.4f}, y={y:.4f}")