X1 = float(input("x1:"))
X2 = float(input("x2:"))

Y1 = float(input("Y1:"))
Y2 = float(input("Y2:"))

j = X2 - X1
k = Y2 - Y1



m = k/j
print('m:' + str(m))


def y(x):
    f = x-X1
    h = m*f
    y = h+Y1
    #y = m*(x-X1) - Y1
    print(y)

y(25)