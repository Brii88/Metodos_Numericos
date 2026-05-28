f = lambda x: x**3 - 2*x + 2
x0, x1 = -3, -1
for i in range(1, 6):
    x_sig = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    print(f"Paso {i}: x = {x_sig:.6f}")
    x0, x1 = x1, x_sig