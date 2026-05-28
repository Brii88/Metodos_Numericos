# 6x + y = 7; x + 4y = 5
x, y = 0, 0
for i in range(1, 6):
    nx = (7 - y) / 6
    ny = (5 - x) / 4
    x, y = nx, ny
    print(f"Iteración {i}: x={x:.4f}, y={y:.4f}")