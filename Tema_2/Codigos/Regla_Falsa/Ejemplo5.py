import math
f = lambda x: math.log(x) + x
a, b = 0.5, 1.0
for i in range(1, 6):
    xr = b - (f(b) * (a - b)) / (f(a) - f(b))
    if f(a) * f(xr) < 0:
        b = xr
    else:
        a = xr
    print(f"Iter {i}: xr = {xr:.4f}")