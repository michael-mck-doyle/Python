'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

x = 10
x = 10/3
print(x)
x = int(x)
print(x)
x = 10 /4
print(x)
x = 10//4
print(x)

x = int(input("Please enter a number: "))
y = int(input("Please enter another number: "))

x = x * y
print("multiplying these numbers gives you: " + str(x))

