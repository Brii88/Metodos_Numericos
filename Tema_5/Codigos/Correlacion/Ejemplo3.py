import math

temp = [5, 10, 15, 20, 25]
ventas = [80, 65, 40, 25, 10]
n = len(temp)

sum_x, sum_y = sum(temp), sum(ventas)
sum_x2 = sum(t**2 for t in temp)
sum_y2 = sum(v**2 for v in ventas)
sum_xy = sum(temp[i] * ventas[i] for i in range(n))

r = (n * sum_xy - sum_x * sum_y) / math.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))

print(f"Coeficiente de correlación (r): {r:.4f} (Negativa)")
print(f"Cuota de error (varianza inexplicada): {(1 - r**2)*100:.2f}%")
