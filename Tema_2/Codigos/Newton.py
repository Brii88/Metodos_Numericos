def newton_raphson(f, df, x0, tol=1e-5, max_iter=100):
    xn = x0
    for i in range(1, max_iter + 1):
        fxn = f(xn)
        dfxn = df(xn)
        
        if dfxn == 0:
            return "La derivada es cero, el método no puede continuar."
        
        x_next = xn - fxn / dfxn
        
        if abs(x_next - xn) < tol:
            return x_next
        
        xn = x_next
    return xn

# Ejemplo: f(x) = x^2 - 5, f'(x) = 2x, valor inicial x0 = 2
f3 = lambda x: x**2 - 5
df3 = lambda x: 2*x
raiz = newton_raphson(f3, df3, 2)
print(f"Raíz aproximada (Newton-Raphson): {raiz}")