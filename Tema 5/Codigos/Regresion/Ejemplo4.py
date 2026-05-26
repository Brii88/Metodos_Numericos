import math

exp = [1, 3, 5, 7, 10]
sueldo = [15, 22, 30, 35, 45]
n = len(exp)

sum_x, sum_y = sum(exp), sum(sueldo)
sum_x2 = sum(x**2 for x in exp)
sum_xy = sum(exp[i] * sueldo[i] for i in range(n))

a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a0 = (sum_y / n) - a1 * (sum_x / n)

syx = math.sqrt(sum((sueldo[i] - (a0 + a1 * exp[i]))**2 for i in range(n)) / (n - 2))

print(f"Modelo Predictivo Salarial: y = {a0:.3f} + {a1:.3f}x")
print(f"Cuota de Error (Syx): {syx:.3f} miles MXN")
