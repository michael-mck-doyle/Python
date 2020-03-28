

'''

__ While __ statement
example taken from book, "A Byte of Python", "Control Flow" section - https://python.swaroopch.com/control_flow.html

The while statement allows you to repeatedly execute a block of statements
as long as a condition is true. A while statement is an example of what is
called a looping statement. A while statement can have an optional else clause.

Notice how it differs from the 'if' statement,
We move the input and if statements to inside the while loop
and set the variable running to True before the while loop.
'''


number = 23
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations, you guessed it.')
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
    # Do anything else you want to do here

print('Done')