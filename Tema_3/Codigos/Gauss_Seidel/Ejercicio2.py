# Sistema: 10x + y + z = 12; x + 10y + z = 12; x + y + 10z = 12
x, y, z = 0, 0, 0  # Inicialización
for i in range(1, 6):
    x = (12 - y - z) / 10
    y = (12 - x - z) / 10
    z = (12 - x - y) / 10
    print(f"Iteración {i}: x={x:.4f}, y={y:.4f}, z={z:.4f}")