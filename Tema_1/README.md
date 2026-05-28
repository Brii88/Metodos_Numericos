# Tema 1: Introducción a los Métodos Numéricos

##  Concepto e Introducción
Los métodos numéricos son técnicas mediante las cuales es posible formular problemas matemáticos de tal forma que puedan resolverse usando operaciones aritméticas. En sistemas computacionales, es vital entender cómo la computadora maneja los números de punto flotante, ya que esto introduce errores de redondeo y truncamiento.

##  Conceptos Clave
* **Error de Redondeo:** Originado por la capacidad limitada de la memoria para almacenar dígitos.
* **Cancelación Catastrófica:** Ocurre al restar números muy cercanos entre sí, perdiendo dígitos significativos.
* **Overflow:** Cuando un número excede el límite máximo de almacenamiento.

##  Algoritmo y Pseudocódigo (Suma de Flotantes)
**Algoritmo:**
1. Inicializar una variable acumuladora en 0.0.
2. Definir el valor de incremento (0.1).
3. Repetir la suma 10 veces.
4. Mostrar el resultado y observar la precisión decimal.

**Pseudocódigo:**
```text
INICIO
  suma <- 0.0
  PARA i desde 1 HASTA 10 HACER
    suma <- suma + 0.1
  FIN PARA
  ESCRIBIR suma
FIN

##  Ejemplos de este tema
> [!TIP]
> Puedes ver la implementación de errores de precisión, cancelación catastrófica y overflow aquí:
> *  **[Ver Código: Errores y Precisión](Codigos)**
