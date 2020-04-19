

class Car:
    """
    The Car class creates blueprint for a car
    """

    def __init__(self, model, year, speed):
        '''
            creates blueprint for a car
            '''
        self.model = model
        self.year = year
        self.speed = speed

    breakpoint()

    def accelerate(self):
        """
            accelerates the speed of the car
            """
        self.speed += 5

    def brake(self):
        """
        decreases the speed of the car by 5
        """
        if self.speed <= 5:
            print("The car has already stopped")
        else:
            self.speed -= 5

    def honk_honk(self):
        """
        honks the car horn
        """
        return f"{self.model} goes 'beep beep"

    def __str__(self):
        return f"Volkswagen make a car called {self.model} with a top speed of {self.speed} mph"

    print(honk_honk.__doc__)
    print(brake.__doc__)
    print(accelerate.__doc__)


print(Car.__doc__)

VWGolf = Car('Golf', 2020, 4)

print(VWGolf)

VWGolf.brake()

VWGolf.brake()
print(VWGolf)

print(VWGolf.honk_honk())
