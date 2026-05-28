# Sistema: 2x - y + z = 2; x + 3y + 2z = 13; x - y + 2z = 3
# Matriz aumentada [A|B]
M = [
    [2.0, -1.0, 1.0, 2.0],
    [1.0, 3.0, 2.0, 13.0],
    [1.0, -1.0, 2.0, 3.0]
]

n = 3
# Proceso de Gauss-Jordan para convertir en Identidad
for i in range(n):
    # Hacer que el pivote sea 1
    pivote = M[i][i]
    for j in range(i, n + 1):
        M[i][j] /= pivote
    
    # Hacer ceros en las otras filas de la columna i
    for k in range(n):
        if k != i:
            factor = M[k][i]
            for j in range(i, n + 1):
                M[k][j] -= factor * M[i][j]

print(f"Soluciones: x={M[0][3]}, y={M[1][3]}, z={M[2][3]}")