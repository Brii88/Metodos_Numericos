# Sistema: 3x + 2y = 12; 2x + 3y = 13
M = [
    [3.0, 2.0, 12.0],
    [2.0, 3.0, 13.0]
]

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

print(f"x = {M[0][2]}, y = {M[1][2]}")