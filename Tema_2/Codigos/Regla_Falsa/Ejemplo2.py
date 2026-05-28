f = lambda x: x**3 - x - 1
a, b = 1, 2
for i in range(1, 6):
    xr = b - (f(b) * (a - b)) / (f(a) - f(b))
    print(f"Iter {i}: xr = {xr:.4f}, f(xr) = {f(xr):.4f}")
    if f(a) * f(xr) < 0:
        b = xr
    else:
        a = xr