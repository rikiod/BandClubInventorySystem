# This program (#1) takes a string and then finds the number of digits and letters in it.

print("Please enter a string:")
string = input()

numberDigits = 0
numberLetters = 0

for i in string:
    if i.isalpha():
        numberDigits +=1
    if i.isdigit():
        numberLetters +=1
print("The number of digits in the string:", numberDigits)
print("The number of letters in the string:", numberLetters)
