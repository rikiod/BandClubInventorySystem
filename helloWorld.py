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


# 4. we have a defined array (list of numbers) with
num = [3, 38, 5, 44, 15, 36, 26, 27, 2, 46, 4, 19, 47, 48, 50]
n = len(val)

#for x in range(n-1):
  #  leftElement = val[x]
  #  rightElement = val[x+1]
   # print("Primary number {}, secondary number {}.".format(leftElement, rightElement)
   # if leftElement > rightElement:
   #     num[x], num[x+1] = num[x+1], num[x]



# Read an integer:
a = int(input())
print ('The next number for the number' + a + 'is' + (a+1))
print ('The previous number for the number' + a + 'is' + (a-1))
