# Tema 4: Diferenciación e Integración Numérica

##  Concepto General
La integración numérica consiste en un conjunto de algoritmos que permiten calcular una aproximación del valor de una integral definida. En ingeniería, se utiliza cuando no conocemos la función analítica (solo tenemos puntos) o cuando la función es demasiado compleja para integrarse por métodos tradicionales. Se basa en aproximar la función por fragmentos de polinomios simples.

---

## 1. Método de Simpson 1/3
**Concepto:** Aproxima la función mediante polinomios de segundo grado (parábolas). Para aplicarlo, se requiere que el intervalo esté dividido en un número par de segmentos.

* **Fórmula:** $I = \frac{h}{3} [f(x_0) + 4f(x_1) + f(x_2)]$
* **Algoritmo:**
    1. Definir la función y los límites $a$ y $b$.
    2. Calcular el tamaño del paso $h = (b-a)/2$.
    3. Identificar $x_0, x_1$ (punto medio) y $x_2$.
    4. Aplicar la suma ponderada: extremos con peso 1 y centro con peso 4.
* **Pseudocódigo:**
    ```text
    INICIO Simpson13(f, a, b)
      h <- (b - a) / 2
      x1 <- a + h
      I <- (h / 3) * (f(a) + 4*f(x1) + f(b))
      MOSTRAR I
    FIN
    ```
*  **[Ver Código: Simpson 1/3](Codigos/Metodo_simpson_1)**

---

## 2. Método de Simpson 3/8
**Concepto:** A diferencia del anterior, este método aproxima la función mediante un polinomio de tercer grado (cúbico). Es ideal cuando el intervalo se divide en un número de segmentos múltiplo de 3.

* **Fórmula:** $I = \frac{3h}{8} [f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)]$
* **Algoritmo:**
    1. Dividir el intervalo $[a, b]$ en 3 partes iguales.
    2. Calcular $h = (b-a)/3$.
    3. Determinar los 4 puntos de evaluación.
    4. Aplicar los pesos 1-3-3-1 a los valores de la función.
* **Pseudocódigo:**
    ```text
    INICIO Simpson38(f, a, b)
      h <- (b - a) / 3
      x1 <- a + h
      x2 <- a + 2*h
      I <- (3 * h / 8) * (f(a) + 3*f(x1) + 3*f(x2) + f(b))
      MOSTRAR I
    FIN
    ```
*  **[Ver Código: Simpson 3/8](Codigos/Metodo_simpson_2)**

---

## 3. Método del Trapecio
**Concepto:** Es el método más sencillo de integración numérica. Consiste en aproximar el área bajo la curva mediante la formación de un trapecio bajo el segmento de la función, uniendo los puntos con una línea recta.

* **Fórmula:** $I = (b - a) \frac{f(a) + f(b)}{2}$
* **Algoritmo:**
    1. Obtener los límites del intervalo.
    2. Evaluar la función en los extremos.
    3. Calcular el promedio de las alturas y multiplicar por la base.
* **Pseudocódigo:**
    ```text
    INICIO Trapecio(f, a, b)
      I <- (b - a) * (f(a) + f(b)) / 2
      MOSTRAR I
    FIN
    ```
*  **[Ver Código: Método del Trapecio](Codigos/Metodo_trapecio)**

---

## 4. Regla de los 3 Puntos
**Concepto:** Basada en las fórmulas de Newton-Cotes, esta regla utiliza tres puntos específicos dentro de un intervalo para mejorar la precisión de la aproximación de la integral o de la derivada en un punto central.

* **Algoritmo:**
    1. Seleccionar tres puntos equidistantes.
    2. Evaluar la función en cada punto.
    3. Aplicar los coeficientes correspondientes para obtener la aproximación numérica.
* **Pseudocódigo:**
    ```text
    INICIO Regla3Puntos(f, x, h)
      f1 <- f(x - h)
      f2 <- f(x)
      f3 <- f(x + h)
      resultado <- (3 * h / 2) * (f1 + f2 + f3)  // Ejemplo para integración
      MOSTRAR resultado
    FIN
    ```
*  **[Ver Código: Regla de 3 Puntos](Codigos/Regla_3_puntos)**

---

> [!TIP]
> Recuerda que para los métodos de Simpson, la precisión aumenta significativamente si divides el intervalo total en muchos subintervalos pequeños (Reglas compuestas).
