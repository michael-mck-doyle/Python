'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

test_input = input("Enter any number: ")


def four_or_seven(test_input):
    x = int(test_input) % 4
    y = int(test_input) % 7

    if x == 0 or y == 0:
        return True
    else:
        return False
    '''if int(test_input) % 4 == 0:
        x = True
        return x
    elif int(test_input) % 7 == 0:
        x = True
        return x
    else:
        return "The number you entered is not divisible by 4 or 7 without remainder"'''


div = four_or_seven(test_input)
print(div)


# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

test_input = input("Enter any number: ")


def four_and_seven(test_input):

    x = int(test_input) % 4
    y = int(test_input) % 7

    if x == 0 and y == 0:
        return True
    else:
        return False


div = four_and_seven(test_input)
print(div)


def num_input():
    num = input("Enter a number between 1 an 1,000,000: ")
    y = int(num)
    if y in range(1, 1000000):
        return y
    else:
        return "The number you entered is not within the required range"


x = num_input()
print(x, "is a number between 1 and 1,000,000")



# call your functions, passing in the user input as the arguments, and set their output equal to new variables 



# print your new variables to display the results
