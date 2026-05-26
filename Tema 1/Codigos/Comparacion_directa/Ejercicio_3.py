# 9. Comparación con epsilon
import math
a = 0.1 + 0.1 + 0.1
b = 0.3
epsilon = 0.00001
print(math.fabs(a - b) < epsilon)