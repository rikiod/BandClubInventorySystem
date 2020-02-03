# This program finds the number of zeros in a set of inputs.
n = int(input())
number = 0

for i in range(n):
    if int(input()) == 0:
        number +=1
print(number)