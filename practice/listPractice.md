## 1. Even Indices

```.py # Given a list of numbers, find and print all the list elements with an even index number.

numbers = input().split() # receiving input and putting into list of strings (reason for last of int when putting in input)
for i in range(0, len(numbers), 2): # step of 2 in order to get only even numbers
    print(numbers[i]) 
 ``` 
    
## 2. Even Elements

```.py # Given a list of numbers, find and print all elements that are an even number. In this case use a for-loop that
# iterates over the list, and not over its indices! That is, don't use range()

numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
for element in numbers:
    if element % 2 == 0:
        print (element)    
```
        
## 3. Greater than Previous
```.py # Given a list of numbers, find and print all the elements that are greater than the previous element.

numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
for i in range (1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        print(numbers[i])

# after looking closer at this program, I can see that the first three lines could be optimized into one:
# numbers = [int(i) for i in input().split()] 
``` 

## 4. Neighbors of the Same Sign
```.py # Given a list of numbers, find and print the first adjacent elements which have the same sign. If there is no such
# pair, leave the output blank.

numbers = [int(i) for i in input().split()]
for i in range (1, len(numbers)):
    if numbers[i] * numbers[i-1] > 0:
        print (numbers[i-1], numbers[i])
        break 
```
        
## 5. Greater than Neighbors
```.py # Given a list of numbers, determine and print the quantity of elements that are greater than both of their neighbors.

total = 0
numbers = [int(i) for i in input().split()]
for i in range (1, len(numbers)-1):
    if numbers[i-1] < numbers[i] > numbers[i+1]:
        total += 1
print(total) 
```
