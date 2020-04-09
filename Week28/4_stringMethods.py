# This program created a class with two methods (get string or print string).

class String:
    def __init__(self):
        self.data = ''

    def getString(self):
        self.data = input()

    def printString(self):
        return self.data.upper()

print("Please enter a string:")
test = String()
test.getString()
print(test.printString())
