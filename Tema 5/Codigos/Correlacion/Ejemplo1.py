import math

horas = [2, 4, 6, 8, 10]
calif = [50, 70, 85, 90, 95]
n = len(horas)

sum_x = sum(horas)
sum_y = sum(calif)
sum_x2 = sum(x**2 for x in horas)
sum_y2 = sum(y**2 for y in calif)
sum_xy = sum(horas[i] * calif[i] for i in range(n))

numerador = (n * sum_xy) - (sum_x * sum_y)
denominador = math.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))
r = numerador / denominador

print(f"Coeficiente de correlación (r): {r:.4f}")
print(f"Cuota de error no explicada: {(1 - r**2)*100:.2f}%")
