import math

vel = [10, 20, 30, 50, 100]
ping = [120, 90, 75, 60, 45]
n = len(vel)

sum_x, sum_y = sum(vel), sum(ping)
sum_x2 = sum(x**2 for x in vel)
sum_y2 = sum(y**2 for y in ping)
sum_xy = sum(vel[i] * ping[i] for i in range(n))

numerador = (n * sum_xy) - (sum_x * sum_y)
denominador = math.sqrt((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2))
r = numerador / denominador

print(f"Coeficiente de correlación (r): {r:.4f}")
print(f"Cuota de error del modelo (%): {(1 - r**2)*100:.2f}%")
