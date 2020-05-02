### Graph an exponential function: f(x) = (x+1)^2 - 1, with x from -2, to 2 with 1000 points. 

```.py import matplotlib.pyplot as pyplot

x = []
y = [] # y = (x+1)**2 - 1
minimum = -2
for i in range(1000):
    x.append(minimum + 0.004 * (i + 1))
    y.append(((x[i]+1)**2) - 1)

pyplot.plot(x, y)
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()
```

**Fig. 1:** The exponential function graphed by the program above.

![exponentialFeb23](exponentialFeb23.png)
