# This program finds the largest prime number out of a set of ten numbers.

# 1. input 10 numbers
# 2. find prime factors
# 3. find the largest

import math

def testPrime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
        return True    

prime = []
num = []

for i in range(10):
    num.append(int(input('Enter a number: ')))
print (num)

for i in range (10):
    if testPrime(num[i]) == "True":
        prime.append(num)
print (prime)

# print("The largest prime number is:", max(prime))          