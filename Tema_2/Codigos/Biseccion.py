def biseccion(f, a, b, tol=1e-5, max_iter=100):
    if f(a) * f(b) >= 0:
        return "El intervalo no es válido (no hay cambio de signo)."
    
    print(f"{'Iter':<10}{'a':<10}{'b':<10}{'xr':<10}{'f(xr)':<10}")
    for i in range(1, max_iter + 1):
        xr = (a + b) / 2
        fxr = f(xr)
        print(f"{i:<10}{a:<10.4f}{b:<10.4f}{xr:<10.4f}{fxr:<10.4f}")
        
        if abs(fxr) < tol:
            return xr
        
        if f(a) * fxr < 0:
            b = xr
        else:
            a = xr
    return xr

# Ejemplo: f(x) = x^3 - x - 1 en [1, 2]
f1 = lambda x: x**3 - x - 1
raiz = biseccion(f1, 1, 2)
print(f"\nRaíz aproximada: {raiz}")