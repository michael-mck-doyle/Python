'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''


import math


class Rectangle():
    """calculate the area of a rectangle"""

    def __init__(self, r_length, r_height):
        self.r_length = r_length
        self.r_height = r_height

    def rectangle_area(self):
        return self.r_length * self.r_height

    def rectangle_perimeter(self):
        return self.r_height * 2 + self.r_length * 2

    def __str__(self):
        return f"The area of the rectangle is {self.rectangle_area()} and the perimeter is {self.rectangle_perimeter()}."


rect = Rectangle(8, 14)
print(rect)

class Circle:
    """calculate the area of a circle"""

    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return math.pi * self.radius**2

    def circle_circumference(self):
        return math.pi * self.radius * 2

    def __str__(self):
        return f"The area of the circle is {round(self.circle_area(),5)} and the circumference is {round(self.circle_circumference(), 5)}."




circ = Circle(5)
print(circ)
