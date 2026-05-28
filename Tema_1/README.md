# Tema 1: Introducción a los Métodos Numéricos

##  Concepto General
Los métodos numéricos son procedimientos mediante los cuales se obtienen soluciones aproximadas a problemas matemáticos complejos utilizando únicamente operaciones aritméticas simples. En computación, esto implica lidiar con la representación binaria de los números, lo que genera limitaciones de precisión y almacenamiento.

---

## 1. Acumulación de Errores
**Concepto:** Ocurre cuando un pequeño error de redondeo se repite muchas veces en un ciclo, haciendo que la diferencia final sea significativa.

* **Algoritmo:**
    1. Definir una variable en 0.0.
    2. Sumar repetidamente un valor fraccionario (ej. 0.1).
    3. Comparar el resultado obtenido con el valor matemático esperado.
* **Pseudocódigo:**
    ```text
    INICIO
      suma <- 0.0
      REPETIR 10 VECES:
        suma <- suma + 0.1
      FIN REPETIR
      MOSTRAR suma
    FIN
    ```
*  **[Ver Código: Acumulación de Errores](../Codigos/Acumulacion_errores)**

---

## 2. Cancelación por Resta (Catastrófica)
**Concepto:** Pérdida de dígitos significativos al restar dos números casi iguales, donde el error relativo se dispara.

* **Fórmula:** $Error = |(a - b) - (\text{valor\_real})|$
* **Algoritmo:**
    1. Definir dos valores con mínima diferencia decimal.
    2. Restar el valor `b` del valor `a`.
    3. Analizar cuántos dígitos de precisión se perdieron en el resultado.
* **Pseudocódigo:**
    ```text
    INICIO
      a <- 1.000000
      b <- 0.9999999999
      resultado <- a - b
      ESCRIBIR resultado
    FIN
    ```
*  **[Ver Código: Cancelación Resta](../Codigos/Cancelacion_resta)**

---

## 3. Comparación Directa
**Concepto:** Error de lógica al intentar comparar dos números flotantes con el operador de igualdad (`==`), debido a que su representación interna rara vez es exacta.

* **Algoritmo:**
    1. Realizar una operación aritmética que resulte en un valor conocido (ej. 0.1 + 0.1 + 0.1).
    2. Comparar el resultado directamente contra el valor esperado (0.3).
    3. Mostrar por qué la comparación devuelve "Falso".
* **Pseudocódigo:**
    ```text
    INICIO
      a <- 0.1 + 0.1 + 0.1
      b <- 0.3
      SI a == b ENTONCES "Iguales" SINO "Diferentes"
    FIN
    ```
*  **[Ver Código: Comparación Directa](../Codigos/Comparacion_directa)**

---

## 4. Conversión Estrecha (Truncado)
**Concepto:** Sucede al convertir un tipo de dato de mayor precisión (como `float`) a uno de menor precisión (como `int`), descartando la parte decimal.

* **Algoritmo:**
    1. Definir un número decimal (precio o medida).
    2. Aplicar una función de conversión a entero.
    3. Calcular la "pérdida" restando el entero del original.
* **Pseudocódigo:**
    ```text
    INICIO
      precio <- 99.99
      entero <- TRUNCAR(precio)
      perdida <- precio - entero
      ESCRIBIR perdida
    FIN
    ```
*  **[Ver Código: Conversión Estrecha](../Codigos/Conversion_estrecha)**

---

## 5. Desbordamiento Silencioso (Overflow)
**Concepto:** Ocurre cuando el resultado de una operación excede el valor máximo que el tipo de dato puede almacenar.

* **Algoritmo:**
    1. Definir una variable con el valor máximo permitido por el sistema (ej. 32 bits).
    2. Sumar un valor adicional.
    3. Observar cómo el número "da la vuelta" a un valor negativo o incorrecto.
* **Pseudocódigo:**
    ```text
    INICIO
      a <- 2,000,000,000
      b <- 500,000,000
      suma <- a + b (limitado a 32 bits)
      MOSTRAR suma
    FIN
    ```
*  **[Ver Código: Desbordamiento Silencioso](../Codigos/Desbordamiento_silencioso)**

---

## 6. Error de Redondeo
**Concepto:** La diferencia entre el valor exacto y el valor representado en la computadora debido a la limitación de bits.

* **Algoritmo:**
    1. Definir dos fracciones simples (0.1 y 0.2).
    2. Realizar la suma.
    3. Observar el residuo decimal al final del resultado.
* **Pseudocódigo:**
    ```text
    INICIO
      resultado <- 0.1 + 0.2
      ESCRIBIR resultado
    FIN
    ```
*  **[Ver Código: Error de Redondeo](../Codigos/Error_redondeo)**

---

## 7. Pérdida de Precisión
**Concepto:** Sucede al operar números de magnitudes muy diferentes (uno muy grande y uno muy pequeño), donde el pequeño es "ignorado" por el grande.

* **Algoritmo:**
    1. Definir un número muy grande ($1.0 \times 10^{16}$).
    2. Sumar un número pequeño (1.0).
    3. Comprobar si el resultado es igual al número grande original.
* **Pseudocódigo:**
    ```text
    INICIO
      grande <- 1.0e16
      pequeno <- 1.0
      resultado <- grande + pequeno
      SI resultado == grande ENTONCES "Perdió precisión"
    FIN
    ```
*  **[Ver Código: Pérdida de Precisión](../Codigos/Perdida_precision)**

---

> [!IMPORTANT]
> Todos los ejemplos prácticos de estos conceptos se encuentran en la carpeta de códigos general del repositorio.
