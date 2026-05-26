import math

x = [2, 3, 5, 6, 8]
y = [20, 25, 34, 38, 50]
n = len(x)

sum_x, sum_y = sum(x), sum(y)
sum_x2 = sum(i**2 for i in x)
sum_xy = sum(x[i] * y[i] for i in range(n))

a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a0 = (sum_y / n) - a1 * (sum_x / n)

st_error_sum = sum((y[i] - (a0 + a1 * x[i]))**2 for i in range(n))
syx = math.sqrt(st_error_sum / (n - 2))

print(f"Modelo de Regresión: y = {a0:.3f} + {a1:.3f}x")
print(f"Cuota de Error (Syx): {syx:.3f}")

