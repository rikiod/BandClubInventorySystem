# Given a list of numbers, find and print all the list elements with an even index number.

numbers = input().split() # receiving input and putting into list of strings (reason for last of int when putting in input)
for i in range(0, len(numbers), 2): # step of 2 in order to get only even numbers
    print(numbers[i])