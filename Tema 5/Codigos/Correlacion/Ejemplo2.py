import math

edad = [1, 3, 5, 7, 9]
costo = [1.5, 2.0, 3.5, 4.0, 5.5]
n = len(edad)

# Funciones map/lambda para sumatorias rápidas
sum_x, sum_y = sum(edad), sum(costo)
sum_x2 = sum(map(lambda x: x**2, edad))
sum_y2 = sum(map(lambda x: x**2, costo))
sum_xy = sum(x*y for x, y in zip(edad, costo))

r = (n * sum_xy - sum_x * sum_y) / math.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))

print(f"Correlación edad-costo (r): {r:.4f}")
print(f"Cuota de error del modelo: {(1 - r**2)*100:.1f}%")

