# Extrapolación 

# Datos 
x = [10, 20]
y = [120, 150]

valor = 50

resultado = 0

# Método
for i in range(len(x)):

    termino = y[i]

    for j in range(len(x)):

        if i != j:
            termino *= (valor - x[j]) / (x[i] - x[j])

    resultado += termino

# Resultado
print("Tiempo estimado de respuesta:", resultado, "ms")