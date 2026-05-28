# Tema 4: Diferenciación e integración numérica

##  Concepto e Introducción
La integración numérica (cuadratura) estima el área bajo una curva cuando la función es difícil de integrar analíticamente. Se divide el intervalo en segmentos y se aproxima el área de cada uno usando polinomios.

##  Fórmulas Principales
* **Simpson 1/3:** $I = \frac{h}{3} [f(x_0) + 4f(x_1) + f(x_2)]$
* **Simpson 3/8:** $I = \frac{3h}{8} [f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)]$

##  Algoritmo y Pseudocódigo (Simpson 1/3)
**Algoritmo:**
1. Definir la función $f(x)$ y el intervalo $[a, b]$.
2. Calcular el punto medio $m = (a+b)/2$.
3. Aplicar la ponderación de la fórmula (extremos peso 1, medio peso 4).
4. Multiplicar por el ancho del intervalo dividido entre 6.

##  Ejemplos de este tema
> [!TIP]
> Implementaciones de Regla del Trapecio y Simpson 1/3 y 3/8 aquí:
> *  **[Ver Carpeta de Códigos](Codigos)**

**Pseudocódigo:**
```text
INICIO Simpson13(f, a, b)
  m <- (a + b) / 2
  I <- ((b - a) / 6) * (f(a) + 4*f(m) + f(b))
  ESCRIBIR I
FIN
