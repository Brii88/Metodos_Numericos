# 17. Truncado de número grande a int
import sys
distancia_km = 5_000_000_000.0
distancia_int = int(distancia_km)
INT_MAX = 2_147_483_647  # Máximo de int en Java (32 bits)
print("Distancia real:", distancia_km, "km")
print("Distancia en int:", distancia_int, "km")
# En Python no hay truncado al máximo de int, pero verificamos igual
if distancia_int >= INT_MAX:
    print("¡ADVERTENCIA! El valor fue truncado al máximo de int")