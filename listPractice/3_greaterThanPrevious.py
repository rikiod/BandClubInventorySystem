# Given a list of numbers, find and print all the elements that are greater than the previous element.

numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
for i in range (1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        print(numbers[i])

# after looking closer at this program, I can see that the first three lines could be optimized into one:
# numbers = [int(i) for i in input().split()]
