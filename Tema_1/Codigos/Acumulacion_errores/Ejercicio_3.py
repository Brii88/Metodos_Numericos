# 12. Uso de Decimal (equivalente a BigDecimal)
from decimal import Decimal
suma = Decimal("0")
inc = Decimal("0.1")
for i in range(10):
    suma += inc
print(suma)