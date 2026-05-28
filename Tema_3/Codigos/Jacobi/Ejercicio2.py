x, y, z = 0, 0, 0
for i in range(1, 6):
    nx = (12 - y - z) / 10
    ny = (12 - x - z) / 10
    nz = (12 - x - y) / 10
    x, y, z = nx, ny, nz
    print(f"Iter {i}: x={x:.4f}, y={y:.4f}, z={z:.4f}")