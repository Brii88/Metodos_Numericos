# Tema 3: Sistemas de Ecuaciones Lineales

##  Concepto e Introducción
Consiste en resolver un conjunto de ecuaciones simultáneas. Se dividen en métodos directos (como Gauss-Jordan) y métodos iterativos (como Jacobi o Gauss-Seidel) que se aproximan a la solución en cada paso.

##  Algoritmo (Gauss-Jordan)
1. Para cada fila (pivote):
2. Normalizar la fila dividiendo entre el elemento de la diagonal.
3. Eliminar los elementos de las otras filas en esa misma columna restando múltiplos de la fila pivote.
4. La matriz resultante contiene las soluciones directamente.

##  Ejemplos del Tema
Implementaciones de eliminación y métodos iterativos:
* 🔗 [Ver códigos de Sistemas Lineales](Codigos)

**Pseudocódigo:**
```text
INICIO Jacobi(A, b, x0, tol, max_iter)
  PARA k desde 1 HASTA max_iter HACER
    PARA i desde 1 HASTA n HACER
      suma = 0
      PARA j desde 1 HASTA n HACER
        SI i != j ENTONCES
          suma = suma + A[i,j] * x0[j]
      FIN SI
    FIN PARA
    x_nuevo[i] = (b[i] - suma) / A[i,i]
  FIN PARA
  SI norma(x_nuevo - x0) < tol ENTONCES RETORNAR x_nuevo
  x0 = x_nuevo
FIN
