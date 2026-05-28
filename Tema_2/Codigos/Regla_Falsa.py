def regla_falsa(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        return "Intervalo inválido."

    for i in range(1, max_iter + 1):
        # Fórmula de la posición falsa
        xr = b - (f(b) * (a - b)) / (f(a) - f(b))
        fxr = f(xr)
        
        if abs(fxr) < tol:
            return xr
        
        if f(a) * fxr < 0:
            b = xr
        else:
            a = xr
    return xr

# Ejemplo: f(x) = x^2 - 2 en [0, 2]
f2 = lambda x: x**2 - 2
raiz = regla_falsa(f2, 0, 2)
print(f"Raíz aproximada (Regla Falsa): {raiz}")