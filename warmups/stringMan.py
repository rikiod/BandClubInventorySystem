# This warmup (2/14/2020) can be viewed on Classroom.

file = open('extract.txt', "r") # r is to read. other options are write or append
extract = file.read()

# finding number of words in the extract (1)
splitWords = extract.split()
numberWords = len(splitWords)
print(numberWords)

# checking if any of these keywords are inside the text extract (2)
keywords = ['house', 'worker', 'master', 'hard', 'responsible', 'skillful']
for kwd in keywords:
    print('Checking for word {} in the text.'.format(kwd))
    print (kwd in extract)

# using a f string to show a message indicating the number of letters (3)
countAlpha = 0
for letter in extract:
    if letter.isalpha(): # if letter is in the alphabet (a-z). alphanum includes numbers
        countAlpha += 1
print(f'There are {countAlpha} letters (A-Z) out of {len(extract)} total characters (including spaces).') # f string

# making the extract entirely lowercase (4)
print(extract.lower()) # using lower function

# use join to print all the words in the text longer than 5 characters with a # appended at the beginning (5)
longWords = list(filter(lambda x: len(x) > 5, splitWords)) # filter takes the last and applies a function to each
# element. the true ones are kept.
print(len(longWords))
print(' #'.join(longWords))

# calculate the total addition of all the numeric codes for the letters in the text (6)
total = 0
for letter in extract:
    total += ord(letter) # converting the letter to a number (unicode)
print(total)

# basic encryption (convert letters to unicode, add a number, and encode it by adding that number)
userMessage = input('Please enter a message.')
userNumber = int(input('Please enter a number to encode your message.'))
print(''.join(map(lambda x: chr(ord(x)+userNumber), userMessage)))