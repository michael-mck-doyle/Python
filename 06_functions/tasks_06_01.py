'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 OR 7 and returns a boolean

#a = input("Enter any number: ")


def mod4_or_7(a):
    x = int(a) % 4
    y = int(a) % 7

    if x == 0 or y == 0:
        return True
    else:
        return False


div = mod4_or_7(98)
print(div)


# define a function that determines whether a number is divisible by both 4 AND 7 and returns a boolean

#b = input("Enter any number: ")


def mod4_and_7(b):

    x = int(b) % 4
    y = int(b) % 7

    if x == 0 and y == 0:
        return True
    else:
        return False


div = mod4_and_7(102)
print(div)


# call your functions, passing in the user input as the arguments, and set their output equal to new variables
# print your new variables to display the results


"""
def num_input():
    num = input("Enter a number between 1 an 1,000,000: ")
    y = int(num)
    if y in range(1, 1000000):
        return y
    else:
        return "The number you entered is not within the required range"

x = num_input()
print(x, "is a number between 1 and 1,000,000")
"""

