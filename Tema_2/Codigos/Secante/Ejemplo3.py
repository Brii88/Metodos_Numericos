f = lambda x: x**2 + 4
x0, x1 = -2, 2
# Nota: f(-2) = 8 y f(2) = 8, causará división por cero
try:
    x_sig = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
except ZeroDivisionError:
    print("Error: Los valores de f(x) son iguales, no se puede calcular.")