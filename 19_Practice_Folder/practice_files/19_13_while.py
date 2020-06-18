

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
import webbrowser

import countdown as countdown

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


count = 5
while count > 0:
  print(count)
  count += -1

# always make sure there is a condition that terminates the loop
# above we decremented the count variable
# below we use a control statement
while True:
  prompt = input('say something: ')
  if prompt == 'quit':
    break
  print(prompt[::-1])
print("bye!! (it's tiuq, btw. ;)")


# webbrowser.open('https://inventwithpython.com/') # opens the web page

def countdown(n):
    while n > 0:
        print(n)
    n = n - 1
    print('Blastoff!')


#course exercise
people = [
            ['Bilbo', 'Baggins'],
            ['Gollum'],
            ['Tom', 'Bombadil'],
            ['Aragorn']
        ]

# Change everything below here to use while loops instead

person = 0
name = 0
while person < people(len()):
    to_print = ""
    person += 1
    while name < person:
        to_print += name + " "
        name +=1
    print(to_print)

print("Looks about right?!")

#for person in people:
    #to_print = ""
    #for name in person:
       # to_print += name + " "
    #print(to_print)