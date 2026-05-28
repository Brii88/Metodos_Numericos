# 5x + 2y = 7; x + 4y = 5
x, y = 0, 0
for i in range(1, 6):
    x = (7 - 2*y) / 5
    y = (5 - x) / 4
    print(f"Paso {i}: x={x:.4f}, y={y:.4f}")