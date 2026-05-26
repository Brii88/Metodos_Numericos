def main():
    n = int(input("Ingrese el tamaño del sistema (n): "))

    # Leer matriz aumentada [A|b]
    print(f"Ingrese la matriz aumentada ({n} x {n + 1}):")
    matrix = []

    for i in range(n):
        values = input(f"Fila {i + 1}: ").split()

        if len(values) != n + 1:
            print(f"Error: Cada fila debe tener exactamente {n + 1} elementos.")
            return

        row = [float(v) for v in values]
        matrix.append(row)

    # Eliminación hacia adelante con pivoteo parcial
    for i in range(n):
        # Buscar fila pivote
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k

        # Intercambiar filas
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Verificar si la matriz es singular
        if abs(matrix[i][i]) < 1e-10:
            print("Error: La matriz es singular o casi singular.")
            return

        # Eliminación
        for k in range(i + 1, n):
            factor = matrix[k][i] / matrix[i][i]
            for j in range(i, n + 1):
                matrix[k][j] -= factor * matrix[i][j]

    # Sustitución hacia atrás
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n]
        for j in range(i + 1, n):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]

    # Mostrar solución
    print("\nSolución:")
    for i in range(n):
        print(f"x{i + 1} = {x[i]:.6f}")

if __name__ == "__main__":
    main()