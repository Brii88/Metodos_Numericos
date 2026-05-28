def secante(f, x0, x1, tol=1e-5, max_iter=100):
    for i in range(1, max_iter + 1):
        fx0 = f(x0)
        fx1 = f(x1)
        
        if fx1 - fx0 == 0:
            return "División por cero."
        
        # Fórmula de la secante
        x_next = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        
        if abs(x_next - x1) < tol:
            return x_next
        
        x0, x1 = x1, x_next
    return x1

# Ejemplo: f(x) = cos(x) - x entre [0, 1]
import math
f4 = lambda x: math.cos(x) - x
raiz = secante(f4, 0, 1)
print(f"Raíz aproximada (Secante): {raiz}")