import matplotlib.pyplot as plt
# X = number of impact
# Y = Moisture percentage


X1 = float(input("x1:"))
X2 = float(input("x2:"))

Y1 = float(input("Y1:"))
Y2 = float(input("Y2:"))

j = X2 - X1
k = Y2 - Y1



m = k/j
#print('m:' + str(m))


def f(x):
    f = x-X1
    h = m*f
    global y
    y = h+Y1
    #y = m*(x-X1) - Y1
    print(y)

f(25)
X = sorted([25, X1, X2])
Y = [Y1, Y2, y]
print(X)
print(Y)

fig, ax = plt.subplots()
ax.plot(X, Y)
plt.show()