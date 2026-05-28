def euler(f, x0, y0, h, pasos):
    print(f"{'Paso':<10}{'x':<10}{'y':<10}")
    x = x0
    y = y0
    for i in range(pasos + 1):
        print(f"{i:<10}{x:<10.2f}{y:<10.4f}")
        y = y + h * f(x, y)
        x = x + h

# Ejemplo 1: dy/dx = x + y | Condición inicial: (0, 1)
f1 = lambda x, y: x + y
print("Método de Euler:")
euler(f1, 0, 1, 0.1, 5)