def runge_kutta_4(f, x0, y0, h, pasos):
    print(f"{'Paso':<10}{'x':<10}{'y':<10}")
    x, y = x0, y0
    for i in range(pasos + 1):
        print(f"{i:<10}{x:<10.2f}{y:<10.6f}")
        
        k1 = h * f(x, y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
        x = x + h

# Ejemplo 3: dy/dx = x * sqrt(y) | Condición inicial: (1, 4)
import math
f3 = lambda x, y: x * math.sqrt(y)

print("\nMétodo de Runge-Kutta (RK4):")
runge_kutta_4(f3, 1, 4, 0.1, 5)