f = lambda x: x**2 + 4
df = lambda x: 2*x
xn = 1
for i in range(1, 6):
    xn_sig = xn - f(xn) / df(xn)
    print(f"Paso {i}: x = {xn_sig:.4f}")
    xn = xn_sig