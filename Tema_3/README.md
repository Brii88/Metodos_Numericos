# Tema 3: Métodos de Solución de Sistemas de Ecuaciones

##  Concepto General
Este tema se enfoca en resolver sistemas de ecuaciones lineales de la forma $Ax = b$. Encontrar el vector de incógnitas $x$ es fundamental en ingeniería para el análisis de estructuras, redes eléctricas y dinámica de sistemas. Los métodos se dividen en **Directos** (llegan a la solución exacta en pasos finitos) e **Iterativos** (se aproximan a la solución mediante repeticiones).

---

## 1. Eliminación de Gauss-Jordan
**Concepto:** Es un método directo que transforma la matriz de coeficientes en una matriz identidad mediante operaciones elementales entre filas. Al finalizar, el vector de términos independientes se convierte en la solución del sistema.

* **Algoritmo:**
    1. Crear la matriz aumentada $[A|b]$.
    2. Para cada columna, seleccionar un pivote y normalizar su fila a 1.
    3. Eliminar los elementos por encima y por debajo del pivote haciendo ceros.
    4. Leer directamente los valores de las incógnitas.
* **Pseudocódigo:**
    ```text
    INICIO GaussJordan
      PARA i desde 0 HASTA n-1 HACER
        Normalizar fila A[i] dividiendo entre A[i][i]
        PARA k desde 0 HASTA n-1 HACER
          SI k != i ENTONCES
            Restar múltiplo de fila i a fila k para hacer A[k][i] = 0
          FIN SI
        FIN PARA
      FIN PARA
    FIN
    ```
*  **[Ver Códigos: Gauss-Jordan](Codigos/Eliminacion_Gauss_Jordan)**

---

## 2. Eliminación Gaussiana
**Concepto:** A diferencia de Gauss-Jordan, este método solo busca transformar la matriz en una triangular superior (hacer ceros debajo de la diagonal). Una vez obtenida, se utiliza la **sustitución hacia atrás** para hallar los valores.

* **Fórmula (Sustitución):** $x_i = \frac{b_i - \sum_{j=i+1}^{n} a_{ij}x_j}{a_{ii}}$
* **Algoritmo:**
    1. Fase de eliminación: Transformar la matriz a triangular superior.
    2. Fase de sustitución: Resolver desde la última incógnita hasta la primera.
* **Pseudocódigo:**
    ```text
    INICIO EliminacionGaussiana
      PARA i desde 0 HASTA n-1 HACER
        PARA k desde i+1 HASTA n-1 HACER
          Factor <- A[k][i] / A[i][i]
          Fila[k] <- Fila[k] - Factor * Fila[i]
        FIN PARA
      FIN PARA
      Sustitución_Hacia_Atrás()
    FIN
    ```
*  **[Ver Códigos: Eliminación Gaussiana](Codigos/Eliminacion_Gaussiana)**

---

## 3. Método de Jacobi
**Concepto:** Es un método iterativo que descompone el sistema para despejar cada incógnita. En cada iteración, se utilizan únicamente los valores de la iteración anterior para calcular los nuevos.

* **Fórmula:** $x_i^{(k+1)} = \frac{b_i - \sum_{j \neq i} a_{ij} x_j^{(k)}}{a_{ii}}$
* **Algoritmo:**
    1. Empezar con un vector de aproximación inicial $x_0$.
    2. Calcular cada $x_i$ nuevo usando los valores viejos.
    3. Comparar el error relativo con la tolerancia.
    4. Repetir hasta converger.
* **Pseudocódigo:**
    ```text
    INICIO Jacobi
      MIENTRAS error > tolerancia HACER
        PARA i desde 0 HASTA n-1 HACER
          suma <- 0
          PARA j desde 0 HASTA n-1 HACER
            SI i != j ENTONCES suma <- suma + A[i][j] * x_viejo[j]
          FIN PARA
          x_nuevo[i] <- (b[i] - suma) / A[i][i]
        FIN PARA
        error <- Norma(x_nuevo - x_viejo)
        x_viejo <- x_nuevo
      FIN MIENTRAS
    FIN
    ```
*  **[Ver Códigos: Jacobi](Codigos/Jacobi)**

---

## 4. Método de Gauss-Seidel
**Concepto:** Es una mejora del método de Jacobi. La diferencia principal es que, en cuanto se calcula un nuevo valor de una incógnita, este se usa inmediatamente para calcular las siguientes incógnitas dentro de la misma iteración.

* **Algoritmo:**
    1. Definir valores iniciales.
    2. Calcular $x_i$ e incorporarlo al vector de solución al instante.
    3. Aplicar frecuentemente un factor de relajación para acelerar la convergencia.
* **Pseudocódigo:**
    ```text
    INICIO GaussSeidel
      MIENTRAS error > tolerancia HACER
        PARA i desde 0 HASTA n-1 HACER
          suma <- 0
          PARA j desde 0 HASTA n-1 HACER
            SI i != j ENTONCES suma <- suma + A[i][j] * x[j]
          FIN PARA
          x[i] <- (b[i] - suma) / A[i][i]
        FIN PARA
      FIN MIENTRAS
    FIN
    ```
*  **[Ver Códigos: Gauss-Seidel](Codigos/Gauss_Seidel)**

---

> [!IMPORTANT]
> Para los métodos iterativos (Jacobi y Gauss-Seidel), el sistema debe ser **diagonalmente dominante** para asegurar que la solución converja.
