f = lambda x: x**2 + 4
a, b = -2, 2
for i in range(1, 6):
    xr = (a + b) / 2
    print(f"Iteración {i}: xr = {xr}, f(xr) = {f(xr)}")
    if f(a) * f(xr) < 0:
        b = xr
    else:
        a = xr