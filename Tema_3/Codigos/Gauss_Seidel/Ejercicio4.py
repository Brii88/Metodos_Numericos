# 4x - y = 3; x + 3y = 5
x, y = 0, 0
for i in range(1, 6):
    x_ant = x
    x = (3 + y) / 4
    y = (5 - x) / 3
    error = abs((x - x_ant) / x) * 100 if x != 0 else 0
    print(f"Iter {i}: x={x:.4f}, Error={error:.2f}%")