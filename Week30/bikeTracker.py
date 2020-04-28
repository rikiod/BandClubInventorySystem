bikes = [] #  creating an empty list in which to store the bikes

class Bicycle:
    numberBikes = 0

    def __init__(self, tyre_size = 29, chain = 11, size = 'M')
        self.tyre_size = tyre_size
        self.chain = chain
        self.size = size
        bikes.append(self) #  editing the bike list by adding this object
        Bicycle.numberBikes += 1 #  tracking the number of bikes

    def post_initialize(self):
        print(self.tyre_size / 2 * 3.1416) #  took "tyre size" to mean the diameter of the wheel and used the number 3.1416 for pi

    def spares(self):
        print(f"Tyre size: {self.tyre_size} inches")
        print(f"Chain speed: {self.chain}")

class MountainBike(Bicycle): #  inheriting from Bicycle class because of second parameter
    numberMountainBikes = 0

    def __init__(self, tyre_size = 27.5, chain, size, front_fork = 100, rear_shock = 80) 
        Bicycle.__init__(self, size, chain) #  taking values from parent class 
        self.tyre_size = tyre_size
        self.front_fork = front_fork
        self.rear_shock = rear_shock
        MountainBike.numberMountainBikes += 1
