# This program converts an age into dog years.

print("Please input the age in human years:")
dogYears = 0
humanYears = int(input())

for i in range(1, humanYears + 1):
    if i <= 2:
        dogYears += 10.5
    else:
        dogYears += 4
print("The age in dog years is", int(dogYears))
