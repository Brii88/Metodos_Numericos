---

### Tema 2: Métodos de Solución de Ecuaciones
**Archivo:** `Tema_2/README.md`

```markdown
# Tema 2: Métodos de Solución de Ecuaciones

##  Concepto e Introducción
Este tema trata sobre encontrar las "raíces" o soluciones de ecuaciones no lineales de la forma $f(x) = 0$. Utilizamos métodos cerrados (que aseguran convergencia en un intervalo) y métodos abiertos (más rápidos pero que pueden divergir).

##  Fórmulas Principales
* **Bisección:** $xr = \frac{a + b}{2}$
* **Newton-Raphson:** $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$
* **Secante:** $x_{i+1} = x_i - \frac{f(x_i)(x_{i-1} - x_i)}{f(x_{i-1}) - f(x_i)}$

##  Ejemplos de este tema
> [!TIP]
> Aquí tienes los algoritmos de Bisección, Regla Falsa y Newton-Raphson:
> *  **[Ver Código: Solución de Ecuaciones](Codigos)**

##  Algoritmo y Pseudocódigo (Bisección)
**Pseudocódigo:**
```text
INICIO Biseccion(f, a, b, tol)
  SI f(a) * f(b) >= 0 ENTONCES retornar ERROR
  MIENTRAS (b - a) / 2 > tol HACER
    xr <- (a + b) / 2
    SI f(a) * f(xr) < 0 ENTONCES
      b <- xr
    SINO
      a <- xr
  FIN MIENTRAS
  RETORNAR xr
FIN
