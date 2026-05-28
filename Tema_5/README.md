# Tema 5: Interpolación y ajuste de funciones

##  Concepto e Introducción
El ajuste de curvas busca una función que mejor represente un conjunto de datos. La **Regresión** se usa cuando hay incertidumbre en los datos, mientras que la **Interpolación** se usa cuando queremos que la curva pase exactamente por todos los puntos.

##  Fórmulas Principales
* **Regresión Lineal:** $y = a_0 + a_1x$
* **Interpolación de Lagrange:** $P(x) = \sum L_i(x) f(x_i)$

##  Algoritmo y Pseudocódigo (Interpolación Lineal)
**Algoritmo:**
1. Tomar dos puntos conocidos $(x_0, y_0)$ y $(x_1, y_1)$.
2. Calcular la pendiente entre ellos.
3. Aplicar la fórmula para hallar el valor de $y$ para un $x$ intermedio.

##  Ejemplos de este tema
> [!TIP]
> Modelos de regresión, Lagrange e interpolación lineal aquí:
> *  **[Ver Carpeta de Códigos](Codigos)**

**Pseudocódigo:**
```text
INICIO InterpolacionLineal(x0, y0, x1, y1, x)
  y <- y0 + ((x - x0) * (y1 - y0)) / (x1 - x0)
  ESCRIBIR y
FIN
