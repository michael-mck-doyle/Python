'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''

try:
    x = input("Please enter a number: ")

    if x != type(int):
        print("Sorry, this calculation only works with integer types. Please enter an integer.")

    x = x * 2
    print(f"Your value multiplied by 2 is: {x}")
except:
    print()
