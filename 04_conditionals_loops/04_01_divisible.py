'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''

x = input("Enter a number between 1 and 1,000,000: ")
if int(x) < 0:
    print("PLease enter a positive number")
if int(x) == 0:
    print("zero is not a valid input")

y = int(x) % 3
if y != 0:
    print("Please try again, there is a remainder")
elif y == 0:
    print("Congratulations ", x, " divided by 3 has zero remainder!")
else:
    print("There seems to be an error with your input")


print("done")
