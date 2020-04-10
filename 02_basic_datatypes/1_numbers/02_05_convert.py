'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

x = 10

# results in float
x = 10/3
print(x)

# convert float to int
x = int(x)
print(x)

# division results in float
x = 10/4
print(x)

# floor division
x = 10//4
print(x)

#Use two user inputted values to perform multiplication.
x = int(input("Please enter a number: "))
y = int(input("Please enter another number: "))

x = x * y
print("multiplying these numbers gives you: " + str(x))

