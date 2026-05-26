import numpy as np 

A = np.array([
    [5.0, 2.0, -3.0],
    [2.0, 10.0, -8.0],
    [3.0, 8.0, 13.0]
])

b = np.array([1.0, 4.0, 7.0])

n = len(A)

x0 = np.array([1.0, 1.0, 1.0])
x = x0.copy()  

nmax = 100
eps = 1e-10

k = 1

while k <= nmax:

    for i in range(n):
        suma = 0.0
        for j in range(n):
            if j != i:
                suma += A[i, j] * x0[j]
        x[i] = (b[i] - suma) / A[i, i]

    error = max(abs(x - x0))

    if error < eps:
        print("MÉTODO DE JACOBI")
        print("1) la solución es =", round(x[0],4), round(x[1],4), round(x[2],4))
        print("2) itera =", k)
        print("3) error =", round(error,10))
        break

    x0 = x.copy()
    k += 1

if k > nmax:
    print("no converge")