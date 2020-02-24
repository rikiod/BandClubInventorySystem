# Graph the following function: f(t) = | 3sin(0.3t) |
# t is greater/equal to 0, less than 50. steps of 0.01

import matplotlib.pyplot as plot
import math

x = [0]
y = [0] # y
minimum = 0
step = 0.01
numberPoints = int(50 / step)
for i in range(numberPoints):
    x.append(minimum + step * (i + 1))
    y.append(abs(3 * math.sin(0.3 * x[i])))

diff =[0, 0]
zeros = [0, 0]
for i in range(numberPoints - 1):
    diff.append(y[i] - y[i+1])
    if diff[-1] == 0:
        zeros.append(1)
    else:
        zeros.append(0)

print(len(x), len(diff))
plot.plot(x, diff, 'r')
plot.show()




