'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.

- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...


'''


class Calculator:
    """
    mimicks actions of calculator
    """
    a = 10
    b = 9
    c = 8

    # if a user does not input values when initialising an object, you can provide the object
    # with default values, shown in the example below
    def __init__(self, x=300, y="Woop-Woop-"):
        self.x = x
        self.y = y

    def addclass_objectvalues(self):
        return Calculator.a * self.y

    def __str__(self):
        return f" x = {self.x}, y = { self.y}, Class plus Object = {self.addclass_objectvalues()}"


cal1 = Calculator(3)
print(cal1)


cal2 = Calculator(2, "oh yeah! ")
print(cal2)


class Coffee:
    """
    defines details coffee order
    """
    barrista: str = "MJ"
    store = "high street"
    order_number = 1

    def __int__(self, size, hot_or_cold):
        self.size = size
        self.hot_or_cold = hot_or_cold
        return self.order_number + 1

    def order_list(self,  customer_name):
        self.customer_name = customer_name
        return customer_name

    def __str__(self):
        return f" {self.barrista} prepared order number {self.order_number} for customer {self.customer_name}"


espresso = Coffee()
espresso.order_number += 1
espresso.order_list("JM")
print(espresso)
mocha = Coffee()
mocha.order_number += 2
print(mocha)
