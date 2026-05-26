def Gseid(a, b, n, x, imax, es, lmbda):
    # Normalización de la matriz
    for i in range(n):
        dummy = a[i][i]
        for j in range(n):
            a[i][j] = a[i][j] / dummy
        b[i] = b[i] / dummy

    # Primera iteración
    for i in range(n):
        suma = b[i]
        for j in range(n):
            if i != j:
                suma -= a[i][j] * x[j]
        x[i] = suma

    iteraciones = 1

    while True:
        centinela = True

        for i in range(n):
            old = x[i]
            suma = b[i]

            for j in range(n):
                if i != j:
                    suma -= a[i][j] * x[j]

            # Relajación
            x[i] = lmbda * suma + (1.0 - lmbda) * old

            # Error aproximado
            if x[i] != 0:
                ea = abs((x[i] - old) / x[i]) * 100
                if ea > es:
                    centinela = False

        iteraciones += 1

        if centinela or iteraciones >= imax:
            break

    return x, iteraciones