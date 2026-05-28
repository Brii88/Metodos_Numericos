# 2x + 3y = 8; 4x + y = 6
# R2 = R2 - 2*R1
a = [[2, 3, 8], [4, 1, 6]]
factor = a[1][0] / a[0][0]
a[1] = [a[1][j] - factor * a[0][j] for j in range(3)]
y = a[1][2] / a[1][1]
x = (a[0][2] - a[0][1]*y) / a[0][0]
print(f"Solución: x={x}, y={y}")