# Sistema: x + 2y = 5; 3x + 4y = 11
A = [[1.0, 2.0], [3.0, 4.0]]
B = [5.0, 11.0]

# Unimos A y B en una matriz aumentada
M = [A[0] + [B[0]], A[1] + [B[1]]]

n = 2
for i in range(n):
    pivote = M[i][i]
    for j in range(n + 1):
        M[i][j] /= pivote
    for k in range(n):
        if k != i:
            factor = M[k][i]
            for j in range(n + 1):
                M[k][j] -= factor * M[i][j]

res = [M[0][2], M[1][2]]
print(f"Resultado optimizado: {res}")