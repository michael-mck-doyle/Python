'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''


class Ingredient:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour


i = Ingredient(name='carrot', colour='orange')
print(i)
print(i.name, i.colour)
c = Ingredient('cabbage', 'green')
print(c)
print(c.name, c.colour)





