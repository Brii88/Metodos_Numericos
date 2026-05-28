# Tema 2: Métodos de Solución de Ecuaciones

##  Concepto General
Este tema se enfoca en encontrar los valores de $x$ (raíces) que satisfacen la ecuación $f(x) = 0$. En ingeniería, esto es fundamental para resolver problemas donde no existe un despeje algebraico directo. Los métodos se dividen en **cerrados** (requieren un intervalo que encierre la raíz) y **abiertos** (requieren uno o más puntos iniciales y son más rápidos).

---

## 1. Método de Bisección
**Concepto:** Es un método cerrado que divide repetidamente un intervalo a la mitad. Se basa en el teorema de valor intermedio: si una función cambia de signo en un intervalo, existe al menos una raíz.

* **Fórmula:** $xr = \frac{a + b}{2}$
* **Algoritmo:**
    1. Elegir un intervalo $[a, b]$ tal que $f(a) \cdot f(b) < 0$.
    2. Calcular el punto medio $xr$.
    3. Determinar en qué subintervalo está la raíz evaluando el signo.
    4. Repetir hasta que el error sea menor a la tolerancia.
* **Pseudocódigo:**
    ```text
    INICIO Biseccion
      MIENTRAS (b - a) / 2 > tol HACER
        xr <- (a + b) / 2
        SI f(a) * f(xr) < 0 ENTONCES
          b <- xr
        SINO
          a <- xr
      FIN MIENTRAS
      RETORNAR xr
    FIN
    ```
*  **[Ver Códigos: Bisección](Codigos/Biseccion.py)**

---

## 2. Método de Newton-Raphson
**Concepto:** Es un método abierto que utiliza la derivada de la función para encontrar una aproximación mejorada de la raíz mediante la recta tangente.

* **Fórmula:** $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
* **Algoritmo:**
    1. Elegir un valor inicial $x_0$.
    2. Calcular la pendiente (derivada) en ese punto.
    3. Proyectar la tangente al eje $x$ para hallar el siguiente punto.
    4. Repetir hasta que la diferencia entre iteraciones sea mínima.
* **Pseudocódigo:**
    ```text
    INICIO Newton
      xn <- x0
      REPETIR
        x_sig <- xn - f(xn) / f_der(xn)
        error <- ABS(x_sig - xn)
        xn <- x_sig
      HASTA error < tol
      RETORNAR xn
    FIN
    ```
*  **[Ver Códigos: Newton-Raphson](Codigos/Newton.py)**

---

## 3. Método de la Regla Falsa (Falsa Posición)
**Concepto:** Similar a la bisección por ser un método cerrado, pero une los puntos $f(a)$ y $f(b)$ con una línea recta. La intersección de esta línea con el eje $x$ suele acercarse más rápido a la raíz.

* **Fórmula:** $xr = b - \frac{f(b)(a - b)}{f(a) - f(b)}$
* **Algoritmo:**
    1. Definir intervalo $[a, b]$ con cambio de signo.
    2. Calcular $xr$ usando la fórmula de la pendiente.
    3. Evaluar el signo de $f(a) \cdot f(xr)$ para ajustar el intervalo.
    4. Repetir hasta alcanzar la precisión deseada.
* **Pseudocódigo:**
    ```text
    INICIO ReglaFalsa
      REPETIR
        xr <- b - (f(b) * (a - b)) / (f(a) - f(b))
        SI f(a) * f(xr) < 0 ENTONCES b <- xr SINO a <- xr
      HASTA ABS(f(xr)) < tol
      RETORNAR xr
    FIN
    ```
*  **[Ver Códigos: Regla Falsa](Codigos/Regla_Falsa.py)**

---

## 4. Método de la Secante
**Concepto:** Es una variación del método de Newton que no requiere conocer la derivada de la función. En su lugar, utiliza una diferencia finita basada en dos puntos iniciales.

* **Fórmula:** $x_{i+1} = x_i - \frac{f(x_i)(x_{i-1} - x_i)}{f(x_{i-1}) - f(x_i)}$
* **Algoritmo:**
    1. Elegir dos puntos iniciales $x_0$ y $x_1$.
    2. Calcular el siguiente punto usando la aproximación de la secante.
    3. Desplazar los puntos: el nuevo $x_0$ es el viejo $x_1$, y el nuevo $x_1$ es el resultado obtenido.
    4. Repetir hasta la convergencia.
* **Pseudocódigo:**
    ```text
    INICIO Secante
      REPETIR
        x_sig <- x1 - (f(x1) * (x0 - x1)) / (f(x0) - f(x1))
        x0 <- x1
        x1 <- x_sig
      HASTA ABS(x1 - x0) < tol
      RETORNAR x1
    FIN
    ```
*  **[Ver Códigos: Secante](Codigos/Secante.py)**

---

> [!IMPORTANT]
> Los métodos abiertos (Newton y Secante) son más rápidos pero requieren que el valor inicial esté cerca de la raíz para evitar que el algoritmo diverja.
