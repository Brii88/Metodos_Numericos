f = lambda x: x**3 - 2*x + 2
a, b = -3, -1
for i in range(1, 6):
    xr = b - (f(b) * (a - b)) / (f(a) - f(b))
    if f(a) * f(xr) < 0:
        b = xr
    else:
        a = xr
    print(f"Paso {i}: xr = {xr:.4f}")