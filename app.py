x1 = input("x1:")
x2 = input("x2:")

N1 = input("N1:")
N2 = input("N2:")

k = float(N2) - float(N1)
j = float(x2) - float(x1)

m = k/j

def y(x):
    y = m*(float(x)-float(x1))-float(N1)
    print(y)

y(25)