f = lambda x: x**3 - 2*x + 2
df = lambda x: 3*x**2 - 2
xn = 0
for i in range(1, 6):
    xn_sig = xn - f(xn) / df(xn)
    print(f"Iter {i}: x = {xn_sig}")
    xn = xn_sig