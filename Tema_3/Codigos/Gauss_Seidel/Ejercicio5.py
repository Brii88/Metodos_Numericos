# 3x + y = 5; x + 2y = 4
x, y = 0, 0
for i in range(1, 6):
    x = (5 - y) / 3
    y = (4 - x) / 2
    print(f"Iter {i}: [x y] = [{x:.4f} {y:.4f}]")