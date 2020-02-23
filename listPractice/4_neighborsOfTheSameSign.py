# Given a list of numbers, find and print the first adjacent elements which have the same sign. If there is no such
# pair, leave the output blank.

numbers = [int(i) for i in input().split()]
for i in range (1, len(numbers)):
    if numbers[i] * numbers[i-1] > 0:
        print (numbers[i-1], numbers[i])
        break