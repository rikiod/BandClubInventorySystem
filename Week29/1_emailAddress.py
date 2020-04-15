# This program takes the first name, last name, and a number from the user. It then writes all of the emails for that number into a text file.

firstName = input('Please input your first name, last name, and a number between 1 and 99, separated by commas: ')
userData = input()
userData = list.split(",")

number = int(list[2])
if number < 2:
    num = 2
elif number > 100:
    number = 100

file = open('email.txt', 'w')
for i in range(1, number+1):
    finalEmail = list[1].lower() + '.' + list[2].lower() + str(i + 1) + '@uwcisak.jp'
    f.write(finalEmail)
    f.write('\n') 
file.close()



