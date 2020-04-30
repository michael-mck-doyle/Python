'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''


class Automobile:
    """ class describing the constituents of a car"""

    def __init__(self, model, year, speed):
        self.model = model
        self.year = year
        self.speed = speed

    def increase_speed(self):
        self.speed += 5

    def __str__(self):
        return f"The car is a {self.model} manufactured in {self.year} travelling at a speed of {self.speed}"


VW = Automobile("Golf", "2020", 45)
print(VW)

VW.increase_speed()
print(VW)
