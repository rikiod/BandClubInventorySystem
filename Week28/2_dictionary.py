# This program creates a dictionary with numbers and their squares up to the integer entered. 

dict = {}

print('Please enter an integer:')
num = int(input())

for i in range(1, num+1):
    dict[i] = i ** 2

print(dict)
