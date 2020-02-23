# Given a list of numbers, find and print all elements that are an even number. In this case use a for-loop that
# iterates over the list, and not over its indices! That is, don't use range()

numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
for element in numbers:
    if element % 2 == 0:
        print (element)
