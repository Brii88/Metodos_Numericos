f = lambda x: x**2 - 5
x0, x1 = 2, 3
for i in range(1, 6):
    x_sig = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
    print(f"Iter {i}: Raíz aprox = {x_sig:.6f}")
    x0, x1 = x1, x_sig