# This program intends to be the method of sign in for the user of the Python Unit 3 project.

import myLib
import hashlib
import os
import binascii

user = {'username': None, 'password-hash': None, 'salt': None} # none means empty/undefined; essentially a template (
# dictionary). the green text is the "key" while the orange text is the "value"

# displaying the menu
print("1 - Register ")
print("2 - Log In")
print("3 - Exit")

opt = 10
while opt > 3: # once the user enters something less than 3, the loop will break (checking user entered a valid option)
    opt = int(input("Enter option (1, 2, or 3) "))

# user entered #1 (registration)
username = input("Please choose a username: ")  # TO DO: check if username is unique
confirmed = False
while not confirmed:
    password = input("Enter your password: ")
    password_test = input("Confirm your password: ")
    if password == password_test: # you can use is or ==
        confirmed = True
print('Thank you for registering!')

# encrypting the password
salt = os.urandom(32) # 32 bytes
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)
# print(binascii.hexlify(key)) # the binascii library converts the bits on the key into characters for us to read. this
# is the hash

user['username'] = username # placing values inside the dictionary
user['password-hash'] = key
user['salt'] = salt

# encrypt password (generate salt, use hashlib function, store info (user_dict)) THESE WERE STEPS FOR REGISTRATION

# user entered #2 (log in)
entered_username = input("Please enter your username: ")
entered_password = input("Please enter your password, {}: ".format(entered_username))
hashed_password = hashlib.pbkdf2_hmac('sha256', entered_password.encode('utf-8'), salt, 1000) # hashing entered pw
if user['password-hash'] == hashed_password and user['username'] == entered_username: # checking entered password and
# username against dictionary
    print("Successfully logged in.")
else:
    opt = 10 # returning back to menu
    while opt > 3:
        print("1 - Register ")
        print("2 - Log In")
        print("3 - Exit")
        opt = int(input("Please try again by entering option 1, 2, or 3: "))

