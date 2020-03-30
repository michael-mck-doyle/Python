

'''

__ For....in.. __ statement

example taken from book, "A Byte of Python", "Control Flow" section - https://python.swaroopch.com/control_flow.html

Traversal with a for loop  - http://greenteapress.com/thinkpython2/html/thinkpython2009.html#sec94


The for..in statement is another looping statement which iterates over
a sequence of objects i.e. go through each item in a sequence. We will see more
about sequences in detail in later chapters. What you need to know right now
is that a sequence is just an ordered collection of items.

In this program, we are printing a sequence of numbers. We generate this sequence
of numbers using the built-in range function.
What we do here is supply it two numbers and range returns a sequence of numbers starting
from the first number and up to the second number.
For example, range(1,5) gives the sequence [1, 2, 3, 4]. By default, range takes a step count of 1.
If we supply a third number to range, then that becomes the step count. For example, range(1,5,2) gives [1,3].
Remember that the range extends up to the second number i.e. it does not include the second number.

Note that range() generates only one number at a time,
if you want the full list of numbers, call list() on the range(),
for example, list(range(5)) will result in [0, 1, 2, 3, 4]. Lists are explained in the data structures chapter.

'''


'''

for i in range(1, 10):
    print(i - 1)
    print("hello next number")
else:
    print('The for loop is over')

print("next for loop __" * 3)
print()

# the 3rd number in the range i.e. 2, is the step sequence.  normally it is 1 but you can
# change this by using a 3rd number to indicate the step sequence
for i in range(1, 10, 2):
    print(i - 1)
    print("hello next number")
else:
    print('The for loop is over')

print("next for loop __" * 3)
print()


print()
print()

# you can use keyword 'and' to search between two numbers

#number = 5
number = int(input('Enter an integer : '))
if number == 5:
    print("it's 5!")
elif number < 5:
    print("too low!")
elif number > 5 and number < 20:
    print("good guess but not quite.")
else:
    print("whoa slow down! so high, take care!")

print()
print()

my_list = [1, 2, 3, "hello", "it's blue!", 10]

for item in my_list:
    print(item)

print()
print()

fruit = (input('Enter a fruit : '))
for letter in fruit:
    print(letter)

print()
print()

users = {'mary': 22, 'caroline': 26, 20: 20}
# let's make them age for 30 years each!

for user, age in users.items():
    aged = int((age + 30)/2)
    print(user, aged)


print()
print()
fruit = (input('Enter a fruit : '))
index = -1
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index - 1

print("Finished")



#Using the range function, write a for loop that counts from 1 to 10 and prints each number to the console.
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and ends at a specified number.
x = range(1,11)
for i in x:
    print(i)
'''

#Using the list provided below, write a for loop to iterate over the list
#and find (and print) the sum of all the numbers in the list.

example_list = [2, 5, 7, 9, 3, 8, 8]

x = 0
for i in example_list:
    x = x + i
print(x)

