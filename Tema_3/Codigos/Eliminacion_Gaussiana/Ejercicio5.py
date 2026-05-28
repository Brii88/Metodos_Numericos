# Matriz con un cero en la diagonal principal M[0][0]
M = [
    [0.0, 2.0, 4.0],
    [1.0, 1.0, 3.0]
]

print("Matriz original:")
for fila in M: print(fila)

# Lógica de Pivoteo
i = 0  # Columna que queremos evaluar
# Buscamos el renglón con el valor más grande en la columna i
max_row = i
for k in range(i + 1, len(M)):
    if abs(M[k][i]) > abs(M[max_row][i]):
        max_row = k

# Intercambio manual de listas (renglones)
M[i], M[max_row] = M[max_row], M[i]

print("\nMatriz después de pivoteo:")
for fila in M: print(fila)