# Tasks for everyone:
# ① 　Generate 1000 random numbers between 1 and 100. Create a graph for this numbers where the x axis are the numbers 1 to 1000, and the y axis are the random numbers.
# ②　 Calculate the average of the 1000 random numbers in ① using a loop.
# ③ 　Graph the equation for the wave function 14*sin(0.5*x) in the range x = [-10, 10] with steps of 0.1.
# ④ 　Create the graph on any other mathematical function you know.
import math

import matplotlib.pyplot as pyplot
import random

# graphing 1000 random numbers between 1 and 100
x = [i for i in range(1, 1000)]
y = [random.randint(1, 100) for i in x] # same as appending

# calculating the average of the 1000 random numbers using a loop
sum = 0
for num in y:
    sum = sum + num
avg = sum / 1000
print(avg)

# alternative way to create steps without using numpy library
x = []
y = [] # y = 14sin(0.5x)
minimum = -10
for i in range(200):
    x.append(minimum + 0.1 * (i + 1))
    y.append(14 * math.sin(0.5 * x[i]))

# graphing the numbers
pyplot.plot(x, y)
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()

# graphing the sine function
x = np.arange(-10, 10, 0.1) # setting range from -10 to 10 with steps of 0.1
y = np.sin(0.5 * x) * 14
pyplot.show()

# graphing a circle
fig, ax = pyplot.subplots() # defining a set of axes
ax.set(xlim=(-10, 10), ylim = (-10, 10)) # setting window of axes

a_circle = pyplot.Circle((3, 3), 2) # setting center to (3, 3) and radius to 2
ax.add_artist(a_circle) # adding circle to axis


