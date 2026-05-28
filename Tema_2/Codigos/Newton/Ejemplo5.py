import math
f = lambda x: math.cos(x) - x
df = lambda x: -math.sin(x) - 1
xn = 0.5
for i in range(1, 6):
    xn_sig = xn - f(xn) / df(xn)
    print(f"Iter {i}: x = {xn_sig:.6f}")
    xn = xn_sig