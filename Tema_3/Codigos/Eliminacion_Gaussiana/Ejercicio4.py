# Sistema: 
# 3.0x - 0.1y - 0.2z = 7.85
# 0.1x + 7.0y - 0.3z = -19.3
# 0.3x - 0.2y + 10.0z = 71.4

# Matriz aumentada [A|B]
M = [
    [3.0, -0.1, -0.2, 7.85],
    [0.1, 7.0, -0.3, -19.3],
    [0.3, -0.2, 10.0, 71.4]
]

n = len(M)

# Fase de Eliminación (Hacia adelante)
for i in range(n):
    for j in range(i + 1, n):
        factor = M[j][i] / M[i][i]
        for k in range(i, n + 1):
            M[j][k] = M[j][k] - factor * M[i][k]

# Fase de Sustitución (Hacia atrás)
x = [0] * n
for i in range(n - 1, -1, -1):
    suma = sum(M[i][j] * x[j] for j in range(i + 1, n))
    x[i] = (M[i][n] - suma) / M[i][i]

print(f"Solución: x={x[0]:.2f}, y={x[1]:.2f}, z={x[2]:.2f}")