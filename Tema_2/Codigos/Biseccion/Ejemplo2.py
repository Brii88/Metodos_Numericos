# Ejemplo: f(x) = x^2 - 3 en el intervalo [1, 2]
import math

f = lambda x: x**2 - 3
a = 1.0
b = 2.0
tol = 0.01  # Tolerancia
iteraciones = 5

print(f"{'Iter':<5} {'a':<10} {'b':<10} {'Xr':<10} {'f(Xr)':<10}")

for i in range(1, iteraciones + 1):
    xr = (a + b) / 2
    fxr = f(xr)
    
    print(f"{i:<5} {a:<10.4f} {b:<10.4f} {xr:<10.4f} {fxr:<10.4f}")
    
    if f(a) * fxr < 0:
        b = xr
    else:
        a = xr

print(f"\nRaíz aproximada por Bisección: {xr:.4f}")