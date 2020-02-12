# encrypting the password (hash)
import hashlib
import os

# testing the hashing algorithm
password = '123456'
salt = os.urandom(32) # creating a random number, 32 characters long, in order to make the password longer and harder to crack

key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000) # utf-8 makes it so any symbol is accepted. sha256 is the hashing protocol. 1000 is the number of times it runs
print(key)

password_entered = '12345'
key_check = hashlib.pbkdf2_hmac('sha256', password_entered.encode('utf-8'), salt, 1000)

if key == key_check:
    print('Logging in...')
else:
    print('Incorrect password.')