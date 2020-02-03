# 1. this program prints hello world
print('Hello world')


# 2. this program checks for an odd or even number
# numbers from 1 to 1000
for x in range(1, 1001): # has option to change how large the step is but default is one
    if x % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    print("{} is {}".format(x, parity))


# 3. defining an array or list in python
# we'll calculate the mean, max, and min
val = [34, 4, 46, 13, 12, 45, 6, 7, 78, 67, 45, 34, 23]
n = len(val)
sumVal = 0

for ind in range(n): # index is the name of the variable. can also be replaced with (n) because the 0 is implicit
    sumVal += val[ind]
print("The sum is {}".format(sumVal))

sumVal = 0
for ele in val: # takes every element of the array
    sumVal += ele
print("The sum is {}".format(sumVal))


# 4. bubble sort
n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
