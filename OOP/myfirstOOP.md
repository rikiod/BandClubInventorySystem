## My First Practice with Objected-Oriented Programming in Python

Here is the code for the practice (questions can be found in a paper handout given to us during class).

```.py 
# From the paper handout, "Object-Oriented Programming (OOP) in Python 3"

class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

class Dogs:
    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # Instance Method
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)

    # Instance Method
    def speak(self, sound):
        return "{} says {}.".format(self.name, sound)

    # Instance Method (changing an attribute of an object)
    def birthday(self):
        self.age += 1

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "{} is walking!".format(self.name)


# Child class (inheriting from parent Dog class)
class RussellTerrier(Dogs):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inheriting from parent Dog class)
class Bulldog(Dogs):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# EXERCISE 1

def get_biggest_number(*args): # any value put in the function will be an argument. star means all the arguments.
    biggest = max(args)
    print("The biggest is {}".format(biggest))
# to use the function: get_biggest_number(dog1.age, dog2.age, dog3.age, etc)


# EXERCISE 2

spot = Dogs("Spot", 12)
mitsu = Dogs("Mitsu", 9)
bella = Dogs("Bella", 6)
myDogs = [spot, mitsu, bella]

myPets = Pets(myDogs)
print("I have {} dogs.".format(len(myPets.dogs)))
for dog in myPets.dogs:
    print("{} is {}.".format(dog.name, dog.age))
    dog.eat()
print("And they're all {}s, of course.".format(dog.species))

# EXERCISE 3

hunger = False
for dog in myPets.dogs:
    if dog.is_hungry:
        hunger = True

if hunger:
    print("My dogs are hungry.")
else:
    print("My dogs are not hungry.")

# EXERCISE 4
myPets.walk()
```

**Questions**

4. When defining a new class, use the following: `class ClassName:`

5. The spelling convention for a class name is Camel Case notation (uppercase).

6. To create an instance of a class, use the following: `instance = Class()`

7. The attributes and behaviors of a class instance are accessed by using the instance's name, following by a period and then the attribute name.

8. A method is a function for a particular class.

9. The purpose of *self* is to refer to the object itself. 

10. The purpose of the \\__init__ method is to give an object a default value and thus, initialize its initial attributes.

11. Inheritance helps to prevent code duplication because child classes inherit all of parent class' attributes and behaviors. 

12. Child classes can not override the inherited properties of their parent classes. 

