t_temp, h = 80, 0.2
for _ in range(2):
    t_temp = t_temp + h * (-0.1 * (t_temp - 20))
print(f"Temperatura: {t_temp} °C")