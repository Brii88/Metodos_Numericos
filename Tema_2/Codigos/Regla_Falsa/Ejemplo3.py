f = lambda x: x**2 + 4
a, b = -2, 2
try:
    for i in range(1, 4):
        xr = b - (f(b) * (a - b)) / (f(a) - f(b))
        print(f"Iter {i}: xr = {xr}")
except ZeroDivisionError:
    print("Error: División por cero (f(a) y f(b) son iguales)")