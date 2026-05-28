# Tema 5: Interpolación y Ajuste de Funciones

##  Concepto General
El ajuste de funciones busca encontrar una expresión matemática que describa mejor un conjunto de datos experimentales. Se divide en dos grandes enfoques: la **Regresión**, que se usa cuando los datos tienen ruido y buscamos la tendencia general; y la **Interpolación**, que se usa cuando necesitamos que la función pase exactamente por cada uno de los puntos conocidos para estimar valores intermedios.

---

## 1. Coeficiente de Correlación
**Concepto:** Es una medida estadística que indica la fuerza y la dirección de la relación lineal entre dos variables. El valor de $r$ oscila entre -1 y 1.

* **Fórmula:** $r = \frac{n\sum xy - (\sum x)(\sum y)}{\sqrt{[n\sum x^2 - (\sum x)^2][n\sum y^2 - (\sum y)^2]}}$
* **Algoritmo:**
    1. Calcular las sumatorias de $x, y, x^2, y^2$ y $xy$.
    2. Aplicar la fórmula del coeficiente de Pearson.
    3. Interpretar el resultado (cerca de 1 es relación fuerte positiva).
* **Pseudocódigo:**
    ```text
    INICIO Correlacion(x, y, n)
      Calcular sum_x, sum_y, sum_x2, sum_y2, sum_xy
      numerador <- (n * sum_xy) - (sum_x * sum_y)
      denominador <- SQRT((n * sum_x2 - sum_x^2) * (n * sum_y2 - sum_y^2))
      r <- numerador / denominador
      ESCRIBIR r
    FIN
    ```
*  **[Ver Códigos: Correlación](Codigos/Correlacion)**

---

## 2. Interpolación Lineal
**Concepto:** Es la forma más simple de interpolación. Consiste en conectar dos puntos conocidos con una línea recta para estimar un valor intermedio.

* **Fórmula:** $y = y_0 + \frac{y_1 - y_0}{x_1 - x_0}(x - x_0)$
* **Algoritmo:**
    1. Identificar los dos puntos $(x_0, y_0)$ y $(x_1, y_1)$ que rodean al valor buscado $x$.
    2. Calcular la pendiente de la recta.
    3. Resolver para la incógnita $y$.
* **Pseudocódigo:**
    ```text
    INICIO InterpolacionLineal(x0, y0, x1, y1, x)
      y <- y0 + ((x - x0) * (y1 - y0)) / (x1 - x0)
      ESCRIBIR y
    FIN
    ```
*  **[Ver Códigos: Interpolación Lineal](Codigos/Interpolacion_lineal)**

---

## 3. Interpolación Cuadrática
**Concepto:** Utiliza un polinomio de segundo grado (parábola) para unir tres puntos. Ofrece una mejor aproximación que la lineal si la función original tiene curvatura.

* **Algoritmo:**
    1. Tomar tres puntos: $(x_0, y_0), (x_1, y_1)$ y $(x_2, y_2)$.
    2. Resolver el sistema de ecuaciones o usar la forma de Lagrange para polinomios de grado 2.
    3. Calcular el valor de $y$ para el $x$ deseado.
* **Pseudocódigo:**
    ```text
    INICIO InterpolacionCuadratica(x0, y0, x1, y1, x2, y2, x)
      L0 <- ((x-x1)*(x-x2)) / ((x0-x1)*(x0-x2))
      L1 <- ((x-x0)*(x-x2)) / ((x1-x0)*(x1-x2))
      L2 <- ((x-x0)*(x-x1)) / ((x2-x0)*(x2-x1))
      y <- y0*L0 + y1*L1 + y2*L2
      ESCRIBIR y
    FIN
    ```
*  **[Ver Códigos: Interpolación Cuadrática](Codigos/Interpolacion_cuadratica)**

---

## 4. Interpolación Segmentada (Splines)
**Concepto:** En lugar de usar un solo polinomio para todos los puntos, se utilizan polinomios de bajo grado (usualmente lineales o cúbicos) entre cada par de puntos adyacentes para evitar oscilaciones bruscas.

* **Algoritmo:**
    1. Ordenar los puntos de forma ascendente.
    2. Definir una función por intervalos.
    3. Asegurar que las piezas se unan suavemente en los "nodos".
* **Pseudocódigo:**
    ```text
    INICIO InterpolacionSegmentada(X_vector, Y_vector, x_buscar)
      BUSCAR el intervalo donde se encuentra x_buscar
      APLICAR interpolación lineal en ese intervalo específico
      RETORNAR y
    FIN
    ```
*  **[Ver Códigos: Interpolación Segmentada](Codigos/Interpolacion_segmentada)**

---

## 5. Regresión Lineal
**Concepto:** Técnica que busca la "línea de mejor ajuste" a través de un conjunto de datos, minimizando la suma de los cuadrados de las diferencias (mínimos cuadrados).

* **Fórmula:** $y = a_0 + a_1x$
* **Algoritmo:**
    1. Calcular las sumatorias necesarias ($x, y, x^2, xy$).
    2. Calcular la pendiente $a_1$ y la intersección $a_0$.
    3. Formular la ecuación de la recta resultante.
* **Pseudocódigo:**
    ```text
    INICIO Regresion(x, y, n)
      a1 <- (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x^2)
      a0 <- (sum_y / n) - a1 * (sum_x / n)
      ESCRIBIR "Ecuación: y = a0 + a1x"
    FIN
    ```
*  **[Ver Códigos: Regresión](Codigos/Regresion)**

---

## 6. Extrapolación
**Concepto:** Consiste en estimar valores **fuera** del rango de los puntos conocidos, asumiendo que la tendencia o el modelo se mantiene constante más allá de los datos medidos.

* **Algoritmo:**
    1. Definir un modelo (lineal o polinomial) basado en los datos existentes.
    2. Evaluar el modelo en un punto $x$ que sea menor al mínimo o mayor al máximo conocido.
* **Pseudocódigo:**
    ```text
    INICIO Extrapolacion(puntos, x_fuera)
      Modelo <- GenerarModelo(puntos)
      resultado <- Modelo(x_fuera)
      ESCRIBIR resultado
    FIN
    ```
*  **[Ver Código: Extrapolación](Codigos/Extrapolacion.py)**

---

> [!CAUTION]
> Ten cuidado con la extrapolación; entre más lejos estés del rango de datos originales, menor será la confiabilidad de la predicción.
