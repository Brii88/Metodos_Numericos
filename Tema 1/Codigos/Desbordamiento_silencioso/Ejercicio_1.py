# 14. Desbordamiento de enteros (overflow)
# En Python los enteros no tienen límite, pero simulamos el comportamiento de Java con int de 32 bits
import ctypes
a = 2_000_000_000
b = 500_000_000
suma = ctypes.c_int32(a + b).value  # Simula overflow de Java
print("a =", a)
print("b =", b)
print("Suma =", suma)