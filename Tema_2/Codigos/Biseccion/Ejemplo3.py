f = lambda x: x**3 - x - 1
a, b = 1, 2
print(f"{'Iter':<5}{'a':<10}{'b':<10}{'Xr':<10}{'f(Xr)':<10}")
for i in range(1, 6):
    xr = (a + b) / 2
    fxr = f(xr)
    print(f"{i:<5}{a:<10.4f}{b:<10.4f}{xr:<10.4f}{fxr:<10.4f}")
    if f(a) * fxr < 0:
        b = xr
    else:
        a = xr
