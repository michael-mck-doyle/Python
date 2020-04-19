
'''
__ Handling Exceptions __

- enclose the code you think might generate an exception in a "try: / except" along with the exception type you
are expecting it to handle.
- you can add and "else" statement to do something if the code executes as expected without an exception
- the 'finally" statement can be used to end whatever needs to be cleaned up e.g. close an open file...no matter
what happens it will execute.
- "raise" custom exceptions - you can actually raise your own exception if you actually want a program to terminate (which
is the opposite of the try: / except which is designed to stop the program crashing!).
- custom exceptions - you cam create your own custom exception class and use it in your program to generate and exception message - see below
'''


while True:
    try:
        x = float(input("Please enter a number: "))
        y = float(input("Please enter another number: "))
        z = x / y
        print(z)
    except ValueError as ver:
        print("only numbers are acceptable in this calculation.  Please enter a number.", ver)
    except NameError as nme:
        print("Re-enter a number", nme)
    except ZeroDivisionError as zde:
        print("Zero is an invalid divisor.  Please try again.", zde)
    else:
        print("Good job!")
    finally:
        break


# custom exception
class DontGoThere(Exception):
    pass
x = 0
while x < 3:
    try:
        dividend = int(input('Enter a number: '))
        divisor = int(input("Enter another number: "))
    except ValueError:
        raise DontGoThere('don\'t even try this!')
    # catching an exception
    try:
        print(dividend/divisor)
    except ZeroDivisionError as zde:
        print("cannot divide by zero")

