# Sistema: x + y = 5; x - y = 1
M = [
    [1.0, 1.0, 5.0],
    [1.0, -1.0, 1.0]
]

# R2 = R2 - R1
for j in range(3):
    M[1][j] = M[1][j] - M[0][j]

# R2 = R2 / -2
for j in range(3):
    M[1][j] = M[1][j] / -2.0

# R1 = R1 - R2
for j in range(3):
    M[0][j] = M[0][j] - M[1][j]

print("Matriz escalonada reducida:")
for fila in M:
    print(fila)