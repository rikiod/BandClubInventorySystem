# This program takes a list of words separated by commas and alphabetizes them.

print("Please enter a list of words separated by commas:")

list = input().split(',')  # splitting words along commas 
list = sorted(list)  # alphabetically sorting words 
list = ','.join(list)  # joining words with commas 

print(list)
