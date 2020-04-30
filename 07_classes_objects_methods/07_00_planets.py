'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()


dunder methods in a class include:

# this is a constructor method used when initialising an object.  The object needs to pass these variables when it is created.
def __init__(self, other_variables):
    self.other_variables = other_variables

# this returns a more readable description of the object
def __str__(self):
    return f"Planet {self.other_variables} is a {self.other_variables} planet in the {self.other_variables}."

# similar to __str__ above but recommended more for developers or preferred amongst the two options
def___repr__(self):
    return f"Planet {self.other_variables} is a {self.other_variables} planet in the {self.other_variables}."

'''


class Planet():
    """blueprint for building planets"""

    def __init__(self, size, colour, temperature):
        self.size = size
        self.colour = colour
        self.temperature = temperature

    def __str__(self):
        return f"You've discovered a {self.size} sized, {self.colour} planet which is very {self.temperature}!"

    def __repr__(self):
        return f"You've discovered a {self.size} sized, {self.colour} planet which is very {self.temperature}!"


mars = Planet("medium", "red", "hot")

print(Planet)
print(mars)

mars.colour = "blue"
mars.temperature = "cold"

print(mars)



