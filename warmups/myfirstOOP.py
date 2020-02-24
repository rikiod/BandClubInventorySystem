# From the paper handout, "Object-Oriented Programming (OOP) in Python 3"


class Dogs:
    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)

    # Instance Method
    def speak(self, sound):
        return "{} says {}.".format(self.name, sound)

    # Instance Method (changing an attribute of an object)
    def birthday(self):
        self.age += 1

# Child class (inheriting from parent Dog class)
class RussellTerrier(Dogs):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inheriting from parent Dog class)
class Bulldog(Dogs):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

def get_biggest_number(*args): # any value put in the function will be an argument. star means all the arguments.
    biggest = max(args)
    print("The biggest is {}".format(biggest))

philo = Dogs("Philo", 5)
mikey = Dogs("Mikey", 6)
spot = Dogs("Spot", 12)
mitsu = Dogs("Mitsu", 9)
bella = Dogs("Bella", 6)

get_biggest_number(philo.age, mikey.age, spot.age, mitsu.age, bella.age)

# Child classes inherit attributes and behaviors from the parent class
jim = Bulldog("Jim", 12)
print(jim.description())

# Child classes have specific attributes and behaviors as well
print(jim.run("slowly"))

print("{} is {} and {} is {}.".format(philo.name, philo.age, mikey.name, mikey.age))

if philo.species == "mammal":
    print("{} is a {}!".format(philo.name, philo.species))

print(mikey.description())
print(mikey.speak("ruff ruff"))

print("Mikey is {} years old.".format(mikey.age))
mikey.birthday()
print("After Mikey's birthday, he is now {} years old.".format(mikey.age))







