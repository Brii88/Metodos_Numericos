# Tema 6: Solución de Ecuaciones Diferenciales

##  Concepto e Introducción
Las ecuaciones diferenciales ordinarias (EDO) describen sistemas que cambian en el tiempo o espacio. Los métodos numéricos resuelven problemas de valor inicial calculando la pendiente en puntos sucesivos para predecir el siguiente valor.

##  Fórmulas Principales
* *Método de Euler:* $y_{i+1} = y_i + f(x_i, y_i)h$
* *Runge-Kutta 4to Orden:* Usa 4 pendientes promediadas ($k_1, k_2, k_3, k_4$).

##  Algoritmo y Pseudocódigo (Euler)
*Algoritmo:*
1. Definir punto inicial $(x_0, y_0)$ y tamaño de paso $h$.
2. Calcular la pendiente $f(x, y)$.
3. Actualizar $y$ sumando el producto de la pendiente por el paso.
4. Incrementar $x$ por el paso y repetir.

##  Ejemplos de este tema
> [!TIP]
> Métodos de Euler, Taylor y Runge-Kutta (RK4) aquí:
> *  *[Ver Carpeta de Códigos](Codigos)*

*Pseudocódigo:*
```text
INICIO Euler(f, x0, y0, h, pasos)
  x <- x0
  y <- y0
  PARA i desde 0 HASTA pasos HACER
    ESCRIBIR x, y
    y <- y + h * f(x, y)
    x <- x + h
  FIN PARA
FIN
