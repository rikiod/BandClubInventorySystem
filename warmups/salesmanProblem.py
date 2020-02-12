# Given four different cities and their coordinates (A, B, C, and D), find the distance between A and the three other cities.

import math
import myLib

cities = [(3, 5), (9, 10), (7, 8), (15, 7)] # the coordinate of the cities in order from a to d

for index in range(4):
    cityA = cities[index]
    for index_2 in range (index+1, 4):
        cityB = cities[index_2]
        d = myLib.distance(target=cityA, origin=cityB) # naming the inputs since parameters have names
        print('Distance between city {} and {} is {}'.format(index, index_2, d))

# zero is A, one is B, two is C, three is D. make it so when printed, it shows that instead 