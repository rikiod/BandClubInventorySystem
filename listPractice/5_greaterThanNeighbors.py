# Given a list of numbers, determine and print the quantity of elements that are greater than both of their neighbors.

total = 0
numbers = [int(i) for i in input().split()]
for i in range (1, len(numbers)-1):
    if numbers[i-1] < numbers[i] > numbers[i+1]:
        total += 1
print(total)