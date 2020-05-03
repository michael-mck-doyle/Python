'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.

- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class


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

#__________________________________________________________________________


class CarPark:
    """
    count the cars in a car park and return the number of available spaces
    """
    car_spaces = 400
    suv_spaces = 50

    def __init__(self, num_cars=0, num_suvs=0):
        self.num_cars = num_cars
        self.num_suvs = num_suvs

    def calculate_spaces(self):
        if CarPark.car_spaces - self.num_cars == 0:
            print(f"The car park is full. There are no spaces available.")
        else:
            return CarPark.car_spaces - self.num_cars

    def __str__(self):
        return f"There are {self.calculate_spaces()} empty spaces in the car park"


print()
HopeStreet = CarPark(400)
print(HopeStreet)


#_______________________________________________


class Employee:
    """"
    employee class for onboarding new employees
    """
    raise_amount = 1.05
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + "@company.com"

    #def __str__(self):
        #return f"Employee {self.first} {self.last} earns {self.pay} "

    def fullname(self):
        return self.first + " " + self.last

#printing namespace



John = Employee("John", "Smith", 50000)
Mary = Employee("Mary", "Smith", 60000)
print()
print(John.fullname())
print(Mary.fullname())


#  ---------------------------------------------
# using print(object.__dict__) returns details of the namespace for an object

class CoffeeShop:
    """
    calculate price of coffee order
    """
    price = 1
    small = price * 1.15
    medium = price * 1.55
    large = price * 1.85
    num_orders = 0

    def __init__(self, size):
        self.size = size

        CoffeeShop.num_orders += 1

    def order_price(self):
        if self.size == "small":
            return CoffeeShop.small * CoffeeShop.price
        elif self.size == "medium":
            return CoffeeShop.medium * CoffeeShop.price
        elif self.size == "large":
            return CoffeeShop.large * CoffeeShop.price
        else:
            print("Choose another item from the menu.")

    def __str__(self):
        return f"The price of your coffee is ${self.order_price()}.  There are {CoffeeShop.num_orders} orders so far."


print()
espresso = CoffeeShop("small")
print(espresso)
print(espresso.__dict__)
print(CoffeeShop.__dict__)
print()
mocha = CoffeeShop("medium")
print(mocha)
latte = CoffeeShop("large")
print(latte)

CoffeeShop.price = 2
print()
print("After price raise:")
print(espresso)
print(mocha)
print(latte)

machiato = CoffeeShop("small")
print(machiato)
print(machiato.__dict__)

#_________________________________________________


