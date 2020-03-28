
'''

__ References __

Control Flow - https://python.swaroopch.com/control_flow.html

There are three control flow statements in Python - if, for and while

Notice how the if statement contains a colon at the end
- we are indicating to Python that a block of statements follows
Note, this also applies to following "elif" and and "else" statements i.e. they should also be followed by a ':'

if guess == number:
elif guess < number:
else:

Remember that the elif and else parts are optional. A minimal valid if statement is:
if True:
    print('Yes, it is true')

'''

flag = True

# if the condition evaluates to True, the indented code gets executed
# otherwise it is simply skipped
if flag == False:
    print("yay!")

print("nothing printed - guess it was False")


#  If Statement

number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    # New block starts here
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
    # New block ends here
elif guess < number:
    # Another block
    print('No, it is a little higher than that')
    # You can do whatever you want in a block ...
else:
    print('No, it is a little lower than that')
    # you must have guessed > number to reach here

print('Done')
# This last statement is always executed,
# after the if statement is executed.
