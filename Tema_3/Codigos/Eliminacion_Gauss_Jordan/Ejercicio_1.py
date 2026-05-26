def gauss_jordan(A):
    n = len(A)

    for i in range(n):
        # PIVOTEO
        if A[i][i] == 0:
            for k in range(i+1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]
                    break

        pivote = A[i][i]

        # NORMALIZACIÓN
        for j in range(n+1):
            A[i][j] = A[i][j] / pivote

        # ELIMINACIÓN
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n+1):
                    A[k][j] = A[k][j] - factor * A[i][j]

    return A


# MATRIZ AUMENTADA 2x2
# Ejemplo:
# x + 2y = 5
# 3x + 4y = 11

A = [
    [1, 2, 5],
    [3, 4, 11]
]

resultado = gauss_jordan(A)

print("Matriz reducida:")
for fila in resultado:
    print(fila)

print("\nSolución del sistema:")
variables = ["x", "y"]

for i in range(len(resultado)):
    print(variables[i], "=", resultado[i][-1])