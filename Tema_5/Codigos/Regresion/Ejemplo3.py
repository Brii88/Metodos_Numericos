import math

nodos = [2, 4, 6, 8, 10]
tiempo = [50, 35, 25, 15, 10]
n = len(nodos)

sum_x, sum_y = sum(nodos), sum(tiempo)
sum_x2 = sum(x**2 for x in nodos)
sum_xy = sum(nodos[i] * tiempo[i] for i in range(n))

a1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
a0 = (sum_y / n) - a1 * (sum_x / n)

syx = math.sqrt(sum((tiempo[i] - (a0 + a1 * nodos[i]))**2 for i in range(n)) / (n - 2))

print(f"Ecuación: y = {a0:.1f} - {abs(a1):.1f}x")
print(f"Cuota de Error (Syx): {syx:.2f} min")
