x, y, z = 0, 0, 0
for i in range(1, 6):
    nx = (5 - y) / 4
    ny = (6 - x - z) / 3
    nz = (4 - y) / 4
    x, y, z = nx, ny, nz
    print(f"Iter {i}: x={x:.4f}, y={y:.4f}, z={z:.4f}")