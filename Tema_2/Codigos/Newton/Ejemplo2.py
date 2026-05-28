f = lambda x: x**3 - x - 1
df = lambda x: 3*x**2 - 1
xn = 2 # Punto inicial
for i in range(1, 6):
    xn_sig = xn - f(xn) / df(xn)
    error = abs((xn_sig - xn) / xn_sig) * 100
    print(f"Iter {i}: x = {xn_sig:.6f}, Error = {error:.2f}%")
    xn = xn_sig