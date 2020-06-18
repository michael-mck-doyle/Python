
'''

__ If __ statement

example taken from book, "A Byte of Python", "Control Flow" section - https://python.swaroopch.com/control_flow.html


The if statement is used to check a condition:
if the condition is true we run a block of statements (called the if-block),
else we process another block of statements (called the else-block).
The else clause is optional.


'''


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


print()
print()

x = 5
y = 10
if x < 5:
    print("one")
elif x > 5:
    print("two")
else:
    print("three")
if x >= 5 and y < 10:
    print("four")
elif x < y and  y == 10:
    print("five")
else:
    print("six")

