# Ejemplo general de Euler
def f(t, y): 
    return 0.5 * y  # Cambia esta fórmula según el ejercicio

t, y, h = 0, 100, 0.1
pasos = 2

for _ in range(pasos):
    y = y + h * f(t, y)
    t = t + h
    print(f"En el tiempo {t:.2f}, el valor es: {y:.4f}")