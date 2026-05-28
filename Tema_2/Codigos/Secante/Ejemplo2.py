f = lambda x: x**3 - x - 1
x0, x1 = 1, 2
for i in range(1, 6):
    x_sig = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    print(f"Iter {i}: x_nuevo = {x_sig:.6f}")
    x0, x1 = x1, x_sig