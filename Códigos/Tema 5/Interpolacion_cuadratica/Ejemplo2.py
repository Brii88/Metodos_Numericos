x0, y0 = 0, 1
x1, y1 = 2, 4
x2, y2 = 5, 10


x = 3


L0 = ((x-x1)*(x-x2))/((x0-x1)*(x0-x2))
L1 = ((x-x0)*(x-x2))/((x1-x0)*(x1-x2))
L2 = ((x-x0)*(x-x1))/((x2-x0)*(x2-x1))


y = y0*L0 + y1*L1 + y2*L2


print("Resultado:", y)
