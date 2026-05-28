def taylor_2do_orden(f, df, x0, y0, h, pasos):
    print(f"{'Paso':<10}{'x':<10}{'y':<10}")
    x, y = x0, y0
    for i in range(pasos + 1):
        print(f"{i:<10}{x:<10.2f}{y:<10.4f}")
        # f es la primera derivada, df es la segunda derivada total
        y = y + h * f(x, y) + (h**2 / 2) * df(x, y)
        x = x + h

# Ejemplo 2: dy/dx = y - x^2 + 1
# La derivada total f'(x,y) sería: y' - 2x = (y - x^2 + 1) - 2x
f2 = lambda x, y: y - x**2 + 1
df2 = lambda x, y: (y - x**2 + 1) - 2*x

print("\nMétodo de Taylor (2do Orden):")
taylor_2do_orden(f2, df2, 0, 0.5, 0.2, 5)