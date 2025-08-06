from matplotlib import pyplot as plt
import random

x = []
y = []
for i in range(50):
    x.append(i+1)
    y.append(random.randint(1, 25))

plt.bar(x, y)
for i in range(len(y)):
    for j in range(i+1, len(y)):
        if y[i] > y[j]:
            t = y[i]
            y[i] = y[j]
            y[j] = t
plt.bar(x, y)
plt.show()