import math

lineas = [1, 2, 4, 6, 8]
bugs = [2, 4, 7, 11, 14]
n = len(lineas)

sum_x, sum_y = sum(lineas), sum(bugs)
sum_x2 = sum(x**2 for x in lineas)
sum_xy = sum(lineas[i] * bugs[i] for i in range(n))

a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a0 = (sum_y / n) - a1 * (sum_x / n)

syx = math.sqrt(sum((bugs[i] - (a0 + a1 * lineas[i]))**2 for i in range(n)) / (n - 2))

print(f"Predicción de Bugs: y = {a0:.3f} + {a1:.3f}x")
print(f"Error Estándar (Syx): {syx:.3f} bugs")
